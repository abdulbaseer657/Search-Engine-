import pickle
from collections import defaultdict
import math
from query_pre_processing import remove_tags_query
from functools import reduce
import sys

#collecting word list using pickle
file2 = open(r'Pre_Processing/Saved_pickle_files/dict.pkl', 'rb')
tokens_list_word = pickle.load(file2)
file2.close()
#print(tokens_list_word)

#Collecting dictionary structure (specifically posting_dict) using pickle
file3 = open(r'Pre_Processing/Saved_pickle_files/postings_pf.pkl', 'rb')
posting_dict = pickle.load(file3)
file3.close()
#print(posting_dict)

#Collecting dictionary structure (specifically posting_dict) using pickle
file4 = open(r'Pre_Processing/Saved_pickle_files/all_docs_pf.pkl', 'rb')
all_doc_dicts = pickle.load(file4)
file3.close()
#print(all_doc_dicts) - list of all the documnets in dictionary format
#print(tokens_list_word)

#Collecting all the keys using pickle
#file5 = open(r'keys.pkl', 'rb')
#keys = pickle.load(file5)
#print(keys)
#file5.close()

#This is a document frequency
frequency = defaultdict(int)
#print(freq) - prints - defaultdict(<class 'int'>, {}) - as it does above

#This gives inverse documnet frequency
inverse_freq_value = 0

# This is a dictionary, who's keys are document ids and vlues are Euclidean distance of corresponding documnet vector
euclid_len = defaultdict(float)
#print(euclid_len ) - prints - defaultdict(<class 'float'>, {})


#cosine_similarity_score = 0
# Total number of documnets
total_len_docs = len(all_doc_dicts)
#print(total_len_docs)

def main_func(query):
	#Initializing term length to frequency
	term_length_to_freq()
	#Initializing Euclidean length
	euclid_length_docs()
	#get_res the query from the user
	enter_query_user(query)

def term_length_to_freq():
	#Stores the frequency of each token in the global freq structure
	global frequency
	for tokens in tokens_list_word:
		frequency[tokens] = len(posting_dict[tokens])

#Now that we have calculated the frequency, we will find the inverse document frequency
def inverse_freq(tokens):
	if tokens in tokens_list_word:
		global inverse_freq_value
		#Using the formula idf = log10(N/df)
		inverse_freq_value = math.log10(total_len_docs/frequency[tokens])
		#Retutn frequency calulated by the formula
		#print(inverse_freq_value)
		return inverse_freq_value
	else:
		#Return 0 otherwise
		return inverse_freq_value

#Now we will calculate the tf_idf weight of each token
def weight(tokens, i):
	if i in posting_dict[tokens]:
		#Calculating weight, which is number tf*idf
		return posting_dict[tokens][i]*inverse_freq(tokens)
	else:
		return 0

#Now we will use everything we've calculated before, to calculate the Euclidian length
def euclid_length_docs():
	global euclid_len 
	for i in all_doc_dicts:
		length_tokens = 0
		for tokens in tokens_list_word:
			#Now calculating length of each token in the token list
			length_tokens  = length_tokens  + (weight(tokens,i)**2)
		#Now our Euclidean length which is obtained is square root of length we jsut calculated
		euclid_len[i] = math.sqrt(length_tokens )

#Now we'll pass the user query in our query() function to search the right term
def enter_query_user(query):
	#search_que= input("Enter your query: ")
	search_que= query
	if search_que== "":
		sys.exit()
	
	#while(search_que):
	search_que= remove_tags_query(search_que)
	search_que= list(filter(('p').__ne__, search_que))
	#print(search_que)
	match_query = []
	for terms in search_que:
		match_query.append(set(posting_dict[terms].keys()))
	#Now removing set() from match_query
	match_query = list(filter((set()).__ne__, match_query))
	#print(match_query)
	#Now intersecting the sub-match_queryes
	try:
		re_sub = reduce(set.intersection, [x for x in match_query])
	except:
		re_sub = 0
	scores_query = []
	if not re_sub:
		print("DOcument not found")
	else:
		for id in re_sub:
			cosine_similarity_score = 0
			for term in search_que:
				if term in tokens_list_word:
					cosine_similarity_score += inverse_freq(term)*weight(term,id)
			#print(euclid_len )
			cosine_similarity_score /=euclid_len[id]
			#print(cosine_similarity_score)
			scores_query.append([id, cosine_similarity_score])
		scores_query = list(map(tuple, scores_query))
		scores_query = sorted(scores_query, key=lambda tup: tup[1], reverse=True)
		#print(scores_query)
		#mapping the nested list into the list of tuples
		#scores_query = sorted(scores_query, reverse=True)
		#print(scores_query)
		print("Score: filename")
		get_res = []
		result_dict = {}
		for (x,rates) in scores_query:
			#print(str(rate)+": "+ all_doc_dicts[x])
			get_res.append(str(rates)+": "+ all_doc_dicts[x])
			result_dict[all_doc_dicts[x]] = rates
		#print(result_dict)
		new_resdict = {}
		for i in result_dict.keys():
			# j = i.replace('/', "\\")
			f= open('Pre_Processing/'+(i) , 'rt')
			c = 0
			k = ''
			for line in f:
				if(c==0):
					c=c+1
					k=line.replace('\n','')
			new_resdict[k]= result_dict[i]
		print(new_resdict)
		file_a = open(r'Pre_Processing/Saved_pickle_files/result_dict.pkl', 'wb')
		pickle.dump(new_resdict, file_a)
		file_a.close()
		# print(result_dict)

if __name__ == "__main__":
	main_func('admissions')