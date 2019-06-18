import cherrypy


class create(object):
	@cherrypy.expose
	def index(self):
		with open('templates/create.html') as fh:
			index_f = fh.read()
		result = index_f.format(_title='create_strana', _heading='create')
		return result