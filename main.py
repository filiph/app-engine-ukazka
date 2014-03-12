# coding=utf-8

import webapp2
from jinja import render_html

class MainHandler(webapp2.RequestHandler):
    def get(self):
        render_html(self, "list.html", u"Ahoj",
                    u"Toto je super kůlový.")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
