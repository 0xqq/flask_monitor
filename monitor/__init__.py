from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
import monitor.apps.monitor_app.urls