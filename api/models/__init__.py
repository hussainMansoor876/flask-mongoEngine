import datetime

from flask_mongoengine import MongoEngine

db = MongoEngine()


# class Todo(db.Document):
#     title = db.StringField(max_length=60)
#     text = db.StringField()
#     done = db.BooleanField(default=False)
#     pub_date = db.DateTimeField(default=datetime.datetime.now)

class Dataset_mongo(db.Document):
    dataset_filename = db.StringField(required=True)
    dataset_rows = db.IntField(required=True)
    dataset_columns = db.IntField(required=True)
    dataset_headers = db.ListField(db.StringField(), required=True)

Dataset_mongo(dataset_filename="abc", dataset_rows=8, dataset_columns=8, dataset_headers=["2","LL"]).save()