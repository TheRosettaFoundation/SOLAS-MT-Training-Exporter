import BaseXClient

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
         
            session.create(self.databaseName, data.getvalue())
            print session.info()
            
            # run query on database
            #print "\n" + session.execute("xquery doc('database')")
            
            
            
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