
from google.appengine.ext import ndb

class Scientist(ndb.Model):
    name = ndb.StringProperty()
    surname = ndb.StringProperty()
    year_of_birth = ndb.DateProperty()

