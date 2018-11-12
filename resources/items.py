# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse
from models import ItemModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)

parser = reqparse.RequestParser()
parser.add_argument('id', help='Id', required=False)
parser.add_argument('title', help='Title - This field cannot be blank', required=True)
parser.add_argument('description', help='Description', required=False)
parser.add_argument('price', help='Price', required=False)


class Items(Resource):
    @jwt_required
    def put(self):
        data = parser.parse_args()
        new_item = ItemModel(
            title=data['title'],
            description=data['description'],
            price=data['price']
        )
        try:
            new_item.save_to_db()
            return {
                'message': 'Item {} was created'.format(data['title'])
            }
        except Exception as e:
            return {'message': str(e)}, 500

    @jwt_required
    def get(self):
        return ItemModel.return_all()

    @jwt_required
    def delete(self):
        return ItemModel.delete_all()
