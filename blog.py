#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
import logging
import datetime
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class Post(ndb.Expando):
    strPostReference = ndb.StringProperty()
    strPostHeading = ndb.StringProperty()
    strPostBody = ndb.TextProperty()
    strAuthor = ndb.StringProperty()

    strSnippet = ndb.StringProperty()

    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()

    strPublished = ndb.BooleanProperty(default=False)

    strCommentIDList = ndb.StringProperty()

    def writePublished(self,strinput):
        try:
            if strinput in [True,False]:
                self.strPublished = strinput
                return True
            else:
                return False
        except:
            return False

    def writePostReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPostReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writePostHeading(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPostHeading = strinput
                return True
            else:
                return False
        except:
            return False

    def writePostBody(self,strinput):
        try:

            if strinput != None:
                self.strPostBody = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAuthor(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAuthor = strinput
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

    def writeSnippet(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSnippet = strinput
                return True
            else:
                return False
        except:
            return False

    def CreatePostReference(self):
        import random,string
        try:
            strPostReference = ""
            for i in range(12):
                strPostReference += random.SystemRandom().choice(string.digits + string.ascii_lowercase)

            return strPostReference
        except:
            return None

    def AddCommentID(self,strinput):
        try:
            strinput = str(strinput)
            tempString = str(self.strCommentIDList)

            if tempString != None:
                MyList = tempString.split("|")
            else:
                MyList = []

            tempString = ""

            logging.info("Ok inside here is Comment ID  = " + strinput)
            if strinput != None:
                MyList = MyList.append(strinput)
                logging.info("Appending a comment ID into post : " + strinput)
            else:
                MyList = []

            for Comment in MyList:
                if tempString == "":
                    tempString = Comment
                    logging.info("Added Comment " + Comment)
                else:
                    tempString = tempString + "|" + Comment

            self.strCommentIDList = tempString
            return True
        except:
            return False


class PostComments(ndb.Expando):
    strCommentID = ndb.StringProperty()
    strComment = ndb.StringProperty()
    strDate = ndb.DateProperty()
    strTime = ndb.DateProperty()
    strUserID = ndb.StringProperty()
    strName = ndb.StringProperty()

    def writeCommentID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCommentID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateCommentID(self):
        try:
            import string,random
            strCommentID = ""
            for i in range(32):
                strCommentID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strCommentID
        except:
            return None
    def writeComment(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strComment = strinput
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


class BlogHandler(webapp2.RequestHandler):
    def get(self):

        findRequest = Post.query(Post.strPublished == True)
        thisPostsList = findRequest.fetch()

        if len(thisPostsList) > 0:
            thisPost = thisPostsList[0]
        else:
            thisPost = Post()


        template = template_env.get_template('templates/blog/blog.html')
        context = {'thisPostsList':thisPostsList,'thisPost':thisPost}
        self.response.write(template.render(context))

    def post(self):

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            template = template_env.get_template('templates/dashboard/blog/blog.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrChoice == "1":
            vstrHeading = self.request.get('vstrHeading')
            vstrIntroduction = self.request.get('vstrIntroduction')
            vstrBody = self.request.get('vstrBody')

            vstrThisDateTime = datetime.datetime.now()
            strThisDate = datetime.date(year=vstrThisDateTime.year,month=vstrThisDateTime.month,day=vstrThisDateTime.day)
            strThisTime = datetime.time(hour=vstrThisDateTime.hour,minute=vstrThisDateTime.minute,second=vstrThisDateTime.second)

            thisPost = Post()
            thisPost.writePostHeading(strinput=vstrHeading)
            thisPost.writePostBody(strinput=vstrBody)
            thisPost.writeSnippet(strinput=vstrIntroduction)
            thisPost.writeAuthor(strinput="Justice Ndou")
            thisPost.writeDate(strinput=strThisDate)
            thisPost.writeTime(strinput=strThisTime)
            thisPost.writePublished(strinput=True)
            thisPost.writePostReference(strinput=thisPost.CreatePostReference())
            thisPost.put()
            self.response.write("Blog Post Successfully updated")

        elif vstrChoice == "2":
            template = template_env.get_template('templates/blog/guest/guest.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrChoice == "3":
            vstrTitle = self.request.get('vstrTitle')
            vstrArticleEditor = self.request.get('vstrArticleEditor')
            vstrIntroduction = self.request.get('vstrIntroduction')

            thisPost = Post()
            thisPost.writePostHeading(strinput=vstrTitle)
            thisPost.writeSnippet(strinput=vstrIntroduction)
            thisPost.writePostBody(strinput=vstrArticleEditor)
            thisPost.writePostReference(strinput=thisPost.CreatePostReference())
            thisPost.writePublished(strinput=True)
            vstrThisDateTime = datetime.datetime.now()
            vstrThisDate = vstrThisDateTime.date()
            vstrThisTime = datetime.time(hour=vstrThisDateTime.hour,minute=vstrThisDateTime.minute,second=vstrThisDateTime.second)

            thisPost.writeDate(strinput=vstrThisDate)
            thisPost.writeTime(strinput=vstrThisTime)
            thisPost.writeAuthor(strinput="Guest")
            #TODO- we can also make it possible for the author to be the loggedin user
            thisPost.put()
            self.response.write("Successfully created a new post")

        elif vstrChoice == "create-comment":
            vstrPostReference = self.request.get('vstrPostReference')
            vstrMyComment = self.request.get('vstrMyComment')

            findRequest = Post.query(Post.strPostReference == vstrPostReference)
            thisPostList = findRequest.fetch()
            if len(thisPostList) > 0:
                thisPost = thisPostList[0]
            else:
                thisPost = Post()

            vstrThisDate = datetime.datetime.now()
            strThisDate = datetime.date(year=vstrThisDate.year,month=vstrThisDate.month,day=vstrThisDate.day)
            strThisTime = datetime.time(hour=vstrThisDate.hour,minute=vstrThisDate.minute,second=vstrThisDate.second)
            thisComment = PostComments()
            #TODO- Please add userid here
            thisComment.writeComment(strinput=vstrMyComment)
            thisComment.writeDate(strinput=strThisDate)
            thisComment.writeTime(strinput=strThisTime)
            thisComment.writeCommentID(strinput=thisComment.CreateCommentID())

            thisPost.AddCommentID(strinput=thisComment.strCommentID)
            thisPost.put()
            thisComment.put()
            self.response.write(vstrMyComment)


class ThisBlogHandler(webapp2.RequestHandler):
    def get(self):
        URL = self.request.url
        strURLList = URL.split("/")
        strPostReference = strURLList[len(strURLList) - 1]

        findRequest = Post.query(Post.strPostReference == strPostReference)
        thisPostList = findRequest.fetch()

        if len(thisPostList) > 0:
            thisPost = thisPostList[0]
        else:
            thisPost = Post()

        logging.info("Are we even here ? >>>>>>>>>>")

        MyCommentList = []
        strCommentList = thisPost.strCommentIDList.split("|")
        logging.info(strCommentList)
        for thisCommentID in strCommentList:
            findRequest = PostComments.query(PostComments.strCommentID == thisCommentID)
            thisCommentList = findRequest.fetch()
            if len(thisCommentList) > 0:
                MyCommentList = MyCommentList.append(thisCommentList[0])
                logging.info("Comments are being found")
            else:
                logging.info("Not comment found with this Comment ID : " + thisCommentID)

        template = template_env.get_template('templates/blog/posts/post.html')
        context = {'thisPost':thisPost,'thisCommentsList': MyCommentList}
        self.response.write(template.render(context))

    def post(self):
        vstrChoice = self.request.get("vstrChoice")

        if vstrChoice == "0":
            vstrArticleID = self.request.get('vstrarticleID')

            findRequest = Post.query(Post.strPostReference == vstrArticleID)
            thisPostList = findRequest.fetch()

            if len(thisPostList) > 0:
                thisPost = thisPostList[0]
            else:
                thisPost = Post()

            logging.info("Are we even here ? >>>>>>>>>>")

            MyCommentList = []
            if thisPost.strCommentIDList != None:
                strTempList = str(thisPost.strCommentIDList)
                logging.info("MY COMMENT LIST SO FAR : " + strTempList)
                strCommentList = strTempList.split("|")
                for thisCommentID in strCommentList:
                    thisCommentID = thisCommentID.strip()
                    findRequest = PostComments.query(PostComments.strCommentID == thisCommentID)
                    thisCommentList = findRequest.fetch()
                    if len(thisCommentList) > 0:
                        MyCommentList.append(thisCommentList[0])
                        logging.info("Comments are being found")
                    else:
                        logging.info("Not comment found with this Comment ID : " + thisCommentID)

            template = template_env.get_template('templates/blog/posts/post-snippet.html')
            context = {'thisPost':thisPost,'thisCommentsList': MyCommentList}
            self.response.write(template.render(context))


app = webapp2.WSGIApplication([
    ('/blog', BlogHandler),
    ('/blog/.*', ThisBlogHandler)

], debug=True)