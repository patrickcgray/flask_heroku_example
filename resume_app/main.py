'''
Created on June 27, 2015

@author: pgray
'''

######################################################
################# initial setup ######################
######################################################

from flask import Flask, redirect, render_template, request
from flask.ext.pymongo import PyMongo
from datetime import datetime

from jinja2 import Environment, PackageLoader

import json, subprocess, os, copy

MONGO_URL = os.environ.get('MONGOLAB_URI')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/resume_app";

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask(__name__, template_folder=tmpl_dir)

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
		return render_template('main.html')
		#return "Hello, World!"
	else:
		pass

    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
    

