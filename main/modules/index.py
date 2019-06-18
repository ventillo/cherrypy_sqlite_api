import cherrypy


class wellcome(object):
	@cherrypy.expose
	def index(self):
		with open('templates/index.html') as fh:
			index_f = fh.read()
		result = index_f.format(_title='Titulni_strana', _heading='Vítejte!')
		return result