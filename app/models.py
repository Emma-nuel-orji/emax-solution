from app import db, login_manager
from datetime import datetime
from flask import current_app
from time import time
from flask_login import UserMixin
import json
# import jwt


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False, )
    image_file = db.Column(db.String(60), nullable=False, default='default.jpg.png')
    
    properties = db.relationship('Properties', backref='author', lazy=True)
    project = db.relationship('Project', backref='author', lazy=True)
    agent = db.relationship('Agent', backref='author', lazy=True)
    news = db.relationship('News', backref='author', lazy=True)
    
    # def get_reset_token(self, expires_in=300):
    #     return jwt.encode(
    #         {'reset_password': self.id, 'exp': time() + expires_in},
    #         current_app.config['SECRET_KEY'], algorithm='HS256')

    # @staticmethod
    # def verify_reset_token(token):
    #     try:
    #         user_id = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
    #     except:
    #         return None
    #     return User.query.get(user_id)

    # def __repr__(self):
    #     return f"User('{self.username}', '{self.phone}', '{self.email}', '{self.image_file}')"


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image = db.Column(db.String(20), nullable=False, default='default.jpg.png')
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Payment('{self.image}')"


class Product(db.Model):
    __searchable__ = ['name', 'desc']
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(20), nullable=False, default='default.jpg.png')
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.String, nullable=False)
    discount = db.Column(db.String, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.name


class JsonEcodedDict(db.TypeDecorator):
    impl = db.Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)


class Properties(db.Model):
    __searchable__ = ['name', 'description']
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(200), nullable=False, default='default.jpg.png')
    name = db.Column(db.String(20000), nullable=False)
    price = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(2000), unique=True, nullable=False)
    status = db.Column(db.String(6000), nullable=False)
    square = db.Column(db.String(2000), nullable=False)
    bedroom = db.Column(db.String(2000), nullable=False)
    bathroom = db.Column(db.String(2000), nullable=False)
    floors = db.Column(db.String(2000), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Properties('{self.name}','{self.price}','{self.location}','{self.status}','{self.square}','{self.bedroom}','{self.bathroom}','{self.floors}','{self.description}','{self.date_created}','{self.image}')"


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(20), nullable=False, default='default.jpg.png')
    name = db.Column(db.String(20000), nullable=False)
    status = db.Column(db.String(200), unique=True, nullable=False)
    location = db.Column(db.String(2000), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Project('{self.image}','{self.name}','{self.status}','{self.location}','{self.description}','{self.date_created}')"

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(20), nullable=False, default='default.jpg.png')
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"News('{self.image}','{self.title}','{self.description}','{self.date_created}')"

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(20), nullable=False, default='default.jpg.png')   
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(6000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f"Agent('{self.image}','{self.name}','{self.email}','{self.phone}','{self.date_created}')"

