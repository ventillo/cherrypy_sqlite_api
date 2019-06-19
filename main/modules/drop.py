import cherrypy


class drop(object):
	@cherrypy.expose
	def index(self):
		''' Method for open specific  html file
		and change it'''
		with open('templates/drop.html') as fh:
			index_f = fh.read()
		result = index_f.format(_title='drop_strana', _heading='drop')
		return result