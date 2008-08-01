import datetime

from django.db import models
from django.contrib.auth.models import User

class Regular(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250, blank=True)
    body = models.TextField()
    
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-pub_date']
    
    def __unicode__(self):
        if self.title:
            return "%s (regular)" % self.title
        else:
            return "Regular"
        
    def get_absolute_url(self):
        return ('djumblr_regular_detail', (), { 'year': self.pub_date.strftime("%Y"),
                                                'month': self.pub_date.strftime("%b").lower(),
                                                'day': self.pub_date.strftime("%d"),
                                                'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)
    
class Photo(models.Model):
    id = models.IntegerField(primary_key=True)
    source = models.URLField(blank=True)
    photo = models.ImageField(upload_to="/photos", blank=True)
    caption = models.TextField(blank=True)
    click_through_url=models.URLField(blank=True)

    pub_date = models.DateTimeField()
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return "Photo"

    def get_absolute_url(self):
        return ('djumblr_photo_detail', (), { 'year': self.pub_date.strftime("%Y"),
                                              'month': self.pub_date.strftime("%b").lower(),
                                              'day': self.pub_date.strftime("%d"),
                                              'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)
        
class Quote(models.Model):
    id = models.IntegerField(primary_key=True)
    quote = models.TextField()
    source = models.TextField(blank=True)

    pub_date = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return "Quote"

    def get_absolute_url(self):
        return ('djumblr_quote_detail', (), { 'year': self.pub_date.strftime("%Y"),
                                              'month': self.pub_date.strftime("%b").lower(),
                                              'day': self.pub_date.strftime("%d"),
                                              'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)

class Link(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500, blank=True)
    url = models.URLField()
    description = models.TextField(blank=True)

    pub_date = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-pub_date']
        
    def __unicode__(self):
        if self.name:
            return "%s (link)" % self.name
        else:
            return "Link"

    def get_absolute_url(self):
        return ('djumblr_link_detail', (), { 'year': self.pub_date.strftime("%Y"),
                                             'month': self.pub_date.strftime("%b").lower(),
                                             'day': self.pub_date.strftime("%d"),
                                             'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)

class Conversation(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=500, blank=True)
    conversation = models.TextField()

    pub_date = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        if self.title:
            return "%s (Conversation)" % self.title
        else:
            return "Conversation"


    def get_absolute_url(self):
        return ('djumblr_conversation_detail', (), { 'year': self.pub_date.strftime("%Y"),
                                                     'month': self.pub_date.strftime("%b").lower(),
                                                     'day': self.pub_date.strftime("%d"),
                                                     'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)
        
class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    embed = models.TextField(blank=True)
    data = models.FileField(blank=True, upload_to='/videos')
    title = models.CharField(blank=True, max_length=250)
    caption = models.TextField(blank=True)

    pub_date = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-pub_date']        
    
    def __unicode__(self):
        return "Video"

    def get_absolute_url(self):
        return ('djumblr_video_detail', (), { 'year': self.pub_date.strftime("%Y"),
                                              'month': self.pub_date.strftime("%b").lower(),
                                              'day': self.pub_date.strftime("%d"),
                                              'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)
    
class Audio(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.FileField(upload_to='/audio')
    caption = models.TextField(blank=True)
    
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-pub_date']        
    
    def __unicode__(self):
        return "Audio"

    def get_absolute_url(self):
        return ('djumblr_audio_detail', (), { 'year': self.pub_date.strftime("%Y"),
                                              'month': self.pub_date.strftime("%b").lower(),
                                              'day': self.pub_date.strftime("%d"),
                                              'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)