from flask import Flask, jsonify
import connexion
from connexion.resolver import RestyResolver
from flask_mongoengine import MongoEngine
app = connexion.App(__name__, specification_dir='openapi/')
db = MongoEngine()
app.add_api('swagger.yml')
app.app.config['MONGODB_SETTINGS'] = {
    'db': 'flask123',
    'host': 'mongodb://mansoor:mansoor11@ds019829.mlab.com:19829/flask123',
    'retryWrites': False
}
# from models import db
db.init_app(app.app)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
