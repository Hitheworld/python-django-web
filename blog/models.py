#coding=utf-8
from __future__ import unicode_literals

# from django.db import models

from mongoengine import *
from news.settings import DBNAME

connect(DBNAME)


class PostModel(Document):
    title = StringField(max_length=120, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)



class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say(self):
        return "I'm " + self.name
