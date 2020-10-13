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
pagedict['title'] = 'Example3-11'
pagedict['titleleft'] = ''
pagedict['main_menu'] = '<a href="/">&nbsp;Home&nbsp;</a>&nbsp;' + \
                        '<a href="/">&nbsp;Menu2&nbsp;</a>&nbsp;' + \
                        '<a href="/">&nbsp;Menu3&nbsp;</a>&nbsp;'
pagedict['content_left'] = ''
if form.getvalue('textdata'):
    textdata = form.getvalue('textdata')
else:
    textdata = "Nothing to display!"
data = """<p>The input text is as follows:</p>"""
data += textdata
data +="""<br/><br/><form action="/cgi-bin/example3-11.py" method="post">
<textarea name="textdata" cols="40" rows="10">
Type your text here:
</textarea><br/>
<input type="submit" value="Submit"/>
</form>"""
pagedict['content_right'] = data
asctime = time.asctime()
parts = asctime.split()
pagedict['year'] = parts[4]

# make the substitutions
html = page_template.substitute(pagedict)

# print the substituted lines
print(html)
