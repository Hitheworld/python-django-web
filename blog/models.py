from __future__ import unicode_literals

# from django.db import models

from mongoengine import *

connect('test')


class PhoneModel(Document):
    name = StringField(required=True)
    phone = StringField(max_length=50)