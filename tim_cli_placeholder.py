#!/usr/bin/env python3

from config import db, app
from models import User, Date, Relationship, Friend, Location, Note

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
    To quit this prompt, type 'exit' at any time
        ''')

# solution to error:==>  https://favtutor.com/blogs/python-switch-case#:~:text=Break%3A%20The%20break%20statement%20is,after%20the%20switch%20case%20statement.
def switch_statement(argument):
    switcher = {
        'view users': view_users(),
        'view dates': view_dates(),
        'view locations': view_locations(),
        'view relationships': view_relationships(),
        'view friends': view_friends(),
        'view notes': view_notes(),
        'view user friends': list_friends_by_user(),
        'view user dates': list_dates_by_user(),
        'view date locations': list_locations_by_date()
    }
 
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, '''
    Thanks for using The Trusted Ideal Mate app (TIM) :)
    ''')

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
    pass

def delete_date():
    pass

def sort_date_by_date_of_date():
    pass

def find_or_create_by_name():
    pass

def create_new_user():
    pass 

def find_by_name():
    pass





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