import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class EssayPage(webapp2.RequestHandler):
    """ """ 
    def get(self):
        """ """
        essay_id = self.request.get("id")
        template = JINJA_ENVIRONMENT.get_template('essay/'+str(essay_id)+'.html')
        self.response.write(template.render({   }))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/essay', EssayPage),
], debug=True)