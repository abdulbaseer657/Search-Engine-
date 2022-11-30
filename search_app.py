
from flask import Flask, render_template, request
#import sys
import vectorizer_sp
import pickle
import jinja2

app = Flask(__name__)
app.jinja_env.globals.update(zip = zip)

@app.route('/')
def main_fun():
    return render_template("index_page.html")
	
@app.route('/result_page', methods=['GET', 'POST'])
def result_page():
	if request.method == 'POST':
		serach_data = request.form.get("query")
		print("This is the user value: ", serach_data )
		vectorizer_sp.main_func((serach_data ))
		file2 = open(r'Pre_Processing/Saved_pickle_files/result_dict.pkl', 'rb')
		results_dict = pickle.load(file2)
		file2.close()
		print(results_dict)
		results_dict= dict(sorted(results_dict.items(),key=lambda item: item[1],reverse=True))
		content = {'classes':list(results_dict.keys()),"percentage":list(results_dict.values())}
		return render_template("results.html", **content)
		
	
	
if __name__ == "__main__":
	app.run(debug=False)