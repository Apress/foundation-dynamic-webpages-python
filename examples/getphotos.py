#!/usr/bin/python3

import time, string, os


html = string.Template("""Content-type:text/html\r\n\r\n
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" 
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>www.holmes4.com</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<link rel="stylesheet" type="text/css" href="/css/styles.css" />
<script type="text/javascript">
    function displayImage(elem) {
      var image = document.getElementById("main-picture");
      image.src = ""; image.src = elem.value;
    }
</script>
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
    <div id="localmenucolumn">
        <div style="line-height:22px">
            <select name="pic-list" style="margin-left:10px; width:150px" size="30" onchange="displayImage(this);">
<!--- **** List of picture files goes here **** -->
            $pictures
<!--- **** End list of picture files **** -->
            </select>
        </div>
    </div> <!-- End Menu Column -->
    <!-- Begin Content Column -->
    <div id="contentcolumn"> 
    <h2>$picpath</h2>
        <p>It could take some time for the image to load, please be patient.</p>
        <img id="main-picture" style="vertical-align: middle;" width="1200" border="0" />
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
subterms['localnavtitle'] = "pictures"
realroot = '/pub/pictures/'
picpath = os.environ['DOCUMENT_URI']
picpath = picpath.rstrip('index.html')
subterms['picpath'] = picpath
# get the list of all files in the picture path
files = os.listdir(realroot + picpath.lstrip('/photos'))
files.sort()
# if the file is a picture then include it, otherwise skip it
piclist = ''
for fname in files:
    if fname.find('.jpg') >= 0:
        piclist = piclist + '            <option value="' + picpath + fname + '">' + fname + '</option>\n'
        continue
    if fname.find('.JPG') >= 0:
        piclist = piclist + '            <option value="' + picpath + fname + '">' + fname + '</option>\n'
        continue
    if fname.find('.png') >= 0:
        piclist = piclist + '            <option value="' + picpath + fname + '">' + fname + '</option>\n'
        continue
    if fname.find('.PNG') >= 0:
        piclist = piclist + '            <option value="' + picpath + fname + '">' + fname + '</option>\n'
        continue
    if fname.find('.gif') >= 0:
        piclist = piclist + '            <option value="' + picpath + fname + '">' + fname + '</option>\n'
        continue
    if fname.find('.GIF') >= 0:
        piclist = piclist + '            <option value="' + picpath + fname + '">' + fname + '</option>\n'
        continue
subterms['pictures'] = piclist
asctime = time.asctime()
parts = asctime.split()
subterms['year'] = parts[4]

# make the substitutions
mod_html = html.substitute(subterms)

# print the substituted lines
print(mod_html)







