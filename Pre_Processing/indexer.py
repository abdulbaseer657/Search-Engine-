
import os
from collections import defaultdict
import pickle

#path,dir and files.
#Default path given is clean_docs - YOu can change it to your appropriate directory.
##path, dirs, files = next(os.walk("./clean_docs"))
#print(files) - prints a list of documents like - [doc1, doc2]
#print(dir) - prints - <built-in function dir> - reason - why not? :-p
#print(path) - prints - ./cleaned_docs

#Empty list, to store keys_pf
##keys_pf = []

#Now, keys_pf for each documnet, in short, counting how many documnets are there.
#for i in range(0, len(files)):
#	keys_pf.append(i)
	#print(keys_pf) - print all the keys_pf for example - [0,1,2,3,4] - If there are five documents

#Empty dictionary_pf, just like keys_pf - used to store the list of files from 0 to n
#all_docs_pf = {}

#Now creating a dictionary_pf structure using above empty dictionary_pf
#for i in range(0, len(files)):
#	(k,v)=(keys_pf[i], "./clean_docs/"+files[i])
#	all_docs_pf[k] = v
	#print(v) - prints list of all the files

#Setting a dictionary_pf - It contains all of the words in total number of documents
#dictionary_pf = set()
#print(dictionary_pf) - prints set()

#This is to store number of postings_pf
#postings_pf = {}
#postings_pf = defaultdict(dict)
#print(postings_pf) - prints - defaultdict(<class 'dict'>, {})

dictionary_pf = set()
#dictionary_pf = set()
postings_pf = {}
postings_pf = defaultdict(dict)

def main():
	path, dirs, files = next(os.walk("clean_docs/"))
	keys_pf = []
	for i in range(0, len(files)):
		keys_pf.append(i)
	all_docs_pf = {}

	for i in range(0, len(files)):
		(k,v)=(keys_pf[i], "clean_docs/"+files[i])
		all_docs_pf[k] = v
	print("Nothing")
	assign_dict(all_docs_pf)
	if not os.path.exists('Saved_pickle_files'):
		os.makedirs('Saved_pickle_files')          
	file_a = open(r'Saved_pickle_files/dict.pkl', 'wb')
	pickle.dump(dictionary_pf, file_a)
	file_a.close()
	# print(dictionary_pf)

	#Store postings_pf in pickle file
	file_b = open(r"Saved_pickle_files/postings_pf.pkl", "wb")
	pickle.dump(postings_pf, file_b)
	file_b.close()
	#print(postings_pf)
	
	#Store list of docs in pickle file
	file_c= open(r"Saved_pickle_files/all_docs_pf.pkl", "wb")
	pickle.dump(all_docs_pf, file_c)
	file_c.close()
	#print(all_docs_pf)
	
	#Store the keys_pf in pickle file
	file_d = open(r"Saved_pickle_files/keys_pf.pkl", "wb")
	pickle.dump(keys_pf, file_d)
	file_d.close()
	#print(keys_pf)

def assign_dict(all_docs_pf):
	global dictionary_pf, postings_pf
	for id_doc in all_docs_pf:
		#Opening the pickle file
		#print(all_docs_pf[id_doc])
		f = open(all_docs_pf[id_doc], 'r', encoding="utf8")
		doc_whole = f.read()
		#print(doc_whole)
		f.close()
		doc_whole = doc_whole.split()
		#Set creates a set of tokens in the documents
		unique_terms_doc = set(doc_whole)
		#print(unique_terms_doc)
		#So, in the previous created dictionary_pf, I'm adding all these terms
		dictionary_pf = dictionary_pf.union(unique_terms_doc)
		#print(dictionary_pf)
		# Now we'll set the postings_pf, with the values equal to the frequency of terms in the document
		for terms in unique_terms_doc:
			postings_pf[terms][id_doc] = doc_whole.count(terms)
