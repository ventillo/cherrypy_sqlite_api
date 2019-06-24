#!/usr/bin/python3
import os
import cherrypy
import config

from modules import index, sqlite

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))


def main_server_loop():
    ''' Master http server - the main executable / daemon
    
    Contains basic server settings and how the sub-modules
    are called and mounted to their respective paths

    Args:
        *None*

    Sets:
        *server_config*:    dict(), updates cherrypy.config
        *conf:*             dict(), see Cherrypy docs for more
        *cherrypy.config:*  dict(), see Cherrypy docs for more
        
    Returns:
        *N/A*

    Raises:
        *Exception*         If server is unable to start
    
    '''
    server_config = {
        'server.socket_host': config._SERVER_IP,
        'server.socket_port': config._SERVER_PORT
    }
    cherrypy.config.update(server_config)
    conf = {
        '/': {
            'tools.sessions.on': False
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }

    cherrypy.tree.mount(index.wellcome(), "/", conf)
    cherrypy.tree.mount(sqlite.insert(), "/insert", conf)
    cherrypy.tree.mount(sqlite.select(), "/select", conf)
    cherrypy.tree.mount(sqlite.delete(), "/delete", conf)
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    try:
        main_server_loop()
    except Exception as e:
        raise e
