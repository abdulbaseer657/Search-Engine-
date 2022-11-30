# Install Natural Language Toolkit (NLTK) using the following command:
# run sudo pip install -U nltk

# Download NLTK stopwords
# nltk.download('stopwords')

# Support for regular expressions.
import re

# Implementing a stop list and stemmer.
from nltk.stem import *
from nltk.stem.porter import *
from nltk.corpus import stopwords
#import nltk

import os

# Pre-process the documents by removing all HTML tags and convert everything
# into lower case.

def remove_Tags(html):
    remove_tags = re.compile('<.*?>')
    plain = re.sub(remove_tags, '', html)
    return plain

def to_Lower_case(text_data):
    return text_data.lower()

# Implement a stop list and a stemmer to pre-process the documents (for the stop
# list and stemmer, you are allowed to use third-party open source code).

def filter_Stop_Words(text):
	stopWords_set = set(stopwords.words('english'))
	filtered_words =  [i for i in text.split() if i not in stopWords_set]
	return filtered_words

def stemmer_func(text):
    stemmer_value = PorterStemmer()
    stem_list = []
    for words in text:
        stem_list.append(stemmer_value.stem(words))
    return stem_list

# Build an inverted index (including dictionary and posting lists) for the
# documents. Please make sure to keep all the frequency information.

# def invertedIndex(documents):
#
#     return index

def main():

	counter_value = 0
	directory = os.listdir('new_docs')
	if not os.path.exists('clean_docs'):
		os.makedirs('clean_docs')

	for file in directory:
		open_file = open('new_docs/'+file, 'r', encoding="utf8")
		read_file = open_file.read()

		plain_text = remove_Tags(read_file)
		lowerCase = to_Lower_case(plain_text)
		filtered_words = filter_Stop_Words(lowerCase)
		stem_list = stemmer_func(filtered_words)
		#Split the file to get filename and filetype
		base_path = os.path.splitext(file)[0]
		new_file_path = base_path + ".txt"
		write_file = open("clean_docs/"+new_file_path, 'w', encoding='utf-8')
		write_file.write(" ".join(stem_list))# ---- to store the file as " " separated list
		write_file.close()
		counter_value += 1
	print("Number of files ", counter_value)

if __name__ == "__main__":
    main()

