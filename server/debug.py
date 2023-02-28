#!/usr/bin/env python3

from config import db, app
from models import User, Date, Relationship, Friend, Location, Note

if __name__ == '__main__':
    engine = db.create_engine('sqlite:///app.db')
    with app.app_context():
        import ipdb; ipdb.set_trace()