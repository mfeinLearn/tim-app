#!/usr/bin/env python3

from faker import Faker
# from app import app
# from models import db, User, Date, Relationship, Friend, Location, Note
from models import User, Date, Relationship, Friend, Location, Note
from random import randint, choice as rc
from datetime import datetime
from config import db, app

# db.init_app(app) 

with app.app_context():

    fake = Faker()

    print('''
    app start
    ''')

    print("Deleting all records...")
    User.query.delete() 
    Date.query.delete()
    Relationship.query.delete()
    Friend.query.delete()
    Location.query.delete()
    Note.query.delete()

    print("Creating Users...")
    # make sure users have unique usernames
    users = []
    usernames = []

    for i in range(20):
        
        username = fake.first_name()
        while username in usernames:
            username = fake.first_name()
        usernames.append(username)

        user = User(
            name=fake.first_name(),
            username=username
        )

        user.password_hash = user.username + 'password'

        users.append(user)

    db.session.add_all(users)
    db.session.commit()



    print("Creating Dates...")
    dates = []

    mylist = ["Male", "Female", "Other"]
    bol_list = [True, False]
    img_url=["https://i.pinimg.com/236x/a9/11/8c/a9118c7a32b4019033dca484ac9d6748.jpg","https://i.pinimg.com/236x/86/75/eb/8675eb57c5369047d29c48477165849e.jpg","https://i.pinimg.com/236x/e4/c0/17/e4c017b9248d29a7a9d5de2360768e93.jpg", "https://i.pinimg.com/236x/6b/4a/d9/6b4ad97c213b85dad13072e0bc1d1fdc.jpg", "https://i.pinimg.com/236x/c5/37/67/c53767e37fd3ee789305bc728cd77258.jpg","https://i.pinimg.com/236x/ef/aa/44/efaa443d406bfec16bc8b967e635f600.jpg"]

    for i in range(20):
        
        date = Date(
            name=fake.first_name(),
            gender=rc(mylist),
            see_again=rc(bol_list),
            image_uri= rc(img_url),
            date_of_date= datetime.utcnow()
        )
        dates.append(date)

    db.session.add_all(dates)
    db.session.commit()

    print("Creating Relationships...")

    rel_list = ["brother", "sister", "father", "mother", "friend"]
    relationships = []

    for i in range(20):

        relationship = Relationship(
            title=rc(rel_list),
        )

        relationships.append(relationship)

    db.session.add_all(relationships)
    db.session.commit()


    print("Creating Friends...")
    friends = []

    for i in range(20):

        friend = Friend(
            name=fake.first_name(),
            email=fake.email(),
            phone_number=int(fake.msisdn())
        )

        friends.append(friend)

    db.session.add_all(friends)
    db.session.commit()



    print("Creating Locations...")
    locations = []

    for i in range(20):

        location = Location(
            name=fake.street_name(),
            address=fake.street_address()
        )

        locations.append(location)

    db.session.add_all(locations)

    print("Creating Notes...")
    notes = []

    for i in range(20):

        note = Note(
            note=fake.text(),
        )

        notes.append(note)

    db.session.add_all(notes)
    db.session.commit()


    print("Complete.")



    print('''
    app end
    ''')
#########################




# def make_movies():

#     Movie.query.delete()
    
#     movies = []
#     for i in range(50):
#         m = Movie(title=fake.sentence(nb_words=4).title())
#         movies.append(m)

#     db.session.add_all(movies)
#     db.session.commit()

# if __name__ == '__main__':
#     with app.app_context():
#         make_movies()


# ######################





# with app.app_context():

#     print("Deleting all records...")
#     Recipe.query.delete()
#     User.query.delete()

#     fake = Faker()

#     print("Creating users...")

#     # make sure users have unique usernames
#     users = []
#     usernames = []

#     for i in range(20):
        
#         username = fake.first_name()
#         while username in usernames:
#             username = fake.first_name()
#         usernames.append(username)

#         user = User(
#             username=username,
#             bio=fake.paragraph(nb_sentences=3),
#             image_url=fake.url(),
#         )

#         user.password_hash = user.username + 'password'

#         users.append(user)

#     db.session.add_all(users)

#     print("Creating recipes...")
#     recipes = []
#     for i in range(100):
#         instructions = fake.paragraph(nb_sentences=8)
        
#         recipe = Recipe(
#             title=fake.sentence(),
#             instructions=instructions,
#             minutes_to_complete=randint(15,90),
#         )

#         recipe.user = rc(users)

#         recipes.append(recipe)

#     db.session.add_all(recipes)
    
#     db.session.commit()
#     print("Complete.") 
  