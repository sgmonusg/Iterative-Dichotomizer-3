import MySQLdb
import sys
import os
import logging


class database:
    
    """
	This class defines the database that is used to create the bag-of-words representation

	"""
    
    def __init__(self,usID='sagar', pswd='toor@123', dbase='IR_assign', hst='localhost'):
        self.userID = usID
        self.password = pswd
        self.database = dbase
        self.host = hst
        self.N = 0
        try:
            self.db = MySQLdb.connect(self.host, self.userID, self.password, self.database)
            logging.info('Able to connect to database')
        except:
            logging.error('Error initialising database')

    def __del__(self):
        self.db.close()

    def create_table_docf(self):    
        """This function creates the table DOC_FREQ which stores all words and their document frequencies"""
		#prepare the cursor
        cursor=self.db.cursor()
        sql='''CREATE TABLE  DOC_FREQ(
                WORD VARCHAR(50),
                FREQ INT,
                PRIMARY KEY(WORD) 
                )'''
        try:
            cursor.execute(sql)
            logging.info("Created table DOC_FREQ")
        except:
            logging.warning("Could not create table DOC_FREQ. Table may already be existing")
        finally:
            cursor.close()

    def add_to_doc_freq(self,word,count):
    	"""This function adds words and their frequencies ti the table DOC_FREQ """
        cursor=self.db.cursor();
        sql="INSERT into DOC_FREQ values ('"+word+"',"+str(count)+")"
        #print sql
        try:
            cursor.execute(sql)
            logging.info("Added word: "+word+" frequency: "+str(count)+" into DOC_FREQ")
            self.db.commit()
        except:
            logging.error("Error adding word:"+word+" frequency:"+str(count)+" into DOC_FREQ")
        finally:
            cursor.close()

    def create_table_doc(self,docname):
    	"""This function creates the table for each document idenitfied by parameter docname"""
        cursor=self.db.cursor()
        sql='''CREATE TABLE %s(TERM VARCHAR(50),TF INT,PRIMARY KEY(TERM))''' %docname
        try:
            cursor.execute(sql)
            logging.info("Created table %s"%docname)
        except:
            logging.error("Error creating table for document %s" %docname)
            self.db.rollback()
        finally:
            cursor.close()
    
    def insert_into_doc(self,docname,word,count):
    	"""This function adds words and their frequencies into the table corresponding to the document in which they occur"""
        cursor=self.db.cursor();
        sql="INSERT into " + docname +" values ('"+word+"',"+str(count)+")"
        #print sql
        try:
            cursor.execute(sql)
            logging.info("Added word: "+word+" having count: "+str(count)+" into "+docname)
            self.db.commit()
        except:
            logging.error("Error inserting word:"+word+" count:"+str(count)+" into table "+docname)
            self.db.rollback()
        finally:
            cursor.close()   

    
    def set_no_of_doc(self,N):
    	"""
    	Sets the number of documents in database
    	"""
    	self.N=N
    
    def get_no_of_doc(self):
    	"""
    	Gets the number of documents in database
    	"""
    	return self.N 
    
    def set_total_words(self,N):
    	"""
    	Sets the total number of words in database
    	"""
    	self.total_words=N
    
    def get_total_words(self):
    	"""
    	Gets the total number of words in database
    	"""
    	return self.total_words  
