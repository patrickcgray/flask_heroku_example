'''
Created on June 27, 2015

@author: pgray
'''

######################################################
################# initial setup ######################
######################################################

from flask import Flask, redirect, render_template, request
from flask.ext.pymongo import PyMongo
from flask.ext.pymongo import ObjectId 
from datetime import datetime

from jinja2 import Environment, PackageLoader

import json, subprocess, os, copy

MONGO_URL = os.environ.get('MONGOLAB_URI')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/resume_app";

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask(__name__, template_folder=tmpl_dir, static_folder='static')

app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app)

######################################################
################# functions and db work ##############
######################################################

######################################################
################# web app routes #####################
######################################################

@app.route('/', methods=['GET'])
def main():
	if request.method == "GET":
		submission_success = request.args.get('submission')
		if submission_success == 'true':
			submission_success = True
		else:
			submission_success = False

		return render_template('main.html', submission_success=submission_success)
	else:
		pass

@app.route('/add_resume', methods=['GET', 'POST'])
def add_resume():
	if request.method == "GET":
		return render_template('add_resume.html')
	elif request.method == "POST":
		email = request.form['email']
		resume_text = request.form['resume']
		name = request.form['name']
		#chapter = request.form['chapter']

		mongo.db.resumes.insert(
				{
					"email" : email,
					"name" : name,
					"resume_text" : resume_text,
					"time_created" : datetime.now(),
				})

		return redirect('/?submission=true')
	else:
		pass

@app.route('/resume_page/<entry_id>', methods=['GET'])
def resume_page(entry_id):
	if request.method == "GET":

		result = mongo.db.resumes.find_one({"_id" : ObjectId(entry_id)})
		print("ya this is the result")
		print(entry_id)
		print(result)

		return render_template('resume_page.html', result=result)
	else:
		pass

@app.route('/search', methods=['GET', 'POST'])
def search():
	if request.method == "GET":
		keywords = request.args.get('keywords')
		result_list = []
		search_attempt = False

		if keywords:
			search_attempt = True
			keyword_list = keywords.split(",")
			final_keyword_list = []
			for word in keyword_list:
				final_keyword_list.append(word.rstrip().lstrip())
			keyword_string = " ".join(final_keyword_list)

			results = mongo.db.resumes.find({ "$text" : { "$search" : keyword_string } })

			for result in results:
				result_list.append(result)

		else:
			pass

		return render_template('search.html', result_list=result_list, search_attempt=search_attempt)
	else:
		pass

    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    with app.app_context():
    	mongo.db.resumes.ensure_index( [ ("resume_text" , "text") ] )
    app.run(host='0.0.0.0', port=port)

