'''
Created on June 27, 2015

@author: pgray
'''

######################################################
################# initial setup ######################
######################################################

from flask import Flask, redirect, render_template, request
from flask_pymongo import PyMongo
from datetime import datetime

from jinja2 import Environment, PackageLoader

import json, subprocess, os, copy

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/resume_app";

app = Flask(__name__)

app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app)

env = Environment(loader=PackageLoader('resume_app', 'templates'))

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
	else:
		pass

    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    

