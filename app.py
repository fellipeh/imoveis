# -*- coding: utf-8 -*-
import datetime
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///imoveis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'alsdkhas71234C!@#$'

db = SQLAlchemy(app)



@app.before_first_request
def create_tables():
    db.create_all()


app.config['JWT_SECRET_KEY'] = 'jwt-alsdkhas71234C-alsdkhas71234C'
jwt = JWTManager(app)

app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(weeks=5215)
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)


import views, models, resources

api.add_resource(resources.UserRegistration, '/user/register')
api.add_resource(resources.UserLogin, '/user/login')
api.add_resource(resources.UserLogoutAccess, '/user/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/user/logout/refresh')
api.add_resource(resources.TokenRefresh, '/user/token/refresh')
api.add_resource(resources.AllUsers, '/user/list')

api.add_resource(resources.Items, '/items')

# api.add_resource(resources.SecretResource, '/secret')
