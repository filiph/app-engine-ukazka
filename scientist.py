
from google.appengine.ext import ndb

class Scientist(ndb.Model):
    name = ndb.StringProperty()
    surname = ndb.StringProperty()
    birth_date = ndb.DateProperty()
    portrait_blob_key = ndb.BlobKeyProperty()
    portrait_url = ndb.StringProperty(indexed=False)


