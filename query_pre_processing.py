import os
import re
import string
from lxml import html
from lxml.html.clean import clean_html
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

TAG_RE_Pattern = re.compile(r'<[^>]+>')

#To remove the stop words
stop_words = set(stopwords.words('english'))

def puns(ch):
    if ch.isalpha():
        return ch
    else:
        return ' '

def remov_duplicates(input):
	#split input string separated by space
	input = input.split(" ")
	#joins two adjacent elements in iterable way
	for i in range(0, len(input)):
		input[i] = "".join(input[i])
	# now create dictionary using counter method which will have strings as key and their frequencies as value
	UniqW = Counter(input)
	#joins two adjacent elements in an iterable way
	s = " ".join(UniqW.keys())
	return s

def remove_tags_query(read_file_query):
	read_file_query = clean_html(read_file_query)
	read_file_query = ''.join(puns(ch)for ch in read_file_query)
	read_file_query = ' '.join(read_file_query.split())
	remove_tags_var = TAG_RE_Pattern.sub('', read_file_query)
	remove_tags_var = re.sub('<script>.*?</script>', '', remove_tags_var)
	lower_var = read_file_query.lower()
	lower_var = remov_duplicates(lower_var)
	words_tokens = word_tokenize(lower_var)
	filt_sentence = [w for w in words_tokens if not w in stop_words]
	filt_sentence = []
	for w in words_tokens:
		if w not in stop_words:
			filt_sentence.append(w)
	#print(filt_sentence)
	return filt_sentence