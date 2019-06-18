import cherrypy


class insert(object):
	@cherrypy.expose
	def index(self):
		with open('templates/insert.html') as fh:
			index_f = fh.read()
		result = index_f.format(_title='insert_strana', _heading='insert')
		return result