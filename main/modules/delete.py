import cherrypy


class delete(object):
	@cherrypy.expose
	def index(self):
		with open('templates/delete.html') as fh:
			index_f = fh.read()
		result = index_f.format(_title='delete_strana', _heading='delete')
		return result