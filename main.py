# coding=utf-8

import webapp2
from jinja import render_html

from google.appengine.api import users

from scientist import Scientist
from datetime import date

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            render_html(self, "list.html", u"Ahoj",
                        u"Nejsi ty náhodou {}?".format(user.nickname()))
        else:
            render_html(self, "list.html", u"Ahoj",
                        u"<a href='{}'>Přihlaš se</a>.".format(users.create_login_url("/")))

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


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/setup', CreateScientistsHandler)
], debug=True)
