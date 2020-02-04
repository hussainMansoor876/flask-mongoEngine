import connexion

from datetime import datetime

# 3rd party modules
from flask import make_response, abort, Flask, request
import os
# from models import datasets_model
# from api.models import Dataset_mongo
from flask_mongoengine import MongoEngine
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'flask123',
    'host': 'mongodb://mansoor:mansoor11@ds019829.mlab.com:19829/flask123',
    'retryWrites': False
}

UPLOAD_FOLDER = './storage/'
ALLOWED_EXTENSIONS = {'csv', 'xls', 'xlsx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

db = MongoEngine()
db.init_app(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
    filename = secure_filename(source_file.filename)
    if allowed_file(filename):
        source_file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return {
            "dataset_id": "mansoor",
        }
    return {
            "dataset_id": "Not found",
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
