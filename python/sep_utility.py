# encoding=utf8
# sep_utility.py

import mysql.connector
import time
import pprint
import sys

DB_CONFIG = {
	"user":		"",
	"password":	"",
	"host":		"",
	"database":	""
}

def unpackArray ( array, connector, prefix, postfix ):
	
	goodstring = ""
	i = 0
	
	for row in array:
		if i > 0:
			sanitizer = row.replace ( '"', "'" )
			goodstring = "%s%s%s" % ( goodstring, connector, sanitizer )
		else:
			goodstring = row
			i = i+1
	
	goodstring = "%s%s%s" % ( prefix, goodstring, postfix )
	
	return goodstring

def generateString ( dbname, args ):
	
	reload(sys)
	sys.setdefaultencoding('utf8')
	pp = pprint.PrettyPrinter(indent=4)
	
	valueID = [] # Contrains keys
	valueVals = [] # Contains values
	
	for vars in args:
		for k, v in vars.iteritems():
			if k not in valueID:
				valueID.append(k)
	
	for vars in args:
		a = []
		for k, v in vars.iteritems():
			a.append(v)
		valueVals.append(a)
	
	baseSQL = "INSERT INTO %s ( %s ) VALUES " % ( dbname, unpackArray(valueID, ", ", "", "") )
	
	valuelist = []
	for row in valueVals:
		aa = unpackArray ( row, '", "','("','"),' )
		baseSQL = "%s%s" % ( baseSQL, aa )
	
	return baseSQL[:-1]+";"

def runSQL ( SQL_string ):
	
	cnx = mysql.connector.connect(**DB_CONFIG)
	cursor = cnx.cursor()
	cursor.execute ( SQL_string )
	cnx.commit()
	cursor.close()
	cnx.close()

def runSQLlist ( SQL_list ):
	
	cnx = mysql.connector.connect(**DB_CONFIG)
	cursor = cnx.cursor()
	
	for row in SQL_list:
		cursor.execute ( row )
	
	cnx.commit()
	cursor.close()
	cnx.close()
	
def timeMillis ():
	return int( round(time.time()*1000) )