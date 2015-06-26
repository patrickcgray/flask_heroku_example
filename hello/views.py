import requests
import time
from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf

from .models import Greeting
from .models import Resume

import logging
logger = logging.getLogger('testlogger')


# Create your views here

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')

def insert_resume(request):
	if request.method == 'GET':
		context = {'success': 'no sire'}
		return render(request, 'insert_resume.html', context)

	elif request.method == 'POST':
		email = request.POST.get("email", "")
		#resume_text = request.POST.get("resume", "")

		this_file = request.FILES['resume']
		logger.info(this_file.name)           # Gives name
		logger.info(this_file.content_type)   # Gives Content type text/html etc
		logger.info(this_file.size)           # Gives file's size in byte
		#resume_text = this_file.read()         # Reads file
		#resume_text = "yoooo this is an awesome resume!!!"
		resume_text = "My interest was piqued when my good friend Hannah Kerner - who I worked with through undergraduate studies and SEDS-USA ? sent me the summary for the Director of Lunar Programs role. I read all I could find about the position and WayPaver Labs in general. I?m fascinated by your ambitious mission, would love to learn more, and think that WayPaver can make a major difference. I also think that my skills, experience, and connections uniquely situaIn addition to my space systems software engineering role I travel frequently to speak at and attend space related events. At conferences nationally and around the Bay Area I often find myself explaining the burgeoning commercial space industry to others. I love my current work and I have been evangelizing Moon Express for over a year as well as organizing SEDS events around the country."
		logger.info('This is a simple log message ayyyyyyy')
		logger.info(resume_text)

		context = {'success': email}
		#need to add the file to the database
		r = Resume(email=email, resume_text=resume_text)
		time.sleep(4)
		r.save()

		return render(request, 'insert_resume.html', context)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

