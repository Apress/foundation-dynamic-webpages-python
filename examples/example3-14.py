#!/usr/bin/python3

from os import environ
import cgi, cgitb

userid = None
password = None
if environ.has_key('HTTP_COOKIE'):
    for cookie in map(strip, split(environ['HTTP+COOKIE'], ';')):
        (key, value) = split(cookie, '=')
        if key == 'UserID':
            userid = value
        if key == 'Password':
            password = value
# the Python variables Userid and password are now set to valid values or None
