# encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.


class Poem(models.Model):
#class Poem(DynamicDocument):
#	meta = {
#		'collection':'poem_data',			
#	}
#	poem_id = SequenceField(required=True, primary_key=True)
#	author = StringField()
#	title = StringField()
	@queryset_manager
	def show_news(doc_cls, queryset):
		return queryset.order_by('-poem_id')
	poem_id = models.IntegerField()
	author = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
