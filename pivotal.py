# -*- coding: utf-8 -*-
import urllib
import urllib2
import xmltodict


class Pivotal:

    def __init__(self):
        PROJECT_ID = '11111'
        self.TOKEN = 'my_pivotal_token'
        self.BASE_URL = 'http://www.pivotaltracker.com/services/v3/projects/%s/stories' % PROJECT_ID

    def request(self, data=None):
        url = self.BASE_URL
        if(data):
            url += '?' + urllib.urlencode(data)
        print url
        req = urllib2.Request(url, None, {'X-TrackerToken': self.TOKEN})
        res = urllib2.urlopen(req)
        return res.read()

    def getStories(self, data):
        stories_xml = self.request(data)
        # print stories_xml
        stories = xmltodict.parse(stories_xml)
        print 'Stories: %s' % stories['stories']['@count']
        if(int(stories['stories']['@count']) == 1):
            return [stories['stories']['story']]
        else:
            return stories['stories']['story']
        # return self.request(filters)
