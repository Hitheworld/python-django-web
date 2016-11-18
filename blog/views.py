from django.shortcuts import render
from django.http import HttpResponse
from models import PhoneModel

class Person(object):
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		selsf.sex = sex

	def say(self):
		return "I'm " + self.name

# Create your views here.
# def index(req):
# 	usre = {'name':'tom', 'age': 23, 'sex':'male'}
# 	book_list = ['python', 'java', 'php']
# 	return render(req, "index.html",{})

def index(req):
	entry = PhoneModel(name='lidong')
	entry.phone = '13410320008'
	entry.save()
	resp = "hello %s , phone :%s" % (entry.name, entry.phone)
	# return HttpResponse(resp)
	# return render(req, "index.html", {resp:resp})
	resp = simplejson.dumps(resp)
	return HttpResponse(resp)

