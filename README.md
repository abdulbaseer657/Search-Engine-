# Search-Engine-
SEARCH ENGINE 
 Mohammed Abdul Baseer
University of Kansas, Lawrence.

ABSTRACT:
This project describes the implementation of a search engine from scratch and the different modules involved with it. There are hundreds of web pages in the KU domain. Each webpage has its purpose. It would be very difficult to browse each page and find the one that the user is looking for his/her needs. This search engine helps users in finding the webpage of their needs. In this project, the KU domain can be searched using any search keywords. We have implemented a crawler to crawl the webpage for the domain (i.e., KU). Apart from the crawler, we have other module vector space models for calculating the similarity of the documents. Document preprocessing and an inverted index for removing HTML tags, converting upper to lower case, removing stop words, and so on. Relevance feedback and term proximity modules are in the testing phase where we have operational code for both modules yet to be merged with the remaining modules.

I INTRODUCTION:
Search engines started in the ’90s and it’s one of the most interesting topics to learn and research what’s behind it. Information retrieval (IR) starts with the query which was given by the user. In IR query is not defined uniquely and instead of matching to the exact result, it may match to multiple documents based on relevancy. Information needs to be taken from a database. The key difference between IR and database is ranking.
The main idea of a search engine is to give us a fast and simple way to find the required information of user interest. The entire process of a search engine is carried out with the model of crawling and indexing, and ranking. To improve the user experience, we need to use efficient algorithms which give us relevant and high-quality results.







II.ARCHITECHTURE OF OUR SEARCH ENGINE
The basic architecture of the search engine is shown in the figure below. Generally, we scrape the website to get the information or data which is the initial step. We have chosen From the KU domain for the project so from where we will scrape and fetch the data which will be useful for further processing i.e., for crawling.
In the crawling phase, the crawler visits the URLs which are listed to be visited these are referred to as seeds. After which it communicates with the server and identifies the hyperlinks which need to be retrieved from the webpages and them to list or queue this is called URL frontier.
Once after retrieved the crawled documents, we will follow the steps listed in Figure1. i.e., further, we will perform document pre-processing and further we perform index inversion, we then use the vector space model (VSM) for similarity and page ranking to results in the web interface.
When a user is given a query from the web interface the results or output is obtained based on the similarity which is shown in the results screenshots.
 



 

Figure1: Image source: “The image used in the documentation is taken from the presentation PPT demonstrated in the class”
III PROGRAMMING LANGUAGES AND FRAMEWORK
•	Framework: Flask
•	Programming language: CSS, HTML, Python
•	Domain: ku.edu
IV WEB CRAWLER
Web crawler helps us browse all the web pages in the KU domain based on the search key. The relevant pages are searched for, and the results are put into a queue.
In this project, there are two text files queue.txt and crawled.txt all the relevant links are initially put into queue.txt, and whatever the pages that have been crawled are put into crawled.txt this process helps the engine to keep track of the pages that have already been crawled and the ones that are yet to be crawled.
The functionality of HTML Parser is that retrieved URLs are converted to absolute URLs which helps to find the required resource. The next step is to remove the unnecessary URL links.
Finally, the spider component will have crawled URLs which are saved in the crawled.txt file. The URLs will be in the queue and added to the waiting list for further processing.



 
Figure2: Image source: “The image used in the documentation is taken from the presentation PPT demonstrated in the class”

V DOCUMENT PREPROCESSING AND INV 	ERTED INDEX
 Of the many pages in the search domain retrieving the selected few results based on the search keyword, it could be time taking and tedious process. Ordering all the pages based on the dictionary and posting list would significantly bring down the search time. The inverted index is a database index that stores any mapping from content, such as text or number, to its locations in a table or inset of documents. Inverted index calculation is based on DF (document frequency) and TF (term frequency).
In the query preprocessing below are the steps 
•	Removal of HTML tags.
•	Tokenization
•	Upper to lower case conversion
•	Removal of stop words
We have used the NLTK package and Porter stemmer.
VI VECTOR SPACE MODEL
Below are the steps and processes used for the implementation of the vector space model.
•	Collecting word list 
•	Collecting dictionary structure 
•	Collecting all keys 
•	Calculate document frequency and inverse document frequency
•	Calculate Euclidean distance
Our vector space model calculates the similarity of the documents with the help of input search keywords.


 
Image source: “The image used in the documentation is taken from the presentation PPT demonstrated in the class”

VII RESULTS
Below are the screenshots of the results. The search engine runs on default port 5000 when we run the search app python file the URL for the search engine is displayed in the logs. Browsing the URL, we can see the active search engine with a text box and search button. When a user enters any keyword and hits the search button or enter, the search engine retrieves all the related URLs in the Ku domain based on cosine similarity and users can navigate any of the webpages of their choice.
 
 
Image source: “The image used in the documentation is taken from the presentation PPT demonstrated in the class”

VIII RELEVANCE FEEDBACK 
We have tried to implement the Relevance feedback in the next version of the search engine. The main idea to implement this module is to improve the result. Generally, we consider the results from initial search results obtained from the user query, to know the user feedback and use the information is required or not in the next new query.

The general technique or method is Rocchio Algorithm, below is the formula to calculate 
 

“Image source: From the class slides concept relevance feedback”

IX FUTURE WORK
We have individual operational codes for relevance feedback and term proximity and would like to merge them into our search engine which is the future scope. We would like to improve the UI part of the website.

REFERENCES
[1] Class lecture slides
[2] Images - project PPT.
[3] Introduction to Information Retrieval , by Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze, Cambridge University Press. 2008.
[4] https://en.wikipedia.org/wiki/Web_crawler














Project log or contributions:
We have planned the regular meetings on Tuesday and Thursday which is online and offline where everyone contributed equally. We have shared the ideas for the modules.


