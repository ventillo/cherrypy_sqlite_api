#!/usr/bin/python3
import cherrypy
import config
import sqlite3
import os
import json
from modules import htmlize

class Checker(object):
    def __init__(self):
        ''' Sanity check

        Describes tables in DB, or lists the contents

        Args:
            *None*

        Sets:
            *N/A:*    Nothing yet

        Returns:
            *N/A:*    boolean(), valid, or not?

        Raises:
            *N/A*     Nothing yet

        '''
        __name__ = "SQLite SQL validator"

    def is_table(db, table):
        ''' Checks if table exists in a DB

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
        db_file = f"{config._ROOT}/{config._DB_PATH}/{db}"
        try:
            open(db_file)
        except Exception as e:
            result = [ False, e ]
            
        return result 

        
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
        dbs = os.listdir(f"{config._ROOT}/{config._DB_PATH}")
        if len(vpath) == 1:
            schema = vpath.pop()
            if schema in dbs:
                cherrypy.request.params['schema'] = schema
                return self
            else:
                del schema
                return self

        elif len(vpath) == 2:
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
        db_file = f"{config._ROOT}/{config._DB_PATH}/{db}"
        if os.path.exists(db_file):
            error = False
            if os.path.isfile(db_file):
                error = False 
            else:
                error = f"{db_file} is not a standard file"
                html_result = htmlize.read_html('error', '/templates/')
                result = html_result.format(_error=error)
                return result
        else:
            error = f"{db_file} does not exist"
            html_result = htmlize.read_html('error', '/templates/')
            result = html_result.format(_error=error)
            return result
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
        self.html = ''
        self.json = {}
        url = cherrypy.url()
        if 'schema' in kwargs.keys():
            # No table is defined, we want the 'schema' of the DB
            try:
                db = kwargs["schema"]
                result = self.sqlite_wrapper(db)
                status = 'OK'
            except Exception as e:
                result = ''
                status = f"ERROR: {e}"
            self.html = htmlize.read_html('schema','/templates/')
            # schema has weird structure, returns (val,) hence schema[0]
            # [2] - third element '[0]CREATE [1]TABLE [2]'xyz' ...
            tables = [schema[0].split(' ')[2].strip('\'') for schema in result]
            self.html = self.html.format(
                _db=db,
                _schema=htmlize.tabelize(result),
                _tables=htmlize.tabelize_links(tables),
                _status=status
            )
            self.json.update({
                "result": {"tables": tables},
                "status": status
            })
        elif 'table' in kwargs.keys():
            # In case a table is defined, what are the values?
            db = kwargs['db']
            table = kwargs['table']
            try:
                result = self.sqlite_wrapper(
                    db,
                    table=table,
                    values=kwargs['values']
                )
                status = 'OK'
            except Exception as e:
                result = ''
                status = f"ERROR: {e}"
            self.html = htmlize.read_html('table','/templates/')
            self.html = self.html.format(
                _db=db,
                _table=table,
                _rows=htmlize.tabelize(result),
                _status=status
            )
            self.json.update({
                "result": {"rows": result},
                "status": status
            })
        elif url.split('/')[-2] == 'select':
            #No DB, nor table is defined, list DBs in config._DB_PATH 
            dbs = os.listdir(f"{config._ROOT}/{config._DB_PATH}")
            result = [db for db in dbs]
            self.html += htmlize.tabelize_links(result)
            self.json.update({
                "result":{"databases": result},
                "status": "OK"
            })
        else:
            result = htmlize.read_html('error', '/templates/')
            e = f'DB is non existent, or wrong parameter specified. Check URL'
            return result.format(_error=e)
        if 'json' in kwargs.keys():
            return json.dumps(self.json)
        else:
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
