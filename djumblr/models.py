import datetime

from django.db import models
from django.contrib.auth.models import User

class Regular(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250, blank=True)
    body = models.TextField()
    
    pubdate = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-pubdate']
    
    def __unicode__(self):
        if self.title:
            return "%s (regular)" % self.title
        else:
            return "Regular"
        
    def get_absolute_url(self):
        return "/regular/%d" % self.id

class Photo(models.Model):
    id = models.IntegerField(primary_key=True)
    source = models.URLField(blank=True)
    photo = models.ImageField(upload_to="/photos", blank=True)
    caption = models.TextField(blank=True)
    click_through_url=models.URLField(blank=True)

    pubdate = models.DateTimeField()
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-pubdate']

    def __unicode__(self):
        return "Photo"

    def get_absolute_url(self):
        return "/photo/%d" % self.id
        
class Quote(models.Model):
    id = models.IntegerField(primary_key=True)
    quote = models.TextField()
    source = models.TextField(blank=True)

    pubdate = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-pubdate']

    def __unicode__(self):
        return "Quote"

    def get_absolute_url(self):
        return "/quote/%d" % self.id


class Link(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500, blank=True)
    url = models.URLField()
    description = models.TextField(blank=True)

    pubdate = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-pubdate']
        
    def __unicode__(self):
        if self.name:
            return "%s (link)" % self.name
        else:
            return "Link"

    def get_absolute_url(self):
        return "/link/%d" % self.id

class Conversation(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=500, blank=True)
    conversation = models.TextField()

    pubdate = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-pubdate']

    def __unicode__(self):
        if self.title:
            return "%s (Conversation)" % self.title
        else:
            return "Conversation"

    def get_absolute_url(self):
        return "/conversation/%d" % self.id
        
class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    embed = models.TextField(blank=True)
    data = models.FileField(blank=True, upload_to='/videos')
    title = models.CharField(blank=True, max_length=250)
    caption = models.TextField(blank=True)

    pubdate = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-pubdate']        
    
    def __unicode__(self):
        return "Video"

    def get_absolute_url(self):
        return "/video/%d" % self.id

class Audio(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.FileField(upload_to='/audio')
    caption = models.TextField(blank=True)
    
    pubdate = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)