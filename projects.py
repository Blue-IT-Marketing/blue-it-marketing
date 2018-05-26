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
import datetime
#Jinja Loader
import logging
template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))


class ProjectFeatures(ndb.Expando):
    strProjectName = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebApp = ndb.StringProperty()
    strSuggestedFeature = ndb.StringProperty()
    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()

    def writeNames(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNames = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurname(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurname = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False

    def writeWebApp(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strWebApp = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSuggestedFeature(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSuggestedFeature = strinput
                return True
            else:
                return False
        except:
            return False


    def writeDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDate = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTime = strinput
                return True
            else:
                return False
        except:
            return False

class BugReports(ndb.Expando):
    strProjectName = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebApp = ndb.StringProperty()
    strBugDescription = ndb.StringProperty()
    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()

    def writeProjectName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProjectName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNames(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNames = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurname(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurname = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False
    def writeWebApp(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strWebApp = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBugDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBugDescription = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTime = strinput
                return True
            else:
                return False
        except:
            return False

class ProjectsHomeHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/projects/projects.html')
        context = {}
        self.response.write(template.render(context))

    def post(self):

        vstrPath = self.request.get('vstrPath')

        if vstrPath == "church-admin":
            template = template_env.get_template('templates/projects/projects/churchadmin/project.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "cover-manager":
            template = template_env.get_template('templates/projects/projects/cover-manager/project.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "hotel-manager":
            template = template_env.get_template('templates/projects/projects/hotel-manager/project.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "sms-messaging":
            template = template_env.get_template('templates/projects/projects/sms-messaging/project.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "hr-systems":
            template = template_env.get_template('templates/projects/projects/hr-systems/project.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "school-management":
            template = template_env.get_template('templates/projects/projects/school-management/project.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "loans-management":
            template = template_env.get_template('templates/projects/projects/loans-management/project.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "client-trace":
            template = template_env.get_template('templates/projects/projects/client-trace/project.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "p2p-traders":
            template = template_env.get_template('templates/projects/projects/p2p-traders/project.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "job-cloud":
            template = template_env.get_template('templates/projects/projects/job-cloud/project.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "freelancing-solutions":
            template = template_env.get_template('templates/projects/projects/freelancing-solutions/project.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "bus-admin":
            template = template_env.get_template('templates/projects/projects/bus-admin/project.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrPath == "submit-feature":
            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrCell = self.request.get('vstrCell')
            vstrEmail = self.request.get('vstrEmail')
            vstrAppSelect = self.request.get('vstrAppSelect')
            vstrFeature = self.request.get('vstrFeature')

            thisProjectFeature = ProjectFeatures()
            thisProjectFeature.writeNames(strinput=vstrNames)
            thisProjectFeature.writeSurname(strinput=vstrSurname)
            thisProjectFeature.writeCell(strinput=vstrCell)
            thisProjectFeature.writeEmail(strinput=vstrEmail)
            thisProjectFeature.writeWebApp(strinput=vstrAppSelect)
            thisProjectFeature.writeSuggestedFeature(strinput=vstrFeature)
            thisProjectFeature.put()
            self.response.write("Successfully saved project feature suggestion our team will get back to you soon")

        elif vstrPath == "submit-bug":
            vstrBugNames = self.request.get('vstrBugNames')
            vstrBugSurname = self.request.get('vstrBugSurname')
            vstrBugCell = self.request.get('vstrBugCell')
            vstrBugEmail = self.request.ger('vstrBugEmail')
            vstrBugAppSelect = self.request.get('vstrBugAppSelect')
            vstrBugDescription = self.request.get('vstrBugDescription')

            thisBugReport = BugReports()
            thisBugReport.writeWebApp(strinput=vstrBugAppSelect)
            thisBugReport.writeBugDescription(strinput=vstrBugDescription)
            thisBugReport.writeNames(strinput=vstrBugNames)
            thisBugReport.writeSurname(strinput=vstrBugSurname)
            thisBugReport.writeCell(strinput=vstrBugCell)
            thisBugReport.writeEmail(strinput=vstrBugEmail)
            thisBugReport.put()
            self.response.write("Successfully saved project Bug Report")


class ProjectsRouterHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/projects/projects.html')
        context = {}
        self.response.write(template.render(context))

app = webapp2.WSGIApplication([
    ('/projects', ProjectsHomeHandler),
    ('/projects/.*', ProjectsRouterHandler),

], debug=True)
