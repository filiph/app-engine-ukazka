
from google.appengine.ext import ndb

class Scientist(ndb.Model):
    name = ndb.StringProperty()
    surname = ndb.StringProperty()
    birth_date = ndb.DateProperty()

