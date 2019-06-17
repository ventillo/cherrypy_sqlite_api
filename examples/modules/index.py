#!/usr/bin/python3
import cherrypy
import config

static_dir = '/templates/' # Needs to have trailing and leading slash '/'

class wellcome(object):
    '''Base Index constructor and expose function'''
    @cherrypy.expose
    def index(self):
        result = '<h1>Wellcome</h1>'
        return result
