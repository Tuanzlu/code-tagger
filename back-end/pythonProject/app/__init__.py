from flask import Flask
import rsa
import sqlite3
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources=r'/*')

from app import routes




