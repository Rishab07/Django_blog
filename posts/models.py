from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

def upload_location(instance,filename):
	return "%s/%s" %(instance.id,filename)



class Post(models.Model):
	title = models.CharField(max_length=56)
	content = models.TextField()
	tips_type = models.CharField(max_length=100)
	author = models.CharField(max_length=120)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	image = models.ImageField(upload_to=upload_location ,
		null=True,blank=True)


	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id":self.id})

	class Meta:
		ordering = ["-timestamp"]



