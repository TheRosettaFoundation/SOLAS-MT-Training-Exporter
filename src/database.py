import BaseXClient

class baseXDB:

    ## possibly set the address, port and other credentials to log into the db here throught the constructor
    def __init__(self, address='localhost', port=1984, username='admin', password='admin'):
        self.address = address
        self.port = port
        self.username = username
        self.password = password
    
    def insert(self, data):
        try:
            
            #create session
            session = BaseXClient.Session(self.address, self.port, self.username, self.password)
            #create new database
         
            session.create("database", data.getvalue())
            print session.info()
            
            # run query on database
            #print "\n" + session.execute("xquery doc('database')")
            
            # drop database
            session.execute("drop db database")
            
            # close session
            session.close()
            
        except IOError as e:
            # print exception
            print e
        