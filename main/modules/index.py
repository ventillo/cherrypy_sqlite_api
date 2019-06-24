import cherrypy


class wellcome(object):
	@cherrypy.expose
	def index(self):
		''' Method for open specific  html file
		and change it'''
		with open('templates/index.html') as fh:
			index_f = fh.read()
		result = index_f.format(_title='Titulni_strana', _heading='Vítejte!')
		fh.close()
		return result
