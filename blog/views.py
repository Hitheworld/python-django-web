import json
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from models import PostModel



# Create your views here.
# def index(req):
# 	usre = {'name':'tom', 'age': 23, 'sex':'male'}
# 	book_list = ['python', 'java', 'php']
# 	return render(req, "index.html",{})


def index(req):
    if req.method == 'POST':
        # save new post
        title = req.POST['title']
        content = req.POST['content']

        entry = PostModel(title=title)
        entry.last_update = datetime.datetime.now()
        entry.content = content
        entry.save()

    # Get all posts from DB
    Posts = PostModel.objects
    return render(req, "index.html", {Posts:Posts})

	# resp = {}
	# JSONObject = {}
	# item = {}
	# items = [item]
	# resp['success'] = 'true'
	# resp['JSONObject'] = JSONObject
	# JSONObject['items'] = items
	# item['title'] = entry.title
	# item['content'] = entry.content
	# item['last_update'] = entry.last_update
	# return HttpResponse(json.dumps(resp), content_type="application/json")
	# return render(req, "index.html", {resp:resp})


def update(request):
    id = eval("request." + request.method + "['id']")
    post = PostModel.objects(id=id)[0]

    if request.method == 'POST':
        # update field values and save to mongo
        post.title = request.POST['title']
        post.last_update = datetime.datetime.now()
        post.content = request.POST['content']
        post.save()
        template = 'index.html'
        params = {'Posts': PostModel.objects}
    elif request.method == 'GET':
        template = 'update.html'
        params = {'post': post}
    return render(template, params)


def delete(request):
    id = eval("request." + request.method + "['id']")
    if request.method == 'POST':
        post = Post.objects(id=id)[0]
        post.delete()
        template = 'index.html'
        params = {'Posts': Post.objects}
    elif request.method == 'GET':
        template = 'delete.html'
        params = {'id': id}
    return render(template, params)