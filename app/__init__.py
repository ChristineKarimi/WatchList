from flask import Flask

#initialization

app = Flask(__name__)

from app import views
