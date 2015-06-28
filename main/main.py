'''
Created on June 27, 2015

@author: pgray
'''

######################################################
################ required imports ####################
######################################################

from flask import Flask, redirect, render_template, request
from flask.ext.pymongo import PyMongo
from flask.ext.pymongo import ObjectId 
from datetime import datetime
import json, subprocess, os, copy

from jinja2 import Environment, PackageLoader

######################################################
################# flask/mongo config #################
######################################################

# setting up the mongo environment to use the heroku MONGOLAB_URI environment variable or the local URL
MONGO_URL = os.environ.get('MONGOLAB_URI')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/vehicles";

# setting up the template directory
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask(__name__, template_folder=tmpl_dir, static_folder='static')

# configuring the mongo database with flask app
app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app)

######################################################
################# web app routes #####################
######################################################

# for more information on Flask routing go to http://flask.pocoo.org/docs/0.10/quickstart/#routing
@app.route('/', methods=['GET'])
def main():
	if request.method == "GET":
		submission_success = request.args.get('submission')
		return render_template('main.html', submission_success=submission_success)

@app.route('/add_motorcycle', methods=['GET', 'POST'])
def add_resume():
	if request.method == "GET":
		error = request.args.get('error')
		if error == 'true':
			error = True
		else:
			error = False
		return render_template('add_motorcycle.html', error=error)
	elif request.method == "POST":
		name = request.form['name']
		make = request.form['make']
		model = request.form['model']
		top_speed = request.form['top_speed']

		if not name or not make or not model or not top_speed:
			return redirect('/add_motorcycle?error=true')

		mongo.db.motorcycles.insert(
				{
					"name" : name,
					"make" : make,
					"model" : model,
					"top_speed" : top_speed,
					"time_created" : datetime.now(),
				})

		return redirect('/?submission=true')
	else:
		pass

@app.route('/list', methods=['GET', 'POST'])
def list():
	if request.method == "GET":
		results = mongo.db.motorcycles.find()
		result_list = []

		#iterating through results cursor and putting them into a python list
		for result in results:
			result_list.append(result)

		return render_template('list.html', result_list=result_list)
	else:
		pass

@app.route('/search', methods=['GET', 'POST'])
def search():
	if request.method == "GET":
		make = request.args.get('make')
		result_list = []
		search_attempt = False

		if make:
			search_attempt = True
			results = mongo.db.motorcycles.find({ "make" : make })

			#iterating through results cursor and putting them into a python list
			for result in results:
				result_list.append(result)
		else:
			pass
		return render_template('search.html', result_list=result_list, search_attempt=search_attempt)
	else:
		pass


#	instantiating the app
if __name__ == "__main__":
	# must run on the heroku designated port, or if there is no env variable it will run on port 5000 
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)

