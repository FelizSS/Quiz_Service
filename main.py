from flask import Flask

from api import leaders, registration, test_process

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()

# zadat konfiguraciyu dlya bazi dannih
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'


# zadat prilojenie
db.init_app(app)


# registraciya komponenta

app.register_blueprint(leaders.leaders_bp)
app.register_blueprint(registration.registration_bpbp)
app.register_blueprint(test_process.test_bp)



