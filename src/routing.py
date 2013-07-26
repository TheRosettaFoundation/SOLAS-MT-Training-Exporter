from bottle import route, run, template, request
from database import baseXDB 

## Sends document to the db
@route('/document', method='POST')
def createDoc():
    document = request.body
    dataStore = baseXDB()
    dataStore.insert(document)
    return document

## Returns all documents on the db
@route('/document', method='GET')
def displayDocs():
    return "displaying all documents on db"

## Returns specified document on the db
@route('/document/:id', method='GET')
def get_event(id):
    return "displaying document " + id

 
run(host='localhost', port=8080, debug=True)


