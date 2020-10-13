from flask import Flask, render_template
from jinja2 import Template, Environment, PackageLoader, select_autoescape
import os, time

app = Flask(__name__)

def get_rows():
    rows = list()
    rows = ["DEPTNO DEPTNAME                             MGRNO  ADMRDEPT LOCATION        ",
            "------ ------------------------------------ ------ -------- ----------------",
            "A00    SPIFFY COMPUTER SERVICE DIV.         000010 A00      -",              
            "B01    PLANNING                             000020 A00      -",              
            "C01    INFORMATION CENTER                   000030 A00      -",              
            "D01    DEVELOPMENT CENTER                   -      A00      -",              
            "D11    MANUFACTURING SYSTEMS                000060 D01      -",              
            "D21    ADMINISTRATION SYSTEMS               000070 D01      -",              
            "E01    SUPPORT SERVICES                     000050 A00      -",              
            "E11    OPERATIONS                           000090 E01      -",              
            "E21    SOFTWARE SUPPORT                     000100 E01      -",              
            "F22    BRANCH OFFICE F2                     -      E01      -",              
            "G22    BRANCH OFFICE G2                     -      E01      -",              
            "H22    BRANCH OFFICE H2                     -      E01      -",              
            "I22    BRANCH OFFICE I2                     -      E01      -",              
            "J22    BRANCH OFFICE J2                     -      E01      -",
            "",
            "  14 record(s) selected."]
    return rows

@app.route('/')
def department(name=None):
    # get the document base for the html_lib directory
    (docroot, tail) = os.path.split(__file__)  # split off the file name
    (docroot, tail) = os.path.split(docroot)   # split off the first directory
    html_lib_path = docroot + '/html_lib/'

    # create the substitutable content
    pagedict = dict()
    title = 'Table Display'
    title1 = 'Department Table'
    pagedict['title'] = 'Table Display'
    titleleft = 'Department Table'
    asctime = time.asctime()
    parts = asctime.split()
    year = parts[4]
    rows = get_rows()

    # get the template and make the substitutions
    html = render_template('jinjatest2.html', rows=rows, title=title, \
                           titleleft=titleleft, title1=title1, year=year)

    # return the substituted lines
    return html
