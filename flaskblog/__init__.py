from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = '383a0c17430549032bd3746008918aad'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'         # konfiguracja bazy danych
db = SQLAlchemy(app)                                                # przypisanie do db bazydanych dla app
bcrypt = Bcrypt(app)                                                # 


from flaskblog import routes