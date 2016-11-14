from django.shortcuts import render
from django.http import HttpResponse

class Person(object):
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		selsf.sex = sex

	def say(self):
		return "I'm " + self.name

# Create your views here.
def index(req):
	usre = {'name':'tom', 'age': 23, 'sex':'male'}
	book_list = ['python', 'java', 'php']
	return render(req, "index.html",{})