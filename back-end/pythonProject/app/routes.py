from app import app
from app.UserLabel import UserLabel
from app.Code import Code
from app.User import User

app.register_blueprint(UserLabel,url_prefix='/UserLabel')
app.register_blueprint(Code,url_prefix='/Code')
app.register_blueprint(User,url_prefix='/User')
