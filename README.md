# Flask/Heroku/Mongo Example App

A barebones Python app using the Flask framework, which can easily be deployed to Heroku.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone https://github.com/patrickcgray/flask_heroku_example.git
$ cd flask-heroku-example
$ pip install -r requirements.txt
$ # make sure that mongo is running by running the mongod command
$ python main/main.py
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku
#### To function properly on heroku you will need to add [MongoLab](https://mongolab.com/)

```sh
$ heroku create
$ git push heroku master
$ heroku open
```

## Tech Stack
Heroku

Python

Flask

Mongodb

## How to Collaborate
get the heroku toolbelt

pull the project

## Code Structure:
	requirements.txt
		-python packages in use. this is used by heroku to build the environment
	main/
  	main.py
  		-all logic and functionality
  	static/
  		-contains CSS and other static files
  	templates/
  		-contains the HTML templates used to display by main.py
	

## Current Functionality
-user can submit a motorcycle

-user can search for motorcycle by make

-user can view a list of all current motorcycle entries
