#!/usr/bin/python3

import os, time, string
import cgi, cgitb

form = cgi.FieldStorage()

page_top = """Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html>
<head>
   <title>$title</title>
   <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
   <link rel="stylesheet" type="text/css" href="/css/example2-2.css" />
   <script type="text/javascript">
       function displayImage(elem) {
          var image = document.getElementById("main-picture");
          image.src = elem.value;
       }
   </script>
</head>
<body>"""

page_bottom = """</body>
</html>"""

# get the document base for the html_lib directory
docroot = os.getenv('DOCUMENT_ROOT')
html_lib_path = docroot + '/html_lib/'

# get the page header
f = open(html_lib_path + 'example3-1.html', 'r')
page_header = f.read()
f.close()

# get the page menu bar
f = open(html_lib_path + 'example3-2.html', 'r')
page_menu_bar = f.read()
f.close()

# get the content
f = open(html_lib_path + 'example3-3.html', 'r')
page_content = f.read()
f.close()

# get the footer
f = open(html_lib_path + 'example3-4.html', 'r')
page_footer = f.read()
f.close()

# create the page template
page_template = string.Template(page_top + page_header + page_menu_bar +
                                page_content + page_footer + page_bottom)

# create the substitutable content
pagedict = dict()
pagedict['title'] = 'Hello'
pagedict['titleleft'] = ''
pagedict['main_menu'] = '<a href="/">&nbsp;Home&nbsp;</a>&nbsp;' + \
                        '<a href="/">&nbsp;Menu2&nbsp;</a>&nbsp;' + \
                        '<a href="/">&nbsp;Menu3&nbsp;</a>&nbsp;'
pagedict['content_left'] = ''
# test to see if we actually have any input
if 'first_name' not in form:
    first_name = ''
else:
    first_name = form.getvalue('first_name')
if 'last_name' not in form:
    last_name = ''
else:
    last_name = form.getvalue('last_name')
data = """<form action="/cgi-bin/example3-9.py" method="get">
First Name: <input type="text" name="first_name"/><br/>
Last Name: <input type="text" name="last_name"/><br/><br/>
<input type="Submit" value="Submit"/>
</form><br/><br/>
<h2>Hello """
pagedict['content_right'] = data + first_name + ' ' + last_name + '</h2>'
asctime = time.asctime()
parts = asctime.split()
pagedict['year'] = parts[4]

# make the substitutions
html = page_template.substitute(pagedict)

# print the substituted lines
print(html)
