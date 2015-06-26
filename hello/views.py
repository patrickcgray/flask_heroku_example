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
		resume_text = "My interest was piqued when my good friend Hannah Kerner - who I worked with through undergraduate studies and SEDS-USA ? sent me the summary for the Director of Lunar Programs role. I read all I could find about the position and WayPaver Labs in general. I?m fascinated by your ambitious mission, would love to learn more, and think that WayPaver can make a major difference. I also think that my skills, experience, and connections uniquely situaIn addition to my space systems software engineering role I travel frequently to speak at and attend space related events. At conferences nationally and around the Bay Area I often find myself explaining the burgeoning commercial space industry to others. I love my current work and I have been evangelizing Moon Express for over a year as well as organizing SEDS events around the country. But in the last couple months I realized that I would like to more fully utilize this latter set of skills. I want to combine my engineering background and my ability toMy resume articulates the bulk of my experience but I would love to discuss, both here and in person, some of my personal projects and endeavors. They paint a more complete portrait of who I actually am and range technically from rebuilding old cars to developing an open source English teaching chatbot and range socially from hosting I think the space industry is on a major upward trend and that WayPaver Labs is poised to help foster and focus this growth. I also believe my skills and experience will significantly benefit the group.  I have worked on a broad range of technical projects, with significant experience in space systems. I have been a part of the core teams in startup accelerators in Brazil and North Carolina. I have strong ties to both the space industry and Silicon Valley. And I have experience running large-scale operations both in and out of the space industry. This combination will make me an effective member of the team, grounded on the technical end, and capable of quickly getting situated in the community and developing WayPaver?s Lunar Programs. I look forward to meeting more wonderfPatrick Grayready in the community and discussing further!"		
		final_resume = unicode(resume_text, "utf-8")
		logger.info('This is a simple log message ayyyyyyy')
		logger.info(final_resume)

		context = {'success': email}
		#need to add the file to the database
		r = Resume(email=email, resume_text=final_resume)
		#time.sleep(4)
		r.save()

		return render(request, 'insert_resume.html', context)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

