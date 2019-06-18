import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        with open('./templates/index.html') as fh:
            index_f = fh.read()
        result = index_f.format(_title='Nazev_stranky', _nadpis='Cokoliv!')
        return result


cherrypy.quickstart(HelloWorld())
