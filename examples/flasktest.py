from flask import Flask
import os, time, string

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/second")
def hello2():
    return "Hello second!"

@app.route("/pictures")
def hello3():
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
    (docroot, tail) = os.path.split(__file__)  # split off the file name
    (docroot, tail) = os.path.split(docroot)   # split off the first directory
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
    page_content = """
        <!--Begin Content-->
        <div id="content">
            <!-- Begin Content Menu Column -->
            <div id="content-left">
                <select id="pic-list" style="margin-left:10px; width:160px"
                              size="20" onchange="displayImage(this);">
    <!--- **** List of picture files goes here **** -->
    $pictures
    <!--- **** End list of picture files **** -->
                </select>
            </div>
            <!-- Begin Content Column -->
            <div id="content-right"> 
            <p>It could take some time for the image to load, please be 
               patient.</p>
            <img id="main-picture" width="400" border="0" />
            </div>
        </div>"""

    # get the footer
    f = open(html_lib_path + 'example3-4.html', 'r')
    page_footer = f.read()
    f.close()

    # create the page template
    page_template = string.Template(page_top + page_header + page_menu_bar +
                                    page_content + page_footer + page_bottom)

    # create the substitutable content
    pagedict = dict()
    pagedict['title'] = 'Pictures'
    pagedict['titleleft'] = 'Pictures'
    pagedict['main_menu'] = '<a href="/">&nbsp;Home&nbsp;</a>&nbsp;' + \
                            '<a href="/">&nbsp;Menu2&nbsp;</a>&nbsp;' + \
                            '<a href="/">&nbsp;Menu3&nbsp;</a>&nbsp;'
    # get the list of all files in the picture path
    picpath = docroot + '/book/pictures'
    files = os.listdir(picpath)
    files.sort()
    # if the file is a picture then include it in the list, otherwise skip it
    piclist = ''
    for fname in files:
        if fname.find('.jpg') >= 0:
            piclist = piclist + '            <option value="' + '/book/pictures/' + fname + '">' + fname + '</option>\n'
            continue
        if fname.find('.JPG') >= 0:
            piclist = piclist + '            <option value="' + '/book/pictures/' + fname + '">' + fname + '</option>\n'
            continue
        if fname.find('.png') >= 0:
            piclist = piclist + '            <option value="' + '/book/pictures/' + fname + '">' + fname + '</option>\n'
            continue
        if fname.find('.PNG') >= 0:
            piclist = piclist + '            <option value="' + '/book/pictures/' + fname + '">' + fname + '</option>\n'
            continue
        if fname.find('.gif') >= 0:
            piclist = piclist + '            <option value="' + '/book/pictures/' + fname + '">' + fname + '</option>\n'
            continue
        if fname.find('.GIF') >= 0:
            piclist = piclist + '            <option value="' + '/book/pictures/' + fname + '">' + fname + '</option>\n'
            continue
    pagedict['pictures'] = piclist
    asctime = time.asctime()
    parts = asctime.split()
    pagedict['year'] = parts[4]

    # make the substitutions
    html = page_template.substitute(pagedict)

    # return the substituted lines
    return html




