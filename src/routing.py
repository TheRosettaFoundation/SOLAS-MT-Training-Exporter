import bottle
from bottle import route, run

@route('/', method='GET')
def homepage():
    return 'Hello world!'
    
@route('/events/:id', method='GET')
def get_event(id):
    return dict(name = 'Event ' + str(id))