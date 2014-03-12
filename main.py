# coding=utf-8

import webapp2
from jinja import render_html

from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            render_html(self, "list.html", u"Ahoj",
                        u"Nejsi ty náhodou {}?".format(user.nickname()))
        else:
            render_html(self, "list.html", u"Ahoj",
                        u"<a href='{}'>Přihlaš se</a>.".format(users.create_login_url("/")))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
