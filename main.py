# coding=utf-8

import webapp2
from jinja import render_html

from google.appengine.api import users
from google.appengine.api import mail

from scientist import Scientist
from datetime import date



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
        

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/setup', CreateScientistsHandler),
    ('/sendmail', SendMailHandler)
], debug=True)
