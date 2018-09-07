import webapp2
import jinja2
import os
from books import *
from google.appengine.api import users
from google.appengine.ext import ndb
import logging
from time import sleep



TEMPLATE = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ['jinja2.ext.autoescape'],
	autoescape = True
)



class HomePage(webapp2.RequestHandler):

	def get(self):
		print()

app = webapp2.WSGIApplication([
  ('/', HomePage),
], debug=True)
