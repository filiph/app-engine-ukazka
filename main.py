# coding=utf-8

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(u'Ahoj Česko!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
