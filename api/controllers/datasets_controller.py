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


def post_dataset_with_file(source_file):  # noqa: E501
    """Creates a new Dataset

    This processes data provided by the API user and creates a new *Dataset*. The API user uploads a data *Source file*. The POST request returns a *Dataset ID*. # noqa: E501

    :param source_file:
    :type source_file: strstr

    :rtype: DatasetIdPostResponse
    """
    print(source_file.filename)
    # return {
    #     "dataset_id": "mansoor",
    # }
    return {
        "dataset_id": "40655045bfy",
        "dataset_filename": "KPIs Sheet.xlsx",
        "dataset_rows": 1500,
        "dataset_columns": 8,
        "dataset_headers": ['Revenue', 'Sign-Ups', 'Active Users', 'Mansoor']
    }


def get_dataset_by_id(requested_dataset_id):  # noqa: E501
    """Retrieve a Dataset by its ID

    This retrieves an existing *Dataset*. The API user indicates a *Dataset ID*. The GET request returns a *Dataset object*. # noqa: E501

    :param requested_dataset_id: The API user indicates a Dataset ID
    :type requested_dataset_id: str

    :rtype: Dataset
    """
    result = Dataset_mongo.objects(id=requested_dataset_id)[0]
    return result
    # return {
    #     "dataset_id": "40655045bfy",
    #     "dataset_filename": "KPIs Sheet.xlsx",
    #     "dataset_rows": 1500,
    #     "dataset_columns": 8,
    #     "dataset_headers": ['Revenue', 'Sign-Ups', 'Active Users', 'Mansoor']
    # }

def create(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    # Does the person exist already?
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{lname} successfully created".format(lname=lname), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=lname),
        )