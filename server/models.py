from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from sqlalchemy.ext.associationproxy import association_proxy

# db = SQLAlchemy()
from config import db, bcrypt


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-dates.user','-relationships.user',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    dates = db.relationship('Date', backref='user')
    relationships = db.relationship('Relationship', backref='user')
    friends = association_proxy('relationships', 'friend', creator=lambda fr: Review(friend=fr))


    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    def __repr__(self):
        return f'<User name={self.name}, username={self.username}>'

class Date(db.Model, SerializerMixin):
    __tablename__ = 'dates'

    serialize_rules = ('-notes.date','-locations.date','-user.dates',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    see_again = db.Column(db.Boolean, unique=False, default=False)
    image_uri = db.Column(db.String)
    date_of_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    locations = db.relationship('Location', backref='date')
    notes = db.relationship('Note', backref='date')

    def __repr__(self):
        return f'<Date name={self.name}, gender={self.gender}, see_again={self.see_again}, image_url={self.image_uri}, date_of_date={self.date_of_date}>'


class Relationship(db.Model, SerializerMixin):
    __tablename__ = 'relationships'

    serialize_rules = ('-user.relationships','-friend.relationships',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    friend_id = db.Column(db.Integer, db.ForeignKey('friends.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Relationship title={self.title}, friend_id={self.friend_id}, user_id={self.user_id}>'


class Friend(db.Model, SerializerMixin):
    __tablename__ = 'friends'

    serialize_rules = ('-relationships.friend',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.Integer) 
    relationships = db.relationship('Relationship', backref='friend')
    users = association_proxy('relationships', 'user', creator=lambda us: Relationship(user=us))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Friend name={self.name}, email={self.email}, phone_number={self.phone_number}>'

class Location(db.Model, SerializerMixin):
    __tablename__ = 'locations'

    serialize_rules = ('-date.locations',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    date_id = db.Column(db.Integer, db.ForeignKey('dates.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Location name={self.name}, address={self.address}, date_id={self.date_id}>' 


class Note(db.Model, SerializerMixin):
    __tablename__ = 'notes'

    serialize_rules = ('-date.notes',)

    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String)
    date_id = db.Column(db.Integer, db.ForeignKey('dates.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Note note={self.note}, date_id={self.date_id}>' 




