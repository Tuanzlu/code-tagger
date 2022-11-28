from app import app
from app.UserRepository import UserRepository

app.register_blueprint(UserRepository,url_prefix='/UserRepository')
