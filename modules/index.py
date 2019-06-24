#!/usr/bin/python3
import cherrypy
import config
import json

static_dir = '/templates/' # Needs to have trailing and leading slash '/'

class wellcome(object):
    '''Base Index constructor and expose function'''
    @cherrypy.expose
    def index(self):
        result = '''<a href="./select">SELECT</a>'''
        return result
    
    @cherrypy.expose
    def other(self):
        result = '<h1>Other</h1>'
        return result
