from bson import json_util
from mongoengine import Document, StringField, BooleanField, connect,ReferenceField, ListField, CASCADE



#uri = "mongodb+srv://user1:vvLi1ykCKG41nHsW@newcluster.w9thwg8.mongodb.net/?retryWrites=true&w=majority"
connect(db='hw8', host='mongodb://localhost:27017')

class Author(Document):
    fullname = StringField(required=True,unique=True)
    born_date=StringField(max_length=50)
    born_location=StringField(max_length=150)
    description=StringField()
    meta={'collection':'author'}


class Quote(Document):
    author = ReferenceField(Author,reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=15))
    quote = StringField()
    meta = {'collection':'quotes'}

    def to_json(self, *args, **kwargs):
        data = self.to_mongo(*args, **kwargs)
        data["author"] = self.author.fullname
        return json_util.dumps(data, ensure_ascii=False)
    
class Contact(Document):
    full_name = StringField(required=True)
    email  = StringField(required=True)
    notifed = BooleanField(default=False)