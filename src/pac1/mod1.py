'''
Created on 24 Jul 2013

@author: philip
'''

import BaseXClient

try:
    
    #create session
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
    
    #create new database
    session.create("database", "<x>Hello World!</x>")
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
    