# import connexion


# def main():
#     app = connexion.App(__name__, specification_dir='openapi/')
#     app.add_api('openapi.yaml')
#     app.run(port=8080)


# if __name__ == '__main__':
#     main()

from flask import Flask, jsonify
import connexion
from connexion.resolver import RestyResolver
from flask_mongoengine import MongoEngine
import datetime
# from models.datasets_model import Dataset_mongo
app = connexion.App(__name__, specification_dir='openapi/')
UPLOAD_FOLDER = 'storage/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
db = MongoEngine()


# Create the application instance
app.add_api('swagger.yml')
app.app.config['MONGODB_SETTINGS'] = {
    'db': 'flask123',
    'host': 'mongodb://mansoor:mansoor11@ds019829.mlab.com:19829/flask123',
    'retryWrites': False
}
# from models import db
db.init_app(app.app)



# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
