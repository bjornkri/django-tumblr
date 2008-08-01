import datetime
import urllib2

from BeautifulSoup import BeautifulStoneSoup
from django.conf import settings
from django.contrib.auth.models import User
from djumblr.models import Regular, Photo, Quote, Link, Conversation, Audio, Video, ConversationLine
from xml.sax.saxutils import unescape

def populate_models(tumblr_user, user):
    '''
    Takes a tumblr username (string), and a User model. Populates the tumblr models
    with data from 'tumblr_user'.tumblr.com, and associates the entries with 'user'.
    '''
    
    # feed_url = "http://%s.tumblr.com/read/api" % tumblr_user
    # xml = urllib2.urlopen(feed_url)
    xml = open('/Users/bjornk/development/testing/testin.xml')
    soup = BeautifulStoneSoup(xml)
    tumbls = soup.findAll('post')
    for tumbl in tumbls:
        # Common to all models
        id = tumbl['id']
        pub_date = datetime.datetime.fromtimestamp(float(tumbl['unix-timestamp']))
        
        # 'Regular' objects.
        if tumbl['type'] == "regular":
            if tumbl.find('regular-title'):
                title = tumbl.find('regular-title').contents[0]
            else:
                title = ""
            body = tumbl.find('regular-body').contents[0]
            m = Regular(id=id, pub_date=pub_date, user=user, title=title, body=unescape(body))
        
        # 'Photo' objects.
        elif tumbl['type'] == "photo":
            source = tumbl.findAll('photo-url')[1].contents[0]
            if tumbl.find('click-through-url'):
                click_through_url = tumbl.find('click-through-url').contents[0]
            if tumbl.find('photo-caption'):
                caption = tumbl.find('photo-caption').contents[0]
            else:
                caption = ""
            m = Photo(id=id, pub_date=pub_date, user=user, source=source, caption=unescape(caption))
        
        # 'Quote' objects.
        elif tumbl['type'] == "quote":
            quote = tumbl.find('quote-text').contents[0]
            if tumbl.find('quote-source'):
                source = tumbl.find('quote-source').contents[0]
            else:
                source = ""
            m = Quote(id=id, pub_date=pub_date, user=user, quote=unescape(quote), source=unescape(source))
            
        # 'Link' objects.
        elif tumbl['type'] == "link":
            if tumbl.find('link-text'):
                name = tumbl.find('link-text').contents[0]
            else:
                name = ""
            url = tumbl.find('link-url').contents[0]
            if tumbl.find('link-description'):
                description = tumbl.find('link-description').contents[0]
            else:
                description = ""
            m = Link(id=id, pub_date=pub_date, user=user, name=name, url=url, description=unescape(description))
        
        # 'Conversation' objects.
        elif tumbl['type'] == "conversation":
            if tumbl.find('conversation-title'):
                title = tumbl.find('conversation-title').contents[0]
            else:
                title = ""
            m = Conversation(id=id, pub_date=pub_date, user=user, title=title)
            m.save()
            
            lines = tumbl.find('conversation-text').contents[0].split('&#13;')
            for line in lines:
                c = ConversationLine(conversation=m, line=line)
                c.save()
            
            
        # 'Video' objects.
        elif tumbl['type'] == "video":
            embed = tumbl.find('video-player').contents[0]
            if tumbl.find('video-caption'):
                caption = tumbl.find('video-caption').contents[0]
            else:
                caption = ""
            m = Video(id=id, pub_date=pub_date, user=user, embed=unescape(embed), caption=unescape(caption))
        
        # 'Audio' objects.
        elif tumbl['type'] == "audio":
            embed = tumbl.find('audio-player').contents[0]
            if tumbl.find('audio-caption'):
                caption = tumbl.find('audio-caption').contents[0]
            else:
                caption = ""
            m = Audio(id=id, pub_date=pub_date, user=user, embed=unescape(embed), caption=unescape(caption))
            
        # TODO: Raise error.
        else:
            print "ERROR!", tumbl
            return ''
        
        m.save()

def populate_all():
    '''
    Loops through all the users defined in TUMBLR_USERS in the main settings file.
    
    TUMBLR_USERS should be a list of dictionaries, each containing a 'tumblr_user' and
    a 'local_user' key. 'tumblr_user' should be a tumblr user name, and 'local_user'
    the exact username of a user.
    
    Example:
    John has the username 'john' on his django website, but 'ignorantcarrot' on tumblr.
    His TUMBLR_USERS would be:

    TUMBLR_USERS = [{ 'tumblr_user': 'ignorantcarrot',
                      'local_user': 'john' }, ]

    '''
    
    for tumblr_user in settings.TUMBLR_USERS:
        user = User.objects.get(username__exact=tumblr_user['local_user'])
        
        populate_models(tumblr_user['tumblr_user'], user)
        
if __name__ == "__main__":
    populate_all()