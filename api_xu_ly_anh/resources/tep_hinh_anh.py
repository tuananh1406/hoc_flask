import os
import werkzeug
from flask import send_from_directory
from flask_restful import Resource, reqparse
from common.parsers import tap_tin


class UploadImage(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument(
             'file',
             type=werkzeug.datastructures.FileStorage,
             location='files',
             )
        args = parse.parse_args()
        hinh_anh = args['file']
        thu_muc = 'tai_len'
        duong_dan_luu = os.path.join(thu_muc, hinh_anh.filename)
        hinh_anh.save(duong_dan_luu)
        return send_from_directory(thu_muc, hinh_anh.filename, as_attachment=True)
