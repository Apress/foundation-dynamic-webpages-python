#!/usr/bin/python

import os

print("Content-type: text/html\r\n\r\n")
print("<html><body></br>")
print("<font size=+1>Environment</font></br>")
for param in os.environ.keys():
    line = "<b>%s</b>: %s</br>" % (param, os.environ[param])
    print(line)
print("</body></html>")
