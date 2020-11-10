from flask import Flask
from flask_restful import Api
from resources.tep_hinh_anh import UploadImage


app = Flask(__name__)
api = Api(app)

api.add_resource(UploadImage, '/upload')

if __name__ == '__main__':
    app.run(debug=True)
