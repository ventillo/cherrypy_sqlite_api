#Comments and PEP8 format TODO
import cherrypy
import os

from modules import select
from modules import delete
from modules import insert
from modules import create
from modules import drop
from modules import index

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))


class main_server_loop(object):
	cherrypy.config.update({'server.socket_host': '127.0.0.1',
							'server.socket_port': 80,
						})
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
	cherrypy.tree.mount(select.select(), "/select", conf)
	cherrypy.tree.mount(delete.delete(), "/delete", conf)
	cherrypy.tree.mount(insert.insert(), "/insert", conf)
	cherrypy.tree.mount(create.create(), "/create", conf)
	cherrypy.tree.mount(drop.drop(), "/drop", conf)
	cherrypy.engine.start()


if __name__ == '__main__':
	try:
		main_server_loop()
	except Exception as e:
		raise e