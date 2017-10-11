# encoding=utf8
# sep_reddit.py

import praw
import pprint
import sys

#reddit details
#user 
#pass 

def run ():
	
	reload(sys)
	sys.setdefaultencoding('utf8')
	
	pp = pprint.PrettyPrinter(indent=4)
	
	reddit = praw.Reddit(
		client_id="",
		client_secret="",
		password="",
		user_agent="",
		username=""
	)
	
	array = []
	for subreddit in reddit.subreddit('popular').hot(limit=5):
		
		subarray = {
			"author":		str(subreddit.author.name),
			"link":			"%s%s" % ("http://reddit.com", str(subreddit.permalink) ),
			"nsfw":			subreddit.over_18,
			"posted":		str(subreddit.created),
			"selftext":		str(subreddit.selftext),
			"subreddit":	str(subreddit.subreddit.display_name),
			"title":		str(subreddit.title),
			"upvotes":		str(subreddit.ups),
			"url":			str(subreddit.url)
		}
		
		# Make sure its SFW
		if subarray["nsfw"]:
			subarray["nsfw"] = "1"
		else:
			subarray["nsfw"] = "0"
		
		array.append ( subarray )
	
	# pp.pprint ( array )
	
	return array
