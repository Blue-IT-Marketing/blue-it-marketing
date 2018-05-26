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

class ProjectsHomeHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/api/api.html')
        context = {}
        self.response.write(template.render(context))

    def post(self):
        vstrPath = self.request.get('vstrPath')

        if vstrPath == "sms-api":
            template = template_env.get_template('templates/api/sub/sms.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "adverts-api":
            template = template_env.get_template('templates/api/sub/adverts.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "surveys-api":
            template = template_env.get_template('templates/api/sub/surveys.html')
            context = {}
            self.response.write(template.render(context))


class ProjectsRouterHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/api/api.html')
        context = {}
        self.response.write(template.render(context))

app = webapp2.WSGIApplication([
    ('/api', ProjectsHomeHandler),
    ('/api/.*', ProjectsRouterHandler),

], debug=True)
