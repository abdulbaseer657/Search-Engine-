from html.parser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
from pre_processing import remove_Tags,to_Lower_case,filter_Stop_Words,stemmer_func
import urllib.request
import os
import re

class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text

def clean_data(text):
    # (REMOVE <SCRIPT> to </script> and variations)
    pattern = r'<[ ]*script.*?\/[ ]*script[ ]*>'  # mach any char zero or more times
    text = re.sub(pattern, '', text, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

    # (REMOVE HTML <STYLE> to </style> and variations)
    pattern = r'<[ ]*style.*?\/[ ]*style[ ]*>'  # mach any char zero or more times
    text = re.sub(pattern, '', text, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

    # (REMOVE HTML <META> to </meta> and variations)
    pattern = r'<[ ]*meta.*?>'  # mach any char zero or more times
    text = re.sub(pattern, '', text, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

    # (REMOVE HTML COMMENTS <!-- to --> and variations)
    pattern = r'<[ ]*!--.*?--[ ]*>'  # mach any char zero or more times
    text = re.sub(pattern, '', text, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

    # (REMOVE HTML DOCTYPE <!DOCTYPE html to > and variations)
    pattern = r'<[ ]*\![ ]*DOCTYPE.*?>'  # mach any char zero or more times
    text = re.sub(pattern, '', text, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

    return text

def get_url(file_name):
    xfile = file_name
    fln = open('new_docs/'+xfile, 'r')
    c=0
    for line in fln:
        if(c==0):
            c=c+1
            k=line.replace('\n','')
    url = k
    return url



def main():
    counter_value = 0
    directory = os.listdir('new_docs')
    if not os.path.exists('clean_docs'):
        os.makedirs('clean_docs')
    for file in directory:
        open_file = open('new_docs/'+file, 'r')
        read_file = open_file.read() 
        read_file = clean_data(read_file)
        read_file = dehtml(read_file)
        read_file = re.sub('\W+',' ', read_file )

        #Preprocess the text
        plain_text = remove_Tags(read_file)
        lowerCase = to_Lower_case(plain_text)
        filtered_words = filter_Stop_Words(lowerCase)
        #stem_list = stemmer_func(filtered_words)

        #Split the file to get filename and filetype
        base_path = os.path.splitext(file)[0]

        new_file_path = base_path + ".txt"
        url=get_url(new_file_path)
        write_file = open("clean_docs/"+new_file_path, 'w')
        write_file.write(url+"\n"+str(" ".join(filtered_words)))# ---- to store the file as " " separated list
        write_file.close()
        counter_value += 1
    print("Number of files ", counter_value)


if __name__ == "__main__":
    main()




















        
		
		
		
		
		


		
		



	
	
		