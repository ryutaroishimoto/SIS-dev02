# -*- coding: utf-8 -*-
import cgi
import os
import sys
import cgi
import os
import datetime os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from google.appengine.dist import use_library use_library('django', '1.2')
from django.conf import settings _ = settings.TEMPLATE_DIRS
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from google.appengine.api import users 
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import urlfetch
from google.appengine.api import memcache
from google.appengine.api.datastore_errors import Timeout
from google.appengine.api import taskqueue
from google.appengine.api import mail
from google.appengine.api import images
sys.path.append('lib')
sys.path.append('vendor')
from django.utils import simplejson
from HTMLParser import HTMLParser
import xml.sax.saxutils
import yaml
import urllib 
from urllib import quote
from urllib import unquote
import re
import random
import math
import urlparse
import types
import md5
