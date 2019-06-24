#!/usr/bin/python3
import cherrypy
import config
import sqlite3
import os


class select(object):
    def __init__(self):
        ''' SELECT method for API

        Describes tables in DB, or lists the contents

        Args:
            *None*

        Sets:
            *self.html:*    dict(), see Cherrypy docs for more

        Returns:
            *self.html:*    string(), html code for rendering

        Raises:
            *RuntimeError*         If dB file cannot be found

        '''
        __name__ = "SQLite select API component"
        self.html = ''
        self.json = ''

    def CheckSelect(self):
        ''' Checks and sanitizes a query

        Escaping, sanitizing and checking what are we sending to the DB

        Args:
            *query*     Query to be sent to the DB

        Sets:
            *N/A*

        Returns:
            *result:*    bool(), is the code to be executed OK, or not

        Raises:
            *N/A*

        '''
        return True

    def _cp_dispatch(self, vpath):
        ''' Modify the request path, REST way

        Format the variables in a row:
        http://server/method/db_file/table/?values=<>&filter=<>

        Args:
            *vpath*     vpath - I don't quite understand this one,
                        is it internal, or just a dummy?

        Sets:
            *cherrypy.request.params:*  list(), various variable parameters
                                        for processing

        Returns:
            *vpath:*    list(), list of path elements

        Raises:
            *N/A*

        '''
        if len(vpath) == 1:
            cherrypy.request.params['schema'] = vpath.pop()
            return self

        if len(vpath) == 2:
            cherrypy.request.params['table'] = vpath.pop()
            cherrypy.request.params['db'] = vpath.pop()
            cherrypy.request.params['values'] = '*'
            return self
        return vpath

    def sqlite_wrapper(self, db, **kwargs):
        ''' Calling the actual data from DB

        Connect to DB, execute a query and return data

        Args:
            *db:*     str(), database file name
            ***kwargs:*   dict(), additional arguments to specify the
                            table and filters to retrieve the data by

        Sets:
            *N/A*

        Returns:
            *result:*    tuple(), rows from table, or DB schema as a tuple

        Raises:
            *N/A*

        '''
        db_file = f"{config._ROOT}/{db}"
        try:
            open(db_file)
        except Exception as e:
            raise RuntimeError(f"ERROR: Unable to read DB file: {e}")
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        if len(kwargs) == 0:
            query = f"SELECT sql FROM sqlite_master"
        else:
            query = f"SELECT * FROM {kwargs['table']}"
        c.execute(query)
        result = c.fetchall()
        conn.commit()
        conn.close()
        return result

    def tabelize(self, table_list):
        ''' Calling the actual data from DB

        Connect to DB, execute a query and return data

        Args:
            *table_list:*   tuple() / list(), rows and items as tuples / lists

        Sets:
            *N/A*

        Returns:
            *table:*    str(), html table code made from tuples / lists

        Raises:
            *N/A*

        '''
        table = '<table>'
        for row in table_list:
            table += '<tr>'
            for item in row:
                table += f"<td> {item} </td>"
            table += '</tr>'
        table += '</table>'
        return table

    @cherrypy.expose
    def index(self, **kwargs):
        ''' Extending the expose - index method

        Returns html / json output

        Args:
            ***kwargs:*   dict(), arguments needed for SELECT / SCHEMA
                            schema=<db_name> or
                            db=<db_name> AND table=<table_name> OPTINALLY
                            values=<columns_to_select>, filter=<conditions>

        Sets:
            *N/A*

        Returns:
            *result:*    str(), rhtml code to be rendered, or JSON

        Raises:
            *N/A*

        '''
        if 'schema' in kwargs.keys():
            result = self.sqlite_wrapper(
                kwargs["schema"]
            )
        else:
            result = self.sqlite_wrapper(
                kwargs['db'],
                table=kwargs['table'],
                values=kwargs['values']
            )
        self.html = ''
        self.html += self.tabelize(result)
        return self.html


class insert(object):
    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        return 'INSERT'


class delete(object):
    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        return 'INSERT'
