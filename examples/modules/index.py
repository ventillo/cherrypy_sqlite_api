#!/usr/bin/python3
import cherrypy
import json

static_dir = '/templates/' # Needs to have trailing and leading slash '/'

class wellcome(object):
    '''Base Index constructor and expose function'''
    @cherrypy.expose
    def index(self):
        result = '''{
            "firstName": "John",
            "lastName": "Smith",
            "isAlive": true,
            "age": 27,
            "address": {
                "streetAddress": "21 2nd Street",
                "city": "New York",
                "state": "NY",
                "postalCode": "10021-3100"
            },
            "phoneNumbers": [
                {
                "type": "home",
                "number": "212 555-1234"
                },
                {
                "type": "office",
                "number": "646 555-4567"
                },
                {
                "type": "mobile",
                "number": "123 456-7890"
                }
            ],
            "children": [],
            "spouse": null
            }'''
        return json.dumps(json.loads(result))
    
    @cherrypy.expose
    def other(self):
        result = '<h1>Other</h1>'
        return result
