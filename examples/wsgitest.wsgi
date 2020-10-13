import sys
import os

def application(environ, start_response):
    status = '200 OK'

    output = ''
    output += "sys.version = %s\n" % repr(sys.version)
    output += "sys.prefix = %s\n" % repr(sys.prefix)
    output += "path = %s\n" % os.environ['PATH']
    output += "REQUEST_METHOD = %s\n" % environ['REQUEST_METHOD']
    name = 'SCRIPT_NAME'
    if name in environ:
        output += name + " = %s\n" % environ[name]
    else:
        output += name + " =\n"
    name = 'PATH_INFO'
    if name in environ:
        output += name + " = %s\n" % environ[name]
    else:
        output += name + " =\n"
    name = 'QUERY_STRING'
    if name in environ:
        output += name + " = %s\n" % environ[name]
    else:
        output += name + " =\n"
    name = 'CONTENT_TYPE'
    if name in environ:
        output += name + " = %s\n" % environ[name]
    else:
        output += name + " =\n"
    name = 'CONTENT_LENGTH'
    if name in environ:
        output += name + " = %s\n" % environ[name]
    else:
        output += name + " =\n"
    output += "SERVER_NAME = %s\n" % environ["SERVER_NAME"]
    output += "SERVER_PORT = %s\n" % environ["SERVER_PORT"]
    output += "SERVER_PROTOCOL = %s\n" % environ["SERVER_PROTOCOL"]
    (v1, v2) = environ["wsgi.version"]
    output += "wsgi.version = %s\n" % str(v1) + '.' + str(v2)
    output += "wsgi.url_scheme = %s\n" % environ["wsgi.url_scheme"]
    output += "wsgi.multithread = %s\n" % environ["wsgi.multithread"]
    output += "wsgi.multiprocess = %s\n" % environ["wsgi.multiprocess"]
    output += "wsgi.run_once = %s\n" % environ["wsgi.run_once"]

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output.encode('utf-8')]


