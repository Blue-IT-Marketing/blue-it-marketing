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


#   Client Records, Project Records, Payments Records, Auto Reminders
#
#
#
#
#
#
#
#
#
#
#
#
#
#

class Company(ndb.Expando):
    strUserID = ndb.StringProperty()
    strCompanyID = ndb.StringProperty()
    strCompanyName = ndb.StringProperty()
    strCompanyDescription = ndb.StringProperty()
    strCountry = ndb.StringProperty()
    strCity = ndb.StringProperty()
    strAddress = ndb.StringProperty()
    strWebsite = ndb.StringProperty()
    strServicesProducts = ndb.StringProperty()

    def writeServiceProducts(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strServicesProducts = strinput
                return True
            else:
                return False
        except:
            return False

    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateCompanyID(self):
        import random,string
        try:
            strCompanyID = ""
            for i in range(32):
                strCompanyID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strCompanyID
        except:
            return None

    def writeCompanyID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCompanyID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCompanyName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCompanyName  = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCompanyDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCompanyDescription = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCountry(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCountry = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCity(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCity = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAddress = strinput
                return True
            else:
                return False
        except:
            return False
    def writeWebsite(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strWebsite = strinput
                return True
            else:
                return False
        except:
            return False

class CompanyContacts(ndb.Expando):
    strCompanyID = ndb.StringProperty()
    strName = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()

    def writeCompanyID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCompanyID = strinput
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
    def writeEmail(self,strinput):
        try:
            strinput  = str(strinput)
            if strinput != None:
                self.strEmail = strinput
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

    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTel = strinput
                return True
            else:
                return False

        except:
            return False

class Projects(ndb.Expando):
    strSeparator = ndb.StringProperty(default="|")
    strCompanyID = ndb.StringProperty()
    strProjectID = ndb.StringProperty()
    strProjectTitle = ndb.StringProperty()
    strProjectDetails = ndb.StringProperty()

    strDateCreated = ndb.DateProperty()
    strTimeCreated = ndb.TimeProperty()
    strETADate = ndb.DateProperty()
    strEstBudget = ndb.IntegerProperty(default=0)
    strTotalCharged = ndb.IntegerProperty(default=0)
    strProjectStatus = ndb.StringProperty(default="Created") # Active , Completed
    strTotalPaid = ndb.IntegerProperty(default=0)

    def writeTotalPaid(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalPaid = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeEstBudget(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strEstBudget = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeTotalCharged(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalCharged = int(strinput)
                return True
            else:
                return False
        except:
            return False


    def writeCompanyID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCompanyID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeProjectID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProjectID = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateProjectID(self):
        import random,string
        try:
            strProjectID = ""
            for i in range(32):
                strProjectID  += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strProjectID
        except:
            return None

    def writeProjectTitle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProjectTitle = strinput
                return True
            else:
                return False
        except:
            return False

    def writeProjectDetails(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProjectDetails = strinput
                return True
            else:
                return False
        except:
            return False






    def writeDateCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def writeETADate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strETADate = strinput
                return True
            else:
                return False
        except:
            return False

    def writeProjectStatus(self,strinput):
        """
            #TODO - finalize all project status
        :param strinput:
        :return:
        """
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProjectStatus = strinput
                return True
            else:
                return False
        except:
            return False

class ProjectFiles(ndb.Expando):
    strUserID  = ndb.StringProperty()
    strProjectID = ndb.StringProperty()
    strFileName = ndb.StringProperty()
    strDescription = ndb.StringProperty()
    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()

    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeProjectID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProjectID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFileName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFileName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDescription = strinput
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

class ProjectChat(ndb.Expando):
    strProjectID = ndb.StringProperty()
    strMessage = ndb.StringProperty()
    strTimeStamp = ndb.DateTimeProperty()
    strIsClient = ndb.BooleanProperty(default=True)
    strFileName = ndb.StringProperty()

    def writeProjectID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProjectID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMessage(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMessage = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeStamp(self,strinput):
        try:
            if strinput != None:
                self.strTimeStamp = strinput
                return True
            else:
                return False
        except:
            return False
    def writeIsClient(self,strinput):
        try:
            if strinput in [True,False]:
                self.strIsClient = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFileName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFileName = strinput
                return True
            else:
                return False
        except:
            return False

class Payments(ndb.Expando):
    strUserID = ndb.StringProperty()
    strProjectID = ndb.StringProperty()
    strProjectTitle = ndb.StringProperty()
    strInvoice = ndb.StringProperty()

    strTotalInvoiced = ndb.IntegerProperty(default=0)
    strTotalPaid = ndb.IntegerProperty(default=0)

    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()

    def writeProjectID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProjectID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeProjectTitle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProjectTitle = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateInvoiceNumber(self):
        import random,string
        try:
            strInvoice = ""
            for i in range(9):
                strInvoice += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strInvoice
        except:
            return None

    def writeInvoiceNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strInvoice = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTotalInvoiced(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalInvoiced = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeTotalPaid(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalPaid = int(strinput)
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


class HireUsHandler(webapp2.RequestHandler):
    def read_file(self, filename):
        import cloudstorage as gcs
        from google.appengine.api import app_identity
        bucket_name = os.environ.get('BUCKET_NAME',app_identity.get_default_gcs_bucket_name())

        self.response.write('Reading the full file contents:\n')
        filename ="/"+ bucket_name + "/" + filename
        with gcs.open(filename) as cloudstorage_file:
            filecontents = cloudstorage_file.read()

        gcs.close()
        return filecontents

    def get(self):
        template = template_env.get_template('templates/hireus/hireus.html')
        context = {}
        self.response.write(template.render(context))

    def post(self):
        from accounts import Accounts,VerifyAndReturnAccount
        from datetime import timedelta


        vstrPath = self.request.get('vstrPath')

        if vstrPath == "company-details":
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            findRequest = Accounts.query(Accounts.strUserID == vstrUserID)
            thisAccountList = findRequest.fetch()

            if len(thisAccountList) > 0:
                thisAccount = thisAccountList[0]

                findRequest = Company.query(Company.strCompanyID == thisAccount.strCompanyID)
                thisCompanyList = findRequest.fetch()

                if len(thisCompanyList) > 0:
                    thisCompany = thisCompanyList[0]
                else:
                    thisCompany = Company()

                findRequest = CompanyContacts.query(CompanyContacts.strCompanyID == thisAccount.strCompanyID)
                thisContactsList = findRequest.fetch()

                if len(thisContactsList) > 0:
                    thisContact = thisContactsList[0]
                else:
                    thisContact = CompanyContacts()

                template = template_env.get_template('templates/hireus/sub/company-details.html')
                context = {'thisCompany':thisCompany,'thisContact':thisContact}
                self.response.write(template.render(context))
            else:
                thisCompany = Company()
                thisContact = CompanyContacts()
                template = template_env.get_template('templates/hireus/sub/company-details.html')
                context = {'thisCompany':thisCompany,'thisContact':thisContact}
                self.response.write(template.render(context))

        elif vstrPath == "update-company-details":
            vstrEmail = self.request.get('vstrEmail')
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrCompanyName = self.request.get('vstrCompanyName')
            vstrCompanyDescription = self.request.get('vstrCompanyDescription')
            vstrCountry = self.request.get('vstrCountry')
            vstrCity = self.request.get('vstrCity')
            vstrAddress = self.request.get('vstrAddress')
            vstrWebsite = self.request.get('vstrWebsite')
            vstrName = self.request.get('vstrName')
            vstrSurname = self.request.get('vstrSurname')
            vstrEmail = self.request.get('vstrEmail')
            vstrCell = self.request.get('vstrCell')
            vstrServicesProducts = self.request.get('vstrServicesProducts')

            findRequest = Accounts.query(Accounts.strUserID == vstrUserID)
            thisAccountList = findRequest.fetch()

            if len(thisAccountList) > 0:
                thisAccount = thisAccountList[0]

                findRequest = Company.query(Company.strCompanyID == thisAccount.strCompanyID)
                thisCompanyList = findRequest.fetch()

                if len(thisCompanyList) > 0:
                    thisCompany = thisCompanyList[0]
                else:
                    thisCompany = Company()


                findRequest = CompanyContacts.query(CompanyContacts.strCompanyID == thisAccount.strCompanyID)
                thisContactsList = findRequest.fetch()

                if len(thisContactsList) > 0:
                    thisContact = thisContactsList[0]
                else:
                    thisContact = CompanyContacts()

                thisCompany.writeCompanyName(strinput=vstrCompanyName)
                thisCompany.writeCompanyDescription(strinput=vstrCompanyDescription)
                thisCompany.writeCountry(strinput=vstrCountry)
                thisCompany.writeCity(strinput=vstrCity)
                thisCompany.writeAddress(strinput=vstrAddress)
                thisCompany.writeWebsite(strinput=vstrWebsite)
                thisCompany.writeServiceProducts(strinput=vstrServicesProducts)
                thisCompany.put()

                thisContact.writeName(strinput=vstrName)
                thisContact.writeSurname(strinput=vstrSurname)
                thisContact.writeEmail(strinput=vstrEmail)
                thisContact.writeCell(strinput=vstrCell)
                thisContact.put()

                self.response.write('Company Details Updated')

        elif vstrPath == "my-projects":
            vstrEmail = self.request.get('vstrEmail')
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if thisAccount != None:
                findRequest = Projects.query(Projects.strCompanyID == thisAccount.strCompanyID)
                thisProjectList = findRequest.fetch()
            else:
                thisProjectList = []

            template = template_env.get_template('templates/hireus/sub/my-projects.html')
            context = {'thisProjectList':thisProjectList}
            self.response.write(template.render(context))

        elif vstrPath == "create-project":
            vstrEmail = self.request.get('vstrEmail')
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if thisAccount != None:

                vstrProjectTitle = self.request.get('vstrProjectTitle')
                vstrProjectDetails = self.request.get('vstrProjectDetails')
                vstrBudget = self.request.get('vstrBudget')
                vstrExpectedDateOfDelivery = self.request.get('vstrExpectedDateOfDelivery')

                vstrThisDateTime = datetime.datetime.now()
                strThisDate = datetime.date(year=vstrThisDateTime.year,month=vstrThisDateTime.month,day=vstrThisDateTime.day)
                strThisTime = datetime.time(hour=vstrThisDateTime.hour,minute=vstrThisDateTime.minute,second=vstrThisDateTime.second)


                vstrTotalWeeks = int(vstrExpectedDateOfDelivery)
                #TODO- Add the total weeks in days
                vstrTotalDays = vstrTotalWeeks * 7
                #TODO timedelta add days
                ETADate = vstrThisDateTime + timedelta(days=vstrTotalDays)


                thisProject = Projects()
                thisProject.writeDateCreated(strinput=strThisDate)
                thisProject.writeTimeCreated(strinput=strThisTime)

                thisProject.writeProjectTitle(strinput=vstrProjectTitle)
                thisProject.writeProjectDetails(strinput=vstrProjectDetails)
                thisProject.writeETADate(strinput=ETADate.date())
                thisProject.writeProjectStatus(strinput="Created")
                thisProject.writeProjectID(strinput=thisProject.CreateProjectID())
                thisProject.writeCompanyID(strinput=thisAccount.strCompanyID)
                thisProject.writeEstBudget(strinput=vstrBudget)
                thisProject.put()
                self.response.write("Project Successfully created")
            else:
                self.response.write("Please login to create a project")


        elif vstrPath == "payment-details":
            vstrEmail = self.request.get('vstrEmail')
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')

            #TODO - find the account details

            thisAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if thisAccount != None:

                findRequest = Payments.query()

                findRequest = Projects.query(Projects.strTotalPaid < Projects.strTotalCharged)
                thisProjectList = findRequest.fetch()

                findRequest = Payments.query(Payments.strUserID == vstrUserID)
                thisPaymentsList = findRequest.fetch()

            else:
                thisProjectList = []
                thisPaymentsList = []




            template = template_env.get_template('templates/hireus/sub/payment-details.html')
            context = {'thisProjectList':thisProjectList,'thisPaymentsList':thisPaymentsList}
            self.response.write(template.render(context))


        elif vstrPath == "client-manager-project-details":

            vstrProjectID = self.request.get('vstrProjectID')

            findRequest = Projects.query(Projects.strProjectID == vstrProjectID)
            thisProjectDetailsList = findRequest.fetch()

            if len(thisProjectDetailsList) > 0:
                thisProject = thisProjectDetailsList[0]
            else:
                thisProject = Projects()

            template = template_env.get_template('templates/hireus/sub/client-manager-project-details.html')
            context = {'thisProject':thisProject}
            self.response.write(template.render(context))

        elif vstrPath == "client-manager-update-project-details":
            vstrProjectDetails = self.request.get('vstrProjectDetails')
            vstrProjectID = self.request.get('vstrProjectID')
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if thisAccount != None:

                findRequest = Projects.query(Projects.strProjectID == vstrProjectID)
                thisProjectList = findRequest.fetch()
                if len(thisProjectList) > 0:
                    thisProject = thisProjectList[0]
                else:
                    thisProject = Projects()

                thisProject.writeProjectDetails(strinput=vstrProjectDetails)
                thisProject.put()
                self.response.write("Project Details Successfully updated")
            else:
                self.response.write("Cannot update project details account not found")



        elif vstrPath == "client-manager-project-progress":
            vstrEmail = self.request.get('vstrEmail')
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')
            vstrProjectID = self.request.get('vstrProjectID')

            thisAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if thisAccount != None:
                findRequest = Projects.query(Projects.strProjectID == vstrProjectID)
                thisProjectList = findRequest.fetch()

                if len(thisProjectList) > 0:
                    thisProject = thisProjectList[0]
                else:
                    thisProject = Projects()

                findRequest = ProjectChat.query(ProjectChat.strProjectID == thisProject.strProjectID)
                thisChatMessagesList = findRequest.fetch()

                template = template_env.get_template('templates/hireus/sub/client-manager-project-progress.html')
                context = {'thisProject':thisProject,'thisChatMessagesList':thisChatMessagesList}
                self.response.write(template.render(context))
            else:
                thisProject = Projects()
                template = template_env.get_template('templates/hireus/sub/client-manager-project-progress.html')
                context = {'thisProject':thisProject}
                self.response.write(template.render(context))

        elif vstrPath == "client-manager-project-files":
            vstrEmail = self.request.get('vstrEmail')
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')
            vstrProjectID = self.request.get('vstrProjectID')

            thisAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if thisAccount != None:
                findRequest = Projects.query(Projects.strProjectID == vstrProjectID)
                thisProjectList = findRequest.fetch()

                if len(thisProjectList) > 0:
                    thisProject = thisProjectList[0]
                else:
                    thisProject = Projects()

                findRequest = ProjectFiles.query(ProjectFiles.strProjectID == thisProject.strProjectID)
                thisProfilesList = findRequest.fetch()

                template = template_env.get_template('templates/hireus/sub/client-manager-project-files.html')
                context = {'thisProject':thisProject,'thisProfilesList':thisProfilesList}
                self.response.write(template.render(context))
            else:
                thisProject = Projects()
                template = template_env.get_template('templates/hireus/sub/client-manager-project-files.html')
                context = {'thisProject':thisProject}
                self.response.write(template.render(context))

        elif vstrPath == "client-manager-upload-files":
            vstrFilename = self.request.get('vstrFileName')
            vstrFileDescription = self.request.get('vstrFileDescription')
            vstrProjectID = self.request.get('vstrProjectID')
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken =  self.request.get('vstrAccessToken')



            vstrThisDateTime = datetime.datetime.now()
            vstrThisDate = vstrThisDateTime.date()
            vstrThisTime = vstrThisDateTime.time()


            MyFileManager = ProjectFiles()
            MyFileManager.writeFileName(strinput=vstrFilename)
            MyFileManager.writeProjectID(strinput=vstrProjectID)
            MyFileManager.writeUserID(strinput=vstrUserID)
            MyFileManager.writeDescription(strinput=vstrFileDescription)
            MyFileManager.writeDate(strinput=vstrThisDate)
            MyFileManager.writeTime(strinput=vstrThisTime)
            MyFileManager.put()
            self.response.write("file successfully uploaded " + vstrFilename)

        elif vstrPath == "client-manager-download-file":
            self.response.headers['Content-Type'] = "blue-it-marketing-downloads"
            self.response.write(self.read_file(filename=self.request.get('vstrFileName')))


        elif vstrPath == "progress-chat":
            vstrPath = self.request.get('vstrPath')
            vstrMessage = self.request.get('vstrMessage')
            vstrProjectID = self.request.get('vstrProjectID')
            vstrUserName = self.request.get('vstrUserName')
            vstrEmail = self.request.get('vstrEmail')
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')


            thisAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if thisAccount != None:
                thisProjectChat = ProjectChat()
                thisProjectChat.writeProjectID(strinput=vstrProjectID)
                thisProjectChat.writeMessage(strinput=vstrMessage)
                thisProjectChat.writeIsClient(strinput=True)
                thisProjectChat.writeTimeStamp(strinput=datetime.datetime.now())
                thisProjectChat.put()

                findRequest = ProjectChat.query(ProjectChat.strProjectID == vstrProjectID)
                thisChatMessagesList = findRequest.fetch()

                template = template_env.get_template('templates/hireus/sub/chat.html')
                context = {'thisChatMessagesList':thisChatMessagesList}
                self.response.write(template.render(context))




class ThisProjectManager(webapp2.RequestHandler):
    def get(self):

        URL =self.request.url
        strURLlist = URL.split("/")

        strProjectID = strURLlist[len(strURLlist) - 1]

        findRequest = Projects.query(Projects.strProjectID == strProjectID)
        thisProjectList = findRequest.fetch()

        if len(thisProjectList) > 0:
            thisProject = thisProjectList[0]

            template = template_env.get_template('templates/hireus/sub/client-project-manager.html')
            context = {'thisProject':thisProject}
            self.response.write(template.render(context))


app = webapp2.WSGIApplication([
    ('/hireus', HireUsHandler),
    ('/hireus/manager/.*', ThisProjectManager)

], debug=True)

