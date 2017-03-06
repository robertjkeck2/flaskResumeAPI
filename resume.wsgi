#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/api.robertjohnkeck.com/")

from resume import app as application
application.secret_key = 'johnsresume'
