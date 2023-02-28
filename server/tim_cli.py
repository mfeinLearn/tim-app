#!/usr/bin/env python3

from config import db, app
from models import User, Date, Relationship, Friend, Location, Note

def view_users():
    return view_users()
def view_dates():
    return view_dates()
def view_locations():
    return view_locations()
def view_relationships():
    return view_relationships()
def view_friends():
    return view_friends()
def view_notes():
    return view_notes()
def list_friends_by_user():
    return list_friends_by_user()
def list_dates_by_user():
    return list_dates_by_user()
def list_locations_by_date():
    return list_locations_by_date()
def update_user_username():
    return update_user_username()
def delete_date():
    return delete_date()
def sort_date_by_date_of_date():
    return sort_date_by_date_of_date()
def create_new_user():
    return create_new_user()
def find_user_by_name_and_username():
    return find_user_by_name_and_username()
def default():
    return "Thanks for using The Trusted Ideal Mate app (TIM) :)"

def print_me():
        print('''

    ***********************************
    Welcome to The Trusted Ideal Mate!
    ***********************************

    To view all of the users, enter 'view users'
    To view all of the dates, enter 'view dates'
    To view all of the locations, enter 'view locations'
    To view all of the relationships, enter 'view relationships'
    To view all of the friends, enter 'view friends'
    To view all of the notes, enter 'view notes'
    To view all of a user's friends, enter 'view user friends'
    To view all of a user's dates, enter 'view user dates'
    To view all of a user's date locations, enter 'view date locations'
    To update user's username, enter 'update user username'
    To delete a date, enter 'delete date'
    To sort all dates by date, enter 'sort date by date'
    To create a new user, enter 'create user'
    To find a user, enter 'find user'
    To quit this prompt, type 'exit' at any time
        ''')

switcher = {
    'view users': view_users,
    'view dates': view_dates,
    'view locations': view_locations,
    'view relationships': view_relationships,
    'view friends': view_friends,
    'view notes': view_notes,
    'view user friends': list_friends_by_user,
    'view user dates': list_dates_by_user,
    'view date locations': list_locations_by_date,
    'update user username': update_user_username,
    'delete date': delete_date,
    'sort date by date': sort_date_by_date_of_date,
    'create user': create_new_user,
    'find user': find_user_by_name_and_username
    }

def switch_statement(argument):
    print(switcher.get(argument, default)())

def call():
    inpwut = ""
    while inpwut != "exit":
        print_me()
        inpwut = input('What would you like to do? ')
        switch_statement(inpwut)

def view_users():
    print('''
    Here are the users:
    ''')
    users = User.query.order_by(User.name).all()
    for i, el in enumerate(users):
        print(f'Name: {el.name} | Username: {el.username} | ID: {el.id}')
    #return ""

def view_locations():
    print('''
    Here are the locations:
    ''')
    locations = Location.query.all()
    for i, el in enumerate(locations):
        print(f'Name: {el.name} | Address: {el.address} | ID: {el.id}')
    #return ""



def view_dates():
    print('''
    Here are the dates:
    ''')
    dates = Date.query.all()
    for i, el in enumerate(dates):
        print(f'Name: {el.name} | gender: {el.gender} | See Again: {el.see_again and "Yes" or "No" } | Image Url: {el.image_uri} | Date of the Date: {el.date_of_date} | ID: {el.id}')
    #return ""

def view_relationships():
    print('''
    Here are the relationships:
    ''')
    relationships = Relationship.query.all()
    for i, el in enumerate(relationships):
        print(f'Title: {el.title} | ID: {el.id}')
    #return ""

def view_friends():
    print('''
    Here are the friends:
    ''')
    friends = Friend.query.all()
    for i, el in enumerate(friends):
        print(f'Name: {el.name} | Phone Number: {el.phone_number} | Email: {el.email}')
    #return ""

def view_notes():
    print('''
    Here are the notes:
    ''')
    notes = Note.query.all()
    for i, el in enumerate(notes):
        print(f'Note: {el.note} | ID: {el.id}')
    #return ""


def list_friends_by_user():
    inpwut = input('''
    
    Please enter the name of a user (first letter MUST be capitalized) HERE: ''')
    user = User.query.filter_by(name=inpwut).first()    
    print(f"{user.name}'s friends are(is): {user.friends}")
    

def list_dates_by_user():
    inpwut = input('''
    
    Please enter the name of a user (first letter MUST be capitalized) HERE: ''')
    user = User.query.filter_by(name=inpwut).first()    
    print(f"{user.name}'s dates are(is): {user.dates}")

def list_locations_by_date():
    inpwut = input('''
    
    Please enter the name of a date (first letter MUST be capitalized) HERE: ''')
    date = Date.query.filter_by(name=inpwut).first()
    print(f" Your dates with {date.name} have been in the following locations: {date.locations}")


def update_user_username():
    inpwut = input('''
    
    Please enter the old username of a user (first letter MUST be capitalized) HERE: ''')

    user = User.query.filter(User.username == inpwut).first()

    new_username = input('''
    
    Please enter the new username of that user (first letter MUST be capitalized) HERE: ''')

    if user:
        user.username = new_username
        db.session.add(user)
        db.session.commit()
        print('saving...')
        print('saving..')
        print('saving.')
        print('updated!')
        print(f"{user.name}'s new username is {user.username}.")

def delete_date():
    date_name = ''
    date_id_input = input('''
    
    Please enter the id of the date that you want to delete (must be an integer!) HERE: ''')

    date = Date.query.filter_by(id=int(date_id_input)).first()
    date_name = date.name
    db.session.delete(date)
    db.session.commit()
    print(f'{date_name} with id {date_id_input} was deleted!')
    

def sort_date_by_date_of_date():
    '''might need to circle back - format dates'''
    sorted_dates_by_date_of_date = Date.query.order_by(db.desc(Date.date_of_date)).all()
    for el in sorted_dates_by_date_of_date:
        print(el)

## still need to add above ^^^^!!!
def create_new_user():
    name_input = input('''
    
    Please enter your name HERE: ''')

    username_input = input('''

    Thanks!
    Now, please enter your username HERE: ''')

    password_input = input('''

    Perfect!
    Ok, finally, please enter your password HERE: ''')

    print('Great, creating new user now!')

    new_user = User(
        name=name_input,
        username=username_input
    )
    new_user.password_hash = password_input + 'password'

    db.session.add(new_user)
    db.session.commit()
    print(f"All set, New user ID is {new_user.id}.")

def find_user_by_name_and_username():
    name_input = input('''
    
    Please enter the name of a user (first letter MUST be capitalized) HERE: ''')
    username_input = input('''
    
    Ty!! 
    Now, please enter the username of that user (first letter MUST be capitalized) HERE: ''')

    user = User.query.filter(User.name == name_input).filter(User.username == username_input).first()

    print(f'the user that you are looking for is {user}')


def find_or_create_user_by_name():
    '''maybe come back'''
    pass


    # print(f"New student ID is {albert_einstein.id}.")








if __name__ == '__main__':
    engine = db.create_engine('sqlite:///app.db')
    with app.app_context():
        #import ipdb; ipdb.set_trace()
        call()

    # student_grades = []

    # grade = input("Student name, grade: ")
    # while grade:
    #     student_grades.append(grade)
    #     # end when no grade is entered
    #     grade = input("Student name, grade: ")

    # create_grade_report(student_grades)