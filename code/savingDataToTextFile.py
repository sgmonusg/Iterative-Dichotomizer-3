import sys
import urllib
import MySQLdb
if urllib.urlopen('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'):
	print("yes")
	text =urllib.urlopen('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data').read()
	#print(text)
	f=open("data.txt","w")
	f.write(text)
	f.close()	
