import os
import webapp2
import jinja2,datetime
from google.appengine.ext import ndb

import logging
#Jinja Loader

template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))



class Subscribers(ndb.Expando):
    strSubscriberID = ndb.StringProperty()
    strName = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()


    def CreateSubscriberID(self):
        import random,string
        try:
            strSubscriberID = ""
            for i in range(126):
                strSubscriberID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strSubscriberID
        except:
            return None

    def writeSubscriberID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSubscriberID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strName = strinput
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


class NewslettersHandler(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        vstrPath = self.request.get('vstrPath')

        if vstrPath == "subscribe":

            vstrName = self.request.get('vstrName')
            vstrSurname = self.request.get('vstrSurname')
            vstrCell = self.request.get('vstrCell')
            vstrEmail = self.request.get('vstrEmail')

            thisSubscriber = Subscribers()
            thisSubscriber.writeName(strinput=vstrName)
            thisSubscriber.writeSurname(strinput=vstrSurname)
            thisSubscriber.writeCell(strinput=vstrCell)
            thisSubscriber.writeEmail(strinput=vstrEmail)

            vstrThisDateTime = datetime.datetime.now()
            strThisDate = vstrThisDateTime.date()
            strThisTime = vstrThisDateTime.time()

            thisSubscriber.writeDate(strinput=strThisDate)
            thisSubscriber.writeTime(strinput=strThisTime)
            thisSubscriber.writeSubscriberID(strinput=thisSubscriber.CreateSubscriberID())
            thisSubscriber.put()
            self.response.write("Newsletter Subscription Successful")



app = webapp2.WSGIApplication([
    ('/newsletters', NewslettersHandler)
], debug=True)
