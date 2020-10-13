#!/usr/bin/python3

import time, string


html = string.Template("""Content-type:text/html\r\n\r\n
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" 
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>www.holmes4.com</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<link rel="stylesheet" type="text/css" href="/css/styles.css" />
</head>
<body>
    <!-- Begin Picture Column -->
    <div id="piccolumn"> 
        <a href="/"><img src="/images/html_Dora.jpg" alt="Holmes4" /></a>
        <br />image by W.David Ashley
    </div>
    <!-- Begin Title Column -->
    <div id="titlecolumn"><h1>$maintitle</h1> 
    </div>

    <!-- Begin Local Navigation Title Column -->
    <div id="localnavigationtitle">$localnavtitle
    </div>
    <!-- Begin Main Menu Column -->
    <div id="mainmenucolumn"><a href="/">&nbsp;Home&nbsp;</a>&nbsp;
        <a href="/photos/">&nbsp;Family&nbsp;Pictures&nbsp;</a>&nbsp;
        <a href="/wda/blogs/index.html">&nbsp;David's&nbsp;Blogs&nbsp;</a>&nbsp;
    </div>

    <!-- Begin Local Menu Column -->
    <div id="localmenucolumn">$localmenucol
    </div> <!-- End Menu Column -->
    <!-- Begin Content Column -->
    <div id="contentcolumn">$contentcol 
    </div> <!-- End Content Column -->
    <!-- Begin Footer -->
    <div id="footer"><img alt="Powered by Apache" src="/images/apache_pb.png" />
            <br />&#169; Copyright 2010-$year
            W. David Ashley. All rights reserved. 
    </div> <!-- End Footer -->
</body>
</html>
""")

# create the substitution variables as a dictionary
subterms = {}
subterms['maintitle'] = "www.holmes4.com"
subterms['localnavtitle'] = "holmes4 links"
subterms['localmenucol'] = """<a href='/photos/'><b>.</b>Photos</a><br />
        <a href='/wda/index.html'><b>.</b>David Ashley</a><br />"""
subterms['contentcol'] = """<h2>Welcome</h2><p>Welcome to the 
        <a href='/' target='_top'>Holmes4</a>
        web site.</p>"""
asctime = time.asctime()
parts = asctime.split()
subterms['year'] = parts[4]

# make the substitutions
mod_html = html.substitute(subterms)

# print the substituted lines
print(mod_html)







