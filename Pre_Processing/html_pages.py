import os
import urllib.request
import re
# importing the modules
import requests
#import main


def html_pages_crawl():
            # Download a webpage.
            #seed_url = 'https://ku.edu'
            hearders = {'headers':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}

            if not os.path.exists('new_docs'):
                os.makedirs('new_docs')

            file1 = open("web_crawler/crawled.txt","r")
            urls_list = file1.readlines()
            #print(urls_list[3])
            #print(len(urls_list))

            for i in range(1,len(urls_list)+1):
                try:
                    seed_url = urls_list[i].strip()
                    n = requests.get(seed_url, headers=hearders)
                    al = n.text
                    file_title = al[al.find('<title>') + 7 : al.find('</title>')]
                    #file_title = file_title.replace(" ","_")
                    file_title = re.sub('[^A-Za-z0-9]+', '', file_title)
                    print(file_title)

                    # Identify ourselves to be polite.
                    request = urllib.request.Request(seed_url)
                    request.add_header("Mohammed Abdul", "Mini Search Engine Project")
                    opener = urllib.request.build_opener()
                    response = opener.open(request)
                    html = response.read()

                    # Save the content to files that are named after the URL.
                    f = open('new_docs/{}.txt'.format(file_title), 'w+')
                    f.write(seed_url+"\n"+str(html))
                    f.write(html)
                    # seed_url+"\n"
                    f.close()
                except:
                    print("Page_Error")


if __name__ == "__main__":
    html_pages_crawl()


