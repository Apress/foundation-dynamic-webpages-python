#!/usr/bin/python3

from time import gmtime, strftime

print('Content-type:text/html\r\n\r\n')
print('<!DOCTYPE html>')
print('<html>')
print('<body>')
print('<p>This is output from the example4-3a.py cgi script. ')
print('The current date is ' + strftime("%A %c", gmtime()) + '.</p>')
print('</body>')
print('</html>')






