import BaseXClient, time
from keyring.tests.test_backend import random_string

class baseXDB:

    ## possibly set the address, port and other credentials to log into the db here throught the constructor
    def __init__(self, address='localhost', port=1984, username='admin', password='admin'):
        self.address = address
        self.port = port
        self.username = username
        self.password = password
        self.databaseName = ''
        
    def setDatabase(self, databaseName):
        self.databaseName = databaseName
    
    def insert(self, data):
        try:
            
            #create session
            session = BaseXClient.Session(self.address, self.port, self.username, self.password)
            
            dbStr = dbStr= session.execute("xquery math:uuid()")
            # try to just insert new value into specified db     
            try:
                session.execute("open {0}".format(self.databaseName))
                
                session.add(dbStr, data.getvalue())
                #pathStr = self.databaseName+".xml"
                #session.add(pathStr, data.getvalue())
                print session.info()
                
            except IOError as e:
                # if that fails we can assume that the db doesn't exist, so create it and insert value
                session.execute("create db {0}".format(self.databaseName))
                session.add(dbStr, data.getvalue())
                
    
                # print exception
                print e
            
            print session.info()
            
            
            
            # close session
            session.close()
            
            # return the key
            return dbStr
            
        except IOError as e:
            # print exception
            print e

    def dropDatabase(self, databaseName):
        #create session
        session = BaseXClient.Session(self.address, self.port, self.username, self.password)
        
        # drop database
        session.execute("drop db "+ databaseName)
        ret = session.info()
            
        # close session
        session.close()
        
        return ret 
    
    
    
    def queryDB(self, queryStr):
        #create session
        session = BaseXClient.Session(self.address, self.port, self.username, self.password)
        if self.databaseName != '':
            session.execute("open {0}".format(self.databaseName))
        
        ret = session.execute(queryStr)
        
        session.info()
        session.close()
        
        return ret
    