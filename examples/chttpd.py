#!/usr/bin/python3
import os
import cherrypy

from modules import index

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))


def main_server_loop():
    ''' Master http server - the main executable / daemon
    
    Contains basic server settings and how the sub-modules
    are called and mounted to their respective paths

    Args:
        *None*

    Sets:
        *server_config:*    dict(), updates cherrypy.config
        *conf:*             dict(), see Cherrypy docs for more
        *cherrypy.config:*  dict(), see Cherrypy docs for more
        
    Returns:
        *N/A*

    Raises:
        *Exception*         If server is unable to start
    
    '''
    server_config={
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 80
    }
    cherrypy.config.update(server_config)
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(SCRIPT_PATH + '/')
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }

    cherrypy.tree.mount(index.wellcome(), "/", conf)
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    try:
        main_server_loop()
    except Exception as e:
        raise e
