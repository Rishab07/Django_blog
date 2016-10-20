from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.posts_list,name="home"),
	#url(r'^list/$',views.posts_list,name="home"),
	url(r'^(?P<id>\d+)/details/$',views.posts_detail,name="detail"),
]