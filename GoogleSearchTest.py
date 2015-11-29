# Testing the google search feature from the json thing
# https://www.youtube.com/watch?v=B5ksIcvsMwE
#
# This is a JSON tool used to search on google
# Tutorial for how to use it:   https://www.youtube.com/watch?v=B5ksIcvsMwE
# http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=

import urllib
import urllib2
import json

# This is used to remove the potential HTML tags that'll be part of the
# result's title
#FOUND ON:  http://stackoverflow.com/a/9662410
def remove_tags(text):
    return ''.join(ET.fromstring(text).itertext())


artist = ['Kendrick Lamar','DJ Premier','Kanye']

exSearch = 'Snoop Dogg playlist site:youtube.com'
encoded = urllib.quote(exSearch)

print encoded

abc = 'https://www.youtube.com/playlist%3Flist%3DPL129176707124BE53'
print
print abc
hello = urllib.unquote(abc)

print hello

rawData = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + encoded).read()

jsonData = json.loads(rawData)
searchResults = jsonData['responseData']['results']

topURLResult = searchResults[0]['url']
topTITLEResult = searchResults[2]['title']
print topURLResult
print topTITLEResult
#topTITLE = remove_tags(topTITLEResult)
print topTITLEResult
print

topResult = [topURLResult, topTITLEResult]
print topResult[1]
print

cmString = "Artist |" + artist[0] + "\n-|-" + \
           "\n |[top video](" + topURLResult + ")" + \
           "\n |[wiki page](" + topURLResult + ")"
print cmString

