from bottle import route, run, template, request
from database import baseXDB 

## Sends document to the db
@route('/databases/<databaseName>/documents', method='POST')
def createDoc(databaseName):
    document = request.body
    dataStore = baseXDB()
    dataStore.setDatabase(databaseName)
    return dataStore.insert(document)
    #return document

## Drops the specified database
@route('/databases/<name>', method='DELETE')
def dropDatabase(name):
    dataStore = baseXDB()
    dataStore.dropDatabase(name)
 
## Returns all databases
@route('/databases', method='GET')
def showDatabases():
    dataStore = baseXDB()
    return dataStore.queryDB("list")
   
## Returns all documents on a specified db
@route('/databases/<databaseName>/documents', method='GET')
def displayDocs(databaseName):
    dataStore = baseXDB()
    dataStore.setDatabase(databaseName)
    return dataStore.queryDB("xquery /")

## Returns specified document
@route('/databases/<databaseName>/documents/<idStr>', method='GET')
def retrieveElement(databaseName, idStr):
    dataStore = baseXDB()
    dataStore.setDatabase(databaseName)
    return dataStore.queryDB("xquery collection('{0}/{1}')".format(databaseName, idStr))

## Returns transunits which contain specified domains from a specified db 
@route('/databases/<databaseName>/transunit/<domain>', method='GET')
def retrieveTransUnitsDB(databaseName, domain):
    dataStore = baseXDB()
    dataStore.setDatabase(databaseName)
    return dataStore.queryDB("xquery //*[local-name()='trans-unit' and @*:domains='{0}']".format(domain))

## Returns transunits which contain specified domains from a specified document
@route('/databases/<databaseName>/documents/<idStr>/transunit/<domain>', method='GET')
def retrieveTransUnits(databaseName, idStr, domain):
    dataStore = baseXDB()
    dataStore.setDatabase(databaseName)
    return dataStore.queryDB("xquery collection('{0}/{1}')//*[local-name()='trans-unit' and @*:domains='{2}']".format(databaseName, idStr, domain))

## Delete a specified document
@route('/databases/<databaseName>/documents/<idStr>', method='DELETE')
def updateElement(databaseName, idStr):
    dataStore = baseXDB()
    dataStore.setDatabase(databaseName)
    return dataStore.queryDB("delete {0}".format(idStr))

# ## Add a specified document
# @route('/databases/<databaseName>/documents/<idStr>', method='PUT')
# def addElement(databaseName, idStr):
#     dataStore = baseXDB()
#     dataStore.setDatabase(databaseName)
#     return dataStore.queryDB("add {0}".format(idStr))

#/database/<databaseName>/document/:id?query=//group[domain=helth]/transunit[id<20 and id>023]&

 
run(host='localhost', port=8080, debug=True)


