# Gustavo Andres Murcia
#   GAM0929@gmail.com
#   gmurcia@uwo.ca

# 2015.11.29

#NOTES:
#   http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=
# this is the json thing for searching

# Musician Bot
# Will read reddit comments on certain subreddits and spit out info
# on the artist mentioned:
#   wikipedia (discography)
#   youtube link to the top playlist
#
#- As of now, the bot will only search for West Coast Rappers. To increase the artist list,
#  the text file read must be expanded. <-- Future development
#- As of now, the bot will only match to comments that exactly match the artist name, it does not parse
#  the comments for a mention of the artist
#       for example:    "I love Snoop Dogg" <-- does not 'match' the textfile, so the bot wont reply

# Import
import praw     # The wrapper for the Reddit API, source: https://praw.readthedocs.org/en/stable/
import urllib   # Used for the searhc functionality
import json     # Used for the search functionality, this analyzes the json object with it's various fields


# Functions 

# dataSearch will look for the keyword inside the database file inside the folder - in this case, west coast rappers.
#   returns a boolean value if the certain artist was found inside the textfile
def dataSearch( keyword ):
    filename = "WestCoastHipHop.txt"
    inFile = open (filename,"r")
    line = inFile.readline().rstrip("\n")
    
    cLetter = ord(keyword[0])-64 #This will only work when the keyword starts with a letter. <-- add numeric artist names in the future
    i = 0
    found = False
    # 2d Array, elements with each
    while line != "":
        #Get the category 
        category = line.split(":")
        line = inFile.readline().rstrip("\n")

        info = category[1].split(" #")
        info[0] = category[0]
        if (cLetter == i):
            #Go through the array info and look for the element
            for j in range(0, len(info)):
                elem = info[j]
                if (elem == keyword):
                    found = True
        
        i = i + 1
        
    return found; 

# youtubeSearch will search youtube for the artist passed as a parameter
#   returns the link to the top result when searching for their playlist
def youtubeSearch( keyword ):
    exSearch = keyword + ' playlist site:youtube.com'
    encoded = urllib.quote(exSearch)

    rawData = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + encoded).read()

    jsonData = json.loads(rawData)
    searchResults = jsonData['responseData']['results']

    # We want to get the top result from the query.
    # this way we can display the most popular videos
    ytURL = searchResults[0]['url']

    ytURL = urllib.unquote(ytURL)
    return ytURL; #change this so that it returns a list with the title of the link and also the url

# wikiSearch will search wikipedia for the artist passed as a paramater
# returns the link to the wiki article (does not check if it exists)
def wikiSearch( keyword ):
    exSearch = keyword + ' site:wikipedia.org'
    encoded = urllib.quote(exSearch)

    rawData = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + encoded).read()

    jsonData = json.loads(rawData)
    searchResults = jsonData['responseData']['results']

    # We want to get the top result from the query.
    # this way we can display the most popular videos
    wikiURL = searchResults[0]['url']
    wikiURL = urllib.unquote(wikiURL)

    return wikiURL;


## Main program
    
r = praw.Reddit(user_agent='Music Artist Information by /u/Gustavo0929')
r.login('MusicInformation','214146') # This is the account information for the bot's reddit account

# The following was done with the help of the praw tutorial:
#   https://praw.readthedocs.org/en/stable/pages/comment_parsing.html
#
# Comment Replier
# This Section will read the comments from either a specific post, or a multi-reddit
#       NOTE: If you want to do the multireddit analysis, see the comment bellow with MULTI REDDIT above it

r = praw.Reddit('MusicInformation service by /u/Gustavo0929')
r.login('MusicInformation', '214146')

# The following ID (3uogoc) comes from the following url:
#       https://www.reddit.com/r/test/comments/3uogoc/hack_western_info_test_3/
# The id should be changed to analyze the comments of any id, by finding it in the following format
#       https://www.reddit.com/r/SUB_REDDIT_NAME/comments/GET_THE_ID_HERE/NAME_OF_THE_POST
submission = r.get_submission(submission_id='3uogoc')
flat_comments = praw.helpers.flatten_tree(submission.comments)

# MULTI REDDIT
# The Following will be used to analyze the comments from the multireddits of music related things
# By using these comments, we can get the comments of a larger base of people.
#       multiReddits = r.get_comments('music+hiphopheads+listentothis')

already_done = set()
for comment in flat_comments:
    if dataSearch(comment.body) and comment.id not in already_done:
        ytURL = youtubeSearch(comment.body)
        wikiURL = wikiSearch(comment.body)
        
        commentString = "|" + comment.body + "\n-|-" + \
           "\n |[Top YouTube Playlist](" + ytURL + ")" + \
           "\n |[Wikipedia article](" + wikiURL + ")"
        comment.reply(commentString)
        already_done.add(comment.id)
