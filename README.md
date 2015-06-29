# Flask/Heroku/Mongo Example App

A barebones Python app which can easily be deployed to Heroku. This app uses the Flask framework, MongoDB as the database engine, and includes basic sample functionality for both of those services.

Live demo: [https://ancient-garden-9052.herokuapp.com/](https://ancient-garden-9052.herokuapp.com/)

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone https://github.com/patrickcgray/flask_heroku_example.git
$ cd flask-heroku-example
$ pip install -r requirements.txt
$ # make sure that mongo is installed and then running by running the mongod command
$ python main/main.py
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku
#### To function properly on heroku you will need to add [MongoLab](https://mongolab.com/) on your Heroku Dashboard

```sh
$ heroku create
$ git push heroku master
$ heroku open
```

## Tech Stack
-Heroku

-Python

-Flask

-Mongodb

## Code Structure:
	Procfile
		-this file has the command to have heroku run the python app
	requirements.txt
		-python packages in use. this is used by heroku to build the environment
	main/
  	    main.py
  	    	-all logic and functionality
  	    static/
  	    	-contains CSS and other static files
  	    templates/
  	    	-contains the HTML templates used to display by main.py
