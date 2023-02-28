from flask import Flask, request, make_response, jsonify, render_template,  request, session
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from models import User, Date, Relationship, Friend, Location, Note

from config import app, db, api

import ipdb
CORS(app)
migrate = Migrate(app, db)

##### Start of API!!!!!!!!

### ROOT
@app.route('/')
def index():
    return "Index for The Trusted Ideal Mate (TIM) API  "


### DATE
@app.route('/dates', methods=['GET', 'POST'])
def dates():
    if request.method == 'GET':
        #ipdb.set_trace()
        dates = Date.query.all()
        dates_dicts = []
        for date in dates:
            dates_dicts.append(date.to_dict())
       
        #ipdb.set_trace()
        return make_response(
            jsonify(dates_dicts),
            200,
        )

    elif request.method == 'POST':
        data = request.get_json()
        # ipdb.set_trace()
        date = Date(
            name = data['name'],
            gender = data['gender'],
            see_again = data['see_again'],
            date_of_date = datetime.utcnow(),
            image_uri = data['image_uri'],
        )

        db.session.add(date)
        db.session.commit()


        user = User.query.filter(User.id == session['user_id']).first()
        date_just_added = Date.query.order_by(Date.id.desc()).first()

        user.dates.append(date_just_added)

        db.session.add(user)
        db.session.commit()


        date_just_added.user_id = user.id
        user.dates.append(date_just_added)

        db.session.add(user)
        db.session.commit()

        date_just_added = Date.query.order_by(Date.id.desc()).first()

        #######   ----  session['user_id']


        date_dict = date_just_added.to_dict()

        response = make_response(
            date_dict,
            201
        )

        return response

    return make_response(
        jsonify({"text": "Method Not Allowed"}),
        405,
    ) 

@app.route('/dates/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def date_by_id(id):
    date = Date.query.filter(Date.id == id).first()

    if request.method == 'GET':
        date_dict = date.to_dict()

        response = make_response(
            date_dict,
            200
        )
        response.headers["Content-Type"] = "application/json"

    elif request.method == 'PATCH':
        #ipdb.set_trace()
        data = request.get_json()

        for attr in data:
            setattr(date, attr, data[attr])
        #ipdb.set_trace()
        date.date_of_date = datetime.utcnow() # fix later!
        db.session.add(date)
        db.session.commit()

        response = make_response(
            jsonify(date.to_dict()),
            200,
        )

    elif request.method == 'DELETE':
        #ipdb.set_trace()
        db.session.delete(date)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Date deleted."    
        }

        response = make_response(
            response_body,
            200
        )

    return response



### LOCATION

@app.route('/locations', methods=['GET', 'POST'])
def locations():
    if request.method == 'GET':
        #ipdb.set_trace()
        locations = Location.query.all()
        locations_dicts = []
        for location in locations:
            locations_dicts.append(location.to_dict())

        return make_response(
            jsonify(locations_dicts),
            200,
        )

    
    elif request.method == 'POST':
        data = request.get_json()
        # ipdb.set_trace()

        location = Location(
            name = data['name'],
            address = data['address'],
        )

        db.session.add(location)
        db.session.commit()

        location_dict = location.to_dict()

        response = make_response(
            location_dict,
            201
        )

        return response


    return make_response(
        jsonify({"text": "Method Not Allowed"}),
        405,
    ) 

@app.route('/locations/<int:id>', methods=['GET', 'PATCH' ,'DELETE'])
def location_by_id(id):
    location = Location.query.filter(Location.id == id).first()

    if request.method == 'GET':
        location_dict = location.to_dict()

        response = make_response(
            location_dict,
            200
        )
        response.headers["Content-Type"] = "application/json"

        return response


    elif request.method == 'PATCH':
        data = request.get_json()
        for attr in data:
            setattr(location, attr, data[attr])
            
        db.session.add(location)
        db.session.commit()

        response = make_response(
            jsonify(location.to_dict()),
            200,
        )

        return response
        #####------


    elif request.method == 'DELETE':
        db.session.delete(location)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Location deleted."    
        }

        response = make_response(
            response_body,
            200
        )

        return response


    return make_response(
        jsonify({"text": "Method Not Allowed"}),
        405,
    )

### USER

@app.route('/users', methods=['GET'])
def users():
    if request.method == 'GET':
        #ipdb.set_trace()
        users = User.query.all()
        users_dicts = []
        for user in users:
            users_dicts.append(user.to_dict())

        return make_response(
            jsonify(users_dicts),
            200,
        )

    return make_response(
        jsonify({"text": "Method Not Allowed"}),
        405,
    )

@app.route('/users/<int:id>', methods=['GET'])
def user_by_id(id):
    user = User.query.filter(User.id == id).first()

    if request.method == 'GET':
        user_dict = user.to_dict()

        response = make_response(
            user_dict,
            200
        )
        response.headers["Content-Type"] = "application/json"

        return response

    return make_response(
        jsonify({"text": "Method Not Allowed"}),
        405,
    ) 


### RELATIONSHIP
@app.route('/relationships', methods=['GET'])
def relationships():
    if request.method == 'GET':
        #ipdb.set_trace()
        relationships = Relationship.query.all()
        relationships_dicts = []
        for relationship in relationships:
            relationships_dicts.append(relationship.to_dict())

        return make_response(
            jsonify(relationships_dicts),
            200,
        )

    return make_response(
        jsonify({"text": "Method Not Allowed"}),
        405,
    )

### FRIEND
@app.route('/friends', methods=['GET', 'POST'])
def friends():
    if request.method == 'GET':
        #ipdb.set_trace()
        friends = Friend.query.all()
        friends_dicts = []
        for friend in friends:
            friends_dicts.append(friend.to_dict())

        return make_response(
            jsonify(friends_dicts),
            200,
        )


    
    elif request.method == 'POST':
        data = request.get_json()
        # ipdb.set_trace()

        friend = Friend(
            name=data['name'],
            email=data['email'],
            phone_number=data['phone_number']
        )

        db.session.add(friend)
        db.session.commit()

        friend_dict = friend.to_dict()

        response = make_response(
            friend_dict,
            201
        )

        return response




    return make_response(
        jsonify({"text": "Method Not Allowed"}),
        405,
    ) 

@app.route('/friends/<int:id>', methods=['GET','PATCH','DELETE'])
def friend_by_id(id):
    friend = Friend.query.filter(Friend.id == id).first()

    if request.method == 'GET':
        friend_dict = friend.to_dict()

        response = make_response(
            friend_dict,
            200
        )
        response.headers["Content-Type"] = "application/json"

        return response

    elif request.method == 'PATCH':
        data = request.get_json()
        for attr in data:
            setattr(friend, attr, data[attr])
            
        db.session.add(friend)
        db.session.commit()

        response = make_response(
            jsonify(friend.to_dict()),
            200,
        )

        return response
        #####------

    elif request.method == 'DELETE':
        db.session.delete(friend)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Date deleted."    
        }

        response = make_response(
            response_body,
            200
        )

        return response

    return make_response(
        jsonify({"text": "Method Not Allowed"}),
        405,
    ) 

###_NOTE
@app.route('/notes', methods=['GET'])
def notes():
    if request.method == 'GET':
        #ipdb.set_trace()
        notes = Note.query.all()
        notes_dicts = []
        for note in notes:
            notes_dicts.append(note.to_dict())

        return make_response(
            jsonify(notes_dicts),
            200,
        )

    return make_response(
        jsonify({"text": "Method Not Allowed"}),
        405,
    )

@app.route('/notes/<int:id>', methods=['GET', 'DELETE'])
def note_by_id(id):
    note = Note.query.filter(Note.id == id).first()

    if request.method == 'GET':
        note_dict = note.to_dict()

        response = make_response(
            note_dict,
            200
        )
        response.headers["Content-Type"] = "application/json"

        return response

    elif request.method == 'DELETE':
        db.session.delete(note)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Note deleted."    
        }

        response = make_response(
            response_body,
            200
        )

        return response




##### End of API!!!!!!!!


##### Beginning of Auth

class ClearSession(Resource):

    def delete(self):
    
        session['user_id'] = None

        return {}, 204


class Login(Resource):

    def post(self):
        #ipdb.set_trace()
        username = request.get_json()['username']
        user = User.query.filter(User.username == username).first()

        session['user_id'] = user.id

        return user.to_dict(), 200

class Logout(Resource):

    def delete(self):

        session['user_id'] = None
        
        return jsonify({'message': '204: No Content'}), 204

class CheckSession(Resource):

    def get(self):
        
        user_id = session['user_id']
        if user_id:
            user = User.query.filter(User.id == user_id).first()
            return jsonify(user.to_dict()), 200
        
        return jsonify({'message': '401: Not Authorized'}), 401

class Signup(Resource):

    def post(self):
        #ipdb.set_trace()
        request_json = request.get_json()

        username = request_json.get('username')
        name = request_json.get('name')
        password = request_json.get('password')

        user = User(
            name=name,
            username=username
        )

        # the setter will encrypt this
        user.password_hash = user.username + 'password'

        print('first')

        try:

            print('here!')

            db.session.add(user)
            db.session.commit()

            session['user_id'] = user.id

            print(user.to_dict())

            return user.to_dict(), 201

        except IntegrityError:

            print('no, here!')
            
            return {'error': '422 Unprocessable Entity'}, 422

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(ClearSession, '/clear')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')


##### End of of Auth

if __name__ == '__main__':
    app.run(port=5555)