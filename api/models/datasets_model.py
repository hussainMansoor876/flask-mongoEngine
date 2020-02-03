#!/usr/bin/env python
# coding: utf-8

# Datasets model for API v0.1.1
#
# A MongoDB **dataset** document's schema is represented by the **Dataset_mongo** class with the following fields:
# - dataset_filename: the name of the Excel file including the extension
# - dataset_rows: the count of rows of the Excel file
# - dataset_columns: the count of columns of the Excel file
# - dataset_headers: the list of columns headers of the Excel file.


# Definition of the Dataset_mongo class

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
