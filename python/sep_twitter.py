# encoding=utf8
# sep_twitter.py

import twitter
import pprint
import json
import sys

def run ( countryID ):
	
	reload(sys)
	sys.setdefaultencoding('utf8')
	
	api = twitter.Api (
		consumer_key="",
		consumer_secret="",
		access_token_key="",
		access_token_secret="" )
	
	country = {
		"AU":23424748,
		"UK":23424975,
		"US":2450022,
		"WORLD":1
	}
	
	trends = api.GetTrendsWoeid ( int ( country.get(countryID, 1) ) )
	
	array = []
	counter = 0
	for row in trends:
		subarray = {
			"name":row.name,
			"time":row.timestamp,
			"tweets":row.tweet_volume,
			"url":row.url
		}
		
		try:
			subarray["tweets"] = int(subarray["tweets"])
		except:
			subarray["tweets"] = 0
		
		array.append(subarray)
		counter += 1
		
		if counter>4:
			break
	
	return array