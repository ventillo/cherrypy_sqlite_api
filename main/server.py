import cherrypy

#from modules import index
#from modules import select
#from modules import delete
#from modules import insert
#from modules import create
#from modules import drop
from modules import *


class main_server_loop(object):
    server_config = {
        'server_socket_host': '127.0.0.1',
        'server_socket_port': 80
    }
    cherrypy.config.update(server_config)
    @cherrypy.expose
    def index(self):
    	return "Hello World!"


cherrypy.quickstart(main_server_loop())