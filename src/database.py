import BaseXClient, time
from keyring.tests.test_backend import random_string
from xml.dom.minidom import parse, parseString

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
            
            dom = parseString(data.getvalue()) # Parse an XML file by name
            # get the current element
            
            
            # and check to see if it has a domain attribute
            self.applyDomainInheritence(dom, dom.documentElement, None)
            
            print dom.toxml()
            
            #create session
            session = BaseXClient.Session(self.address, self.port, self.username, self.password)
            
            dbStr = dbStr= session.execute("xquery math:uuid()")
            # try to just insert new value into specified db     
            try:
                session.execute("open {0}".format(self.databaseName))
                
                session.add(dbStr, dom.toxml())
                #pathStr = self.databaseName+".xml"
                #session.add(pathStr, data.getvalue())
                print session.info()
                
            except IOError as e:
                # if that fails we can assume that the db doesn't exist, so create it and insert value
                session.execute("create db {0}".format(self.databaseName))
                session.add(dbStr, dom.toxml())
                
    
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

    def applyDomainInheritence(self, inputDom, data, domain):
        #dom = inputDom
        varNode = data
        
        #print varNode.toxml()
        #print varNode.attributes.keys()

        # if the current node does not contain a domain attrib
        if varNode.getAttribute('itsxlf:domains') == '':
            # then add the parent domain if it exists
            if domain != None:
                varNode.setAttribute('itsxlf:domains', domain)
                print "parent attribute added"
            else:
                print "no parent attribute added"
        else:
            # if an attribute already exists on the current node, then set that to the current one
            domain = varNode.getAttribute('itsxlf:domains')
            
        # get the root element as a node
        nodes = data.childNodes # getElementsByTagName("xliff")[0]
        
        for node in nodes:
            if node.nodeType == node.ELEMENT_NODE:
                self.applyDomainInheritence(inputDom, node, domain)
        
    
        
        
        
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
    