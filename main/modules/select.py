import cherrypy


class select(object):
	@cherrypy.expose
	def index(self):
		with open('templates/select.html') as fh:
			index_f = fh.read()
		result = index_f.format(_title='select_strana', _heading='select')
		return result