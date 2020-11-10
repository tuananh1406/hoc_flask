import werkzeug
from flask_restful import reqparse


tap_tin = reqparse.RequestParser()
tap_tin.add_argument(
        'file',
        type=werkzeug.datastructures.FileStorage,
        location='tep_tai_len',
    )
