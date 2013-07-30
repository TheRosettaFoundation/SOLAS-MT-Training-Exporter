import BaseXClient, time
from keyring.tests.test_backend import random_string

class baseXDB:

    ## possibly set the address, port and other credentials to log into the db here throught the constructor
    def __init__(self, address='localhost', port=1984, username='admin', password='admin'):
        self.address = address
        self.port = port
        self.username = username
        self.password = password
        self.databaseName = 'database'
        
    def setDatabase(self, databaseName):
        self.databaseName = databaseName
    
    def insert(self, data):
        try:
            
            #create session
            session = BaseXClient.Session(self.address, self.port, self.username, self.password)
            
            #create new database
            #session.create(self.databaseName, data.getvalue())
            #session.create(self.databaseName, data.getvalue())
            
            # try to just insert new value into specified db
            
            try:
                #session.execute("")
                session.execute("open {0}".format(self.databaseName))
                dbStr= random_string(8)
                session.add(dbStr, data.getvalue())
                #pathStr = self.databaseName+".xml"
                #session.add(pathStr, data.getvalue())
                print session.info()
                
            except IOError as e:
            # if that fails we can assume that the db doesn't exist, so create it and insert value
                session.create(self.databaseName, data.getvalue())
    
#             # print exception
                print e
            
            print session.info()
            
            # run query on database
            #print "\n" + session.execute("xquery doc('database')")
            
            # close session
            session.close()
            
            
        except IOError as e:
            # print exception
            print e

    def dropDatabase(self, databaseName):
        #create session
        session = BaseXClient.Session(self.address, self.port, self.username, self.password)
        
        # drop database
        session.execute("drop db "+ databaseName)
            
        # close session
        session.close()
    
    def showDatabases(self):
        #create session
        session = BaseXClient.Session(self.address, self.port, self.username, self.password)
        
        # drop database
        print session.execute("show databases")
            
        # close session
        session.close()
        
    def queryElements(self):
        #create session
        session = BaseXClient.Session(self.address, self.port, self.username, self.password)
        
        session.execute("open {0}".format(self.databaseName))

        return session.execute("xquery /")
        
        # close session
        session.close()
    