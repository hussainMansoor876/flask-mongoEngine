# import connexion


# def main():
#     app = connexion.App(__name__, specification_dir='openapi/')
#     app.add_api('openapi.yaml')
#     app.run(port=8080)


# if __name__ == '__main__':
#     main()

from flask import Flask, jsonify
import connexion
from flask_mongoengine import MongoEngine
import datetime
app = connexion.App(__name__, specification_dir='openapi/')

# Create the application instance
app.add_api('swagger.yml')
# app.app.config['MONGO_DBNAME'] = 'flask123'
# app.app.config['MONGO_URI'] = 'mongodb://mansoor:mansoor11@ds019829.mlab.com:19829/flask123'
app.app.config['MONGODB_SETTINGS'] = {
    'db': 'flask123',
    'host': 'mongodb://mansoor:mansoor11@ds019829.mlab.com:19829/flask123',
    'retryWrites': False
}
mongo = MongoEngine(app.app)


class User(mongo.Document):
    email = mongo.StringField(required=True)
    first_name = mongo.StringField(max_length=50)
    last_name = mongo.StringField(max_length=50)
    date = mongo.DateTimeField(default=datetime.datetime.now)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    try:
        # result = User(email='abc@gmail.com', first_name="Mansoor",
        #               last_name="Hussain").save()
        # print(result.email)
        num_posts = User.objects().order_by('date')
        # print('Found {} posts with tag "mongodb"'.format(num_posts))
        for i in num_posts:
            print(i.email)

        return jsonify({"data": num_posts})
    except Exception as e:
        print(e)
        return str(e)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
