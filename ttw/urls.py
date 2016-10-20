from django.conf.urls import url,include
from django.contrib import admin
from posts.views import posts_detail,about

urlpatterns = [
	#url(r'^$',"posts.views.posts_list"),
	#url(r'^know_us/$',about,name="know_us"),
    url(r'^admin/', admin.site.urls),
    url(r'^',include("posts.urls",namespace="posts")),
]


