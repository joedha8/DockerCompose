# Product Service

# Import framework
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class Biodata(Resource):
    def get(self):
        return {
            'bio': ['Yudha Pratama Putra', '155410053', 'Teknik Informatika']
        }

# Create routes
api.add_resource(Biodata, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
