# encoding=utf8
# sep_imgur.py

# Get your API key information from here
# https://api.imgur.com/
# See lines 18, and 19 to fill in information

import imgurpython
import datetime
import sys

def run ():
	
	reload(sys)
	sys.setdefaultencoding('utf8')
	
	
	client_id = ""
	client_secret = ""
	client = imgurpython.ImgurClient ( client_id, client_secret )
	
	items = client.gallery()
	
	array = []
	counter = 0
	for row in items:
		
		# Determine what image to show
		g_item = client.gallery_item(row.id)
		cover = "https://i.imgur.com/KjsT4r8.png"
		if type( g_item ) is imgurpython.imgur.models.gallery_album.GalleryAlbum:
			cover = "https://i.imgur.com/%s.png" % g_item.cover
		elif type( g_item ) is imgurpython.imgur.models.gallery_image.GalleryImage:
			cover = row.link
		
		# Make the dict
		subarray = {
			"description":	str(row.description),
			"gallery":		str(row.in_gallery),
			"postID":		str(row.id),
			"link":			str(row.link),
			"nsfw":			str(row.nsfw),
			"points":		str(row.points),
			"processedurl":	str(cover),
			"time":			str(row.datetime),
			"views":		str(row.views)
		}
		
		# If nsfw easier for sql
		if subarray["nsfw"]:
			subarray['nsfw'] = "1"
		else:
			subarray['nsfw'] = "0"
		
		array.append(subarray)
		counter += 1
		
		if counter>4:
			break
	
	return array
