# coding=utf-8

import webapp2
from jinja import render_html

from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.blobstore import BlobInfo
from google.appengine.ext import blobstore
from google.appengine.api.images import get_serving_url

from scientist import Scientist
from datetime import date, datetime



class MainHandler(webapp2.RequestHandler):
    def get(self):
        scientists = Scientist.query().order(Scientist.birth_date).fetch()
        render_html(self, "list.html", u"Česká věda",
                    u"Zde je seznam.",
                    template_values={"scientists": scientists})

class CreateScientistsHandler(webapp2.RequestHandler):
    def get(self):
        mendel = Scientist()
        mendel.name = u"Gregor"
        mendel.surname = u"Mendel"
        mendel.birth_date = date(1822, 7, 20)

        mendel.put()

        wich = Scientist()
        wich.name = u"Otto"
        wich.surname = u"Wichterle"
        wich.birth_date = date(1913, 10, 27)

        wich.put()

        mull = Scientist()
        mull.name = u"Ilona"
        mull.surname = u"Müllerová"
        mull.birth_date = date(1954, 1, 1)

        mull.put()


class SendMailHandler(webapp2.RequestHandler):
    def post(self):
        user_address = self.request.get("email")
        sender_address = "pls-reply@example.com"
        subject = u"Vítejte"
        message = u"Tento email vám přišel z App Enginu"

        mail.send_mail(sender_address, user_address, subject, message)

class AddScientistHandler(blobstore_handlers.BlobstoreUploadHandler):
    def get(self):
        upload_url = blobstore.create_upload_url("/upload")
        render_html(self, "add_form.html", u"Nahrát vědce", u"",
                    template_values={"upload_url": upload_url})

    def post(self):
        s = Scientist()
        s.name = self.request.get("name")
        s.surname = self.request.get("surname")
        s.birth_date = datetime.strptime(self.request.get("birth_date"), "%Y-%m-%d").date()
        upload_files = self.get_uploads("portrait")
        blob_info = upload_files[0]
        assert (isinstance(blob_info, BlobInfo))
        s.portrait_blob_key = blob_info.key()
        s.portrait_url = get_serving_url(s.portrait_blob_key)
        s.put()

        self.redirect("/upload")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/setup', CreateScientistsHandler),
    ('/sendmail', SendMailHandler),
    ('/upload', AddScientistHandler),
], debug=True)
