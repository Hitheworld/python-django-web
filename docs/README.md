django object

1、install python
2、django install 
3、django-admin startproject object[name]
4、django-admin startapp blog[appname]
5、edit settings.py
	app add --> blog
6、edit urls.py
	url(r'^blog/index/$', views.index, name='index')
7、edit blog/views.py
	from django.http import HttpResponse
	def index(req)：
		return HttpResponse('<h1>Hello World<h2>')
8、python manager.py runserver


MySql: 

mysqld --initialize-insecure
mysqld --console
mysql -uroot
set password=password('root');
mysql -uroot -proot

MySQLdb:
 	http://www.codegood.com/downloads


django:
	python manage.py migrate
	python manage.py createsuperuser

