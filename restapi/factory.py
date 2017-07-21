# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-07-21 10:16:31
# @Last Modified by:   jerry
# @Last Modified time: 2017-07-21 10:18:42
import os
from flask import Flask
from flask.views import MethodView
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] =True
    app.config['MONGODB_SETTINGS'] = {'DB':'RestBlog'}
    db.init_app(app)
    return app
