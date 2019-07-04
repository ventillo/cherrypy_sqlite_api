import config

def tabelize(table_list):
    ''' Construct a table out of 

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
        if not isinstance(row, (list,tuple)):
            table += f"<td> {row} </td>"
        else:
            for item in row:
                table += f"<td> {item} </td>"
        table += '</tr>'
    table += '</table>'
    return table

def tabelize_links(table_list):
    ''' Making a table with links

    Constructs a clickable link in HTML, so that the link points to ./link

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
        if not isinstance(row, (list, tuple)):
            table += f"<td> <a href=\"./{row}/\">{row}</a> </td>"
        else:
            for item in row:
                table += f"<td> <a href=\"./{item}/\">{item}</a> </td>"
        table += '</tr>'
    table += '</table>'
    return table

def read_html(filename, _STATIC_DIR):
    '''Read a html file

    Reads a file from a selected static directory - needs to be set as static
    in the cherrypy (chttpd.py).

    Args:
        ``filename`` *str()*, plain filename, without any path specification,
        without extension 
        ``_STATIC_DIR`` *str()*, path relative to the project root,
        where chttpd.py resides

    Returns:
        *str()*, parsed html code from the read file, or a HTML
        formatted error if file cannot be read for any reason

    Exceptions:
        On file read fail, string with Exception text is returned
        
    '''
    read_path = config._ROOT+ _STATIC_DIR + filename + '.html'
    try:
        with open(read_path, 'r') as handle:
            return handle.read()
    except Exception as e:
        return """<div>ERROR: {}!</div><br>{}""".format(e, read_path)
