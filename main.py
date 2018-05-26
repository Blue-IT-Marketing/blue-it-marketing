#!/usr/bin/env python

# Copyright 2007 Google Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users

#Jinja Loader
import logging
template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))



class MainHandler(webapp2.RequestHandler): # Loading the Main App Window
    def get(self):
        template = template_env.get_template('templates/index.html')
        context = {}
        self.response.write(template.render(context))


    def post(self):
        pass



class FAQHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/faq.html')
        context = {}
        self.response.write(template.render(context))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template("templates/about.html")
        context = {}
        self.response.write(template.render(context))


class TermsHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/terms.html')
        context = {}
        self.response.write(template.render(context))
class PrivacyHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/privacy.html')
        context = {}
        self.response.write(template.render(context))

class SitemapHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/sitemap/sitemap.xml')
        context = {}
        self.response.headers["Content-Type"] = 'text/xml'
        self.response.write(template.render(context))

class RobotsHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/sitemap/robots.txt')
        context = {}
        self.response.headers["Content-Type"] = "text/plain"
        self.response.write(template.render(context))

class CatchAllHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/index.html')
        context = {}
        self.response.write(template.render(context))



app = webapp2.WSGIApplication([

    ('/', MainHandler),
    ('/faq', FAQHandler),
    ('/about', AboutHandler),
    ('/terms', TermsHandler),
    ('/privacy', PrivacyHandler),
    ('/sitemap.xml', SitemapHandler),
    ('/robots.txt', RobotsHandler),
    ('/.*', CatchAllHandler)
], debug=True)
