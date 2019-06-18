import cherrypy


class drop(object):
	@cherrypy.expose
	def index(self):
		with open('templates/drop.html') as fh:
			index_f = fh.read()
		result = index_f.format(_title='drop_strana', _heading='drop')
		return result