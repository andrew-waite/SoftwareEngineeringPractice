
# sep_main.py

import sep_imgur as probeImgur
import sep_reddit as probeReddit
import sep_twitter as probeTwitter
import sep_youtube as probeYoutube
import sep_utility as utility
import pprint

if __name__ == "__main__":
	pp = pprint.PrettyPrinter(indent=4)
	
	time = utility.timeMillis()	
	print "Gathering Data from websites"
	prbYoutube = probeYoutube.run("AU")
	prbTwitter = probeTwitter.run("AU")
	prbReddit = probeReddit.run()
	prbImgur = probeImgur.run()
	print "Gathered in %sms\n" % ( utility.timeMillis()-time )
	time = utility.timeMillis()	
	
	print "Generating SQL strings"
	SQL_youtube = utility.generateString ( "youtube", prbYoutube )
	SQL_twitter = utility.generateString ( "twitter", prbTwitter )
	SQL_reddit = utility.generateString ( "reddit", prbReddit )
	SQL_imgur = utility.generateString ( "imgur", prbImgur )
	print "Generated in %sms\n" % ( utility.timeMillis()-time )
	time = utility.timeMillis()	
	
	print "Executing SQL"
	utility.runSQLlist ( [ SQL_youtube, SQL_twitter, SQL_reddit, SQL_imgur ] ) #efficient
	# utility.runSQL ( SQL_youtube ) # inefficient
	# utility.runSQL ( SQL_twitter ) # inefficient
	# utility.runSQL ( SQL_reddit ) # inefficient
	# utility.runSQL ( SQL_imgur ) # inefficient
	print "Executed in %sms\n" % ( utility.timeMillis()-time )
	