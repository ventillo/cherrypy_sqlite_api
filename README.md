# cherrypy_sqlite_restapi

Simple, lightweight, universal SQLite API, based on cherrypy.

## Requirements:
    1. universal
    2. ssl / non-ssl versions
    3. secure / cleanup of querries
    4. DB/table specification
    5. row inserts
    6. row deletes
    7. row modifies

## REST API
https://www.restapitutorial.com/

## Cherrypy http microframework / server
https://cherrypy.org/

## Progress
1. set up Cherrypy server as base for RESTAPI (matoumi)
    - cherrypy base, config, root, ssl (later)?
    - responses for /insert /select /delete /modify
    
2. classes and functions for DB operations and mapping
    - Conditions operators and values can obviously be merged to one statement
      and sent to the API as is - then need to be validated.
    - INSERT
        - INSERT INTO {table} VALUES({val1}, {val2})
        - validate number of fields and types
        - error handling and tracebacks
    - SELECT
        - SELECT {fields} FROM {table} WHERE {condition} {operator} {value}
        - the whole where cluase is optional, but needs to be implemented
    - DELETE
        - DELETE FROM {table} WHERE {condition} {operator} {value}
    - MODIFY / ALTER

3. aggregate functions and complex queries mapping
