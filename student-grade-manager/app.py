from flask import Flask
from flask_login import LoginManager
from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

from routes import *  # Import routes sau khi app được tạo

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Sử dụng PORT từ Railway, mặc định 5000 nếu local
    app.run(host='0.0.0.0', port=port)
