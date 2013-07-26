from bottle import route, run, template, request

## Sends document to the db
@route('/document', method='POST')
def createDoc():
    document = request.body
    return document

## Returns all documents on the db
@route('/document', method='GET')
def displayDocs():
    return "displaying all documents on db"

## Returns specified document on the db
@route('/document/:id', method='GET')
def get_event(id):
    return "displaying document " + id
    

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

 
run(host='localhost', port=8080, debug=True)


