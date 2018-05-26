import logging
import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
import datetime

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


def VerifyAndReturnAccount(strUserID, strAccessToken):
    """
        Myoptions = {"type": "service_account",
                         "project_id": "sa-sms-b",
                         "private_key_id": "b5a2df76c2222b83893b111c41e49bdf3fb2298a",
                         "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDogYEyuGH8Dxd2\nOt11WSlWxPL7bxKZd6F26NOmVQ+vWDqlthmGPWM1zAFW4l/+600VUMKqqcjAC39W\nm2kCQp+S95WyovzyZ7u4PVEBoYrQJq1oSI1zjxCtRC/u0kqI5iYLyN7ofpJRqjnu\nUCQyu/8AstoW1M88/xwwgRUbJqZxPpbrkBHQGakm+M8Q5ZvJwQPLpPeQLRD7Xjyt\nmgbHLqDaJy1iwEo1V8ypAyS0il0rfNx7TtxTgrBUEpjt9/rPrVSdkSwExyZeFTYS\nPZo2ls24irlHQC+MKVanbSyNFeT20Z9KM/Fl2v6XpwQZFqd4tf2k3U3U7CjJ2K4A\nhi8ABWLtAgMBAAECggEADIHANr+UWxVfaGIM552+4NwB9g8o1k3ecaG0ljidJLbU\n8MpgNR24PdHrgIZM2PmZ++Y259dE5TpjxH+M9oIpnfjozzh/7XTcXtzC2W5HI/Xw\nqLC+ayjsTLsOQ6/W3TuuxZODP3O6Nd+3ngom6FO/M9prFi9RtoZCje64+UJAUcxh\n2A9ZcpQNzjUScqhmJiy+HvKYnmRx7gRuxTLi7drKgFQJUY4qptMindVuTudBVTxZ\n8/gOuUv3cCg+WBgZrWIt9BFE6g0KbZYIJWC892cI22qwPlday+h99134J75fTG03\nAXKFfdvOYO4wv7xAhgwMIn/ewGQhHANw1G0Ah0qmQQKBgQD9u5C93GxnokSCoHSr\nEWm2VDRNQXJuMhrp8QCU2xFZbswOzzjE4IUZS01ac90upRhzuuaIv/mwCLJh9hfH\nRbaPj7Z/0Oy/Vf251oqsGKcZwjaQlLWGA+wFg/7x0D2N9xjNiao4uMx42zohCLG3\nT3U3a05J7rzs99IbYw0NSsu/qwKBgQDqlWGXM1/FCI/YdwMVncuQx/HbzyLLReVx\ny5VegQADOR06DiUJbDilvY+6cjuwIqOYwKYY/zNbM8YubF63mDUTOINEXGB3sCSf\nz2L6TnHQcZ4PQUm1TSHgcliTZmRqWpn5WmAqH/z672jkYGTrWMBsF2E5U5Q1OeB1\nxYWNc1kvxwKBgFl0BA57pJhQw/iNmzQoWm2WeC34ceBZt9VcSwkvxokSH8zkz63R\nPftx6d6G1Ka6O8mpTddOXzfpiQIyYaW2dStdzkh3ns/CAEbBVXhg5KCXMOd+FhUe\nUtqK85nLAbiIMe1cqG+A7014dKDq0MTAtaGJKju0eFTO9fsDy7kw8m4rAoGBAJNl\nd2OFEUkBnzi5VwPPGWiIaaze0xL8gTXmYJ132uUrjvS6jIUGLfXeTSAuxNhge4Dw\nk60jNUa6Gm1zBHTBu5+vI7Phg2/RCsIrkhqLDbKWoWUedczogT/BOWysqq207gii\nw8fUP6YAplzRQLgsFQQWEK3vmTF0g1gc21TMxJ5jAoGBALXq/qhnQOUHUnuPs5M3\n+waHg7mJgzQt1jbClB1AVc722Lp9KSFCIhzbr3AQmHDo/eSAm9OwTTd1I4NW4vY9\nieSp/Md16NCqMXqBP6uINKuEMURAW2gGbLHDxu55EopOly+2NdgYHZbcnaeadAix\nLZoX/XlMSSgtyei0GxS9dZai\n-----END PRIVATE KEY-----\n",
                         "client_email": "firebase-adminsdk-ov6wg@sa-sms-b.iam.gserviceaccount.com",
                         "client_id": "114948598379533240849",
                         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                         "token_uri": "https://accounts.google.com/o/oauth2/token",
                         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                         "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ov6wg%40sa-sms-b.iam.gserviceaccount.com"}
            try:

                import firebase_admin

                cred = firebase_admin.credentials.Certificate(Myoptions)

                default_app = firebase_admin.initialize_app(cred)

                from firebase_admin.auth import verify_id_token
            except:
                logging.error("Credentials error")


            findRequest = Accounts.query(Accounts.strUserID == strUserID)
            thisAccountList = findRequest.fetch()
            if len(thisAccountList) > 0:
                thisAccount = thisAccountList[0]

                try:
                    decode_token = verify_id_token(id_token=strAccessToken,app=default_app)
                    uid = decode_token['uid']
                except:
                    uid = None

                if (uid != None) and (uid == strUserID):
                    return thisAccount
                else:
                    return None  # Once firebase credentials is working properly then we should return none here
            else:
                return None

    """




    findRequest = Accounts.query(Accounts.strUserID == strUserID)
    thisAccountList = findRequest.fetch()
    if len(thisAccountList) > 0:
        thisAccount = thisAccountList[0]
        return thisAccount
    else:
        return None


class Accounts(ndb.Expando):

    strUserID = ndb.StringProperty()
    strCompanyID = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebsite = ndb.StringProperty()
    strVerified = ndb.BooleanProperty(default=False)
    strVerificationCode = ndb.StringProperty()
    strSuspended = ndb.BooleanProperty(default=False)

    strPhotoURL = ndb.StringProperty()
    strProviderData = ndb.StringProperty()
    strAccessToken = ndb.StringProperty()

    strLastSignInDate = ndb.DateProperty()
    strLastSignInTime = ndb.TimeProperty()

    def writeLastSignInDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strLastSignInDate = strinput
                return True
            else:
                return False
        except:
            return False

    def writeLastSignInTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strLastSignInTime = strinput
                return True
            else:
                return False
        except:
            return False

    def writePhotoURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPhotoURL = strinput
                return True
            else:
                return False
        except:
            return False

    def writeProviderData(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProviderData = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccessToken(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccessToken = strinput
                return True
            else:
                return False
        except:
            return False

    def writeVerified(self,strinput):
        try:
            if strinput in [True,False]:
                self.strVerified = strinput
                return True
            else:
                return False

        except:
            return False
    def writeVerificationCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strVerificationCode = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateVerificationCode(self):
        import random, string
        try:
            strVerificationCode = ""
            for i in range(6):
                strVerificationCode += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strVerificationCode
        except:
            return None
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

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/login.html')
        context = {}
        self.response.write(template.render(context))

    def post(self):
        """
            Create accout information here
        :return:
        """
        from hireus import Company,CompanyContacts
        vstrPath = self.request.get('vstrPath')

        if vstrPath == "login-details":
            vstrDisplayName = self.request.get('vstrDisplayName')
            vstrEmail = self.request.get('vstrEmail')
            vstrEmailVerified = self.request.get('vstremailVerified')
            vstrUserID = self.request.get('vstrUserID')
            vstrPhoneNumber = self.request.get('vstrPhoneNumber')
            vstrProviderData = self.request.get('vstrProviderData')
            vstrAccessToken = self.request.get('vstrAccessToken')

            findRequest = Accounts.query(Accounts.strUserID == vstrUserID)
            thisAccountsList = findRequest.fetch()
            if len(thisAccountsList) > 0:
                thisAccount = thisAccountsList[0]

            else:
                thisCompany = Company()
                thisContant = CompanyContacts()
                thisCompany.writeUserID(strinput=vstrUserID)
                thisCompany.writeCompanyID(strinput=thisCompany.CreateCompanyID())

                thisContant.writeCompanyID(strinput=thisCompany.strCompanyID)
                thisContant.writeCell(strinput=vstrPhoneNumber)
                thisContant.writeEmail(strinput=vstrEmail)
                if " " in vstrDisplayName:
                    vstrNamesList = vstrDisplayName.split(" ")
                    thisContant.writeName(strinput=vstrNamesList[0])
                    thisContant.writeSurname(strinput=vstrNamesList[1])
                else:
                    thisContant.writeName(vstrDisplayName)
                thisAccount = Accounts()
                thisAccount.writeNames(strinput=vstrDisplayName)
                thisAccount.writeAccessToken(strinput=vstrAccessToken)
                thisAccount.writeEmail(strinput=vstrEmail)
                thisAccount.writeUserID(strinput=vstrUserID)
                thisAccount.writeCell(strinput=vstrPhoneNumber)
                thisAccount.writeProviderData(strinput=vstrProviderData)
                if vstrEmailVerified == "YES":
                    thisAccount.writeVerified(strinput=True)
                else:
                    thisAccount.writeVerified(strinput=False)
                thisAccount.writeCompanyID(strinput=thisCompany.strCompanyID)
                thisCompany.put()
                thisAccount.put()
                thisContant.put()

class LogoutHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/logout.html')
        context = {}
        self.response.write(template.render(context))


app = webapp2.WSGIApplication([

    ('/login', LoginHandler),
    ('/logout', LogoutHandler)
], debug=True)