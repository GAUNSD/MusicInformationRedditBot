# Test 2

import praw


r = praw.Reddit(user_agent='Music Artist Information by /u/Gustavo0929')
r.login('MusicInformation','214146')

########################### from the tutorial #######
#   https://praw.readthedocs.org/en/stable/pages/comment_parsing.html
#
# Comment parser
# This Section will read the comments and depending on what is found, it'll comment information on the indicated artist

r = praw.Reddit('MusicInformation service by /u/Gustavo0929')
r.login('MusicInformation', '214146')
submission = r.get_submission(submission_id='3uogoc')
flat_comments = praw.helpers.flatten_tree(submission.comments)

multiReddits = r.get_comments('music+hiphopheads+listentothis')

artist = ["Kendrick Lamar", "Kanye", "Rick Ross"]

already_done = set()
for comment in multiReddits:
    print comment.body
    print "\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44"
