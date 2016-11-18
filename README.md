###django object

1、install python
2、django install 
3、django-admin startproject object[name]
4、django-admin startapp blog[appname]
5、edit settings.py
	app add --> blog
6、edit urls.py
	url(r'^blog/index/$', views.index, name='index')
7、edit blog/views.py
	<code>
	from django.http import HttpResponse<br />
	def index(req)：<br />
		return HttpResponse('\<h1\>Hello World\<h2\>')
	</code>
8、python manage.py runserver


MySql: 

mysqld --initialize-insecure
mysqld --console
mysql -uroot
set password=password('root');
mysql -uroot -proot

MySQLdb:
 	http://www.codegood.com/downloads

MySQLGUI:
    MySQL-Front


# Mongodb
sc.exe create MongoDB binPath= "D:\MongoDB\Server\3.2\bin\mongod.exe --service --config=\"D:\MongoDB\Server\3.2\mongodb.cfg\"" DisplayName= "MongoDB" start= "auto"
mongod --dbpath D:\MongoDB\data\db
mongod --config D:\MongoDB\mongo.config --install --serviceName "MongoDB"

django:
	python manage.py migrate
	python manage.py createsuperuser



