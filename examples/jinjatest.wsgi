import logging
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/pub/www/holmes4/docroot/wsgitest/')
from jinjatest import app as application
application.secret_key = 'jinja test on apache 2.4'
