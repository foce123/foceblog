from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=16)
    def __unicode__(self):
        return self.name
 
class Tag(models.Model):
    name = models.CharField(max_length=16)
    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    email = models.EmailField(blank=True)
    def __unicode__(self):
        return u'%s' %(self.name)
 
class Blog(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True,serialize=False)
    title = models.CharField(max_length=32)
    author = models.ForeignKey(Author)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    def __unicode__(self):
        return u'%s' %(self.title)
 
class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    name = models.CharField(max_length=16)
    email = models.EmailField()
    content = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s' %(self.content)
