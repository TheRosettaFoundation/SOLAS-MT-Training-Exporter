from bottle import route, run, template, request
from database import baseXDB 

## Sends document to the db
@route('/database/<databaseName>/document', method='POST')
def createDoc(databaseName):
    document = request.body
    dataStore = baseXDB()
    dataStore.setDatabase(databaseName)
    dataStore.insert(document)
    return document

## Drops the specified database
@route('/database/<name>', method='DELETE')
def dropDatabase(name):
    dataStore = baseXDB()
    dataStore.dropDatabase(name)
 
## Returns all databases
@route('/database', method='GET')
def showDatabases():
    dataStore = baseXDB()
    dataStore.showDatabases()
   
## Returns all documents on the db
@route('/database/<databaseName>/document', method='GET')
def displayDocs(databaseName):
    dataStore = baseXDB()
    dataStore.setDatabase(databaseName)
    return dataStore.queryElements()



#/database/<databaseName>/document/:id?query=//group[domain=helth]/transunit[id<20 and id>023]&


## Returns specified document on the db
@route('/database/<databaseName>/document/:id', method='GET')
def get_event(id):
    return "displaying document " + id

 
run(host='localhost', port=8080, debug=True)


