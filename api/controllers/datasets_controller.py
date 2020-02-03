import connexion

from datetime import datetime

# 3rd party modules
from flask import make_response, abort, Flask
# from models import datasets_model
# from api.models import Dataset_mongo
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'flask123',
    'host': 'mongodb://mansoor:mansoor11@ds019829.mlab.com:19829/flask123',
    'retryWrites': False
}
# from models import db
db = MongoEngine()
db.init_app(app)


class Dataset_mongo(db.Document):
    dataset_filename = db.StringField(required=True)
    dataset_rows = db.IntField(required=True)
    dataset_columns = db.IntField(required=True)
    dataset_headers = db.ListField(db.StringField(), required=True)


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp(),
    },
}


def post_dataset_with_file(source_file):  # noqa: E501
    """Creates a new Dataset

    This processes data provided by the API user and creates a new *Dataset*. The API user uploads a data *Source file*. The POST request returns a *Dataset ID*. # noqa: E501

    :param source_file:
    :type source_file: strstr

    :rtype: DatasetIdPostResponse
    """
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def get_dataset_by_id(requested_dataset_id):  # noqa: E501
    """Retrieve a Dataset by its ID

    This retrieves an existing *Dataset*. The API user indicates a *Dataset ID*. The GET request returns a *Dataset object*. # noqa: E501

    :param requested_dataset_id: The API user indicates a Dataset ID
    :type requested_dataset_id: str

    :rtype: Dataset
    """
    result = Dataset_mongo.objects(id="5e37e07428afb4ab335976e5")[0]
    for i in result:
        print(i)
    print(requested_dataset_id)
    return result
    # return {
    #     "dataset_id": "40655045bfy",
    #     "dataset_filename": "KPIs Sheet.xlsx",
    #     "dataset_rows": 1500,
    #     "dataset_columns": 8,
    #     "dataset_headers": ['Revenue', 'Sign-Ups', 'Active Users', 'Mansoor']
    # }
