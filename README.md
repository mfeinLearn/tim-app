# the-tim-app

Welcome to TIM! The Trusted Ideal Mate app.

In a world where finding the perfect match can be daunting, we understand the importance of prioritizing safety. While the concept of an ideal mate might be subjective, our application aims to make your dating experience safer and more secure. We achieve this by introducing a feature that sends essential information about your date – such as images, names, and more – to a trusted person or friend. This extra layer of precaution ensures that when you embark on a date with a potential match, someone you trust is aware of your plans.

We believe that safety should be an integral part of your dating journey. By incorporating the Trusted Ideal Mate app into your safety protocol, you can approach your dates with increased confidence and peace of mind.

## Setup

1. clone down
2. `cd tim-app`
3. run the following in the terminal: `pipenv install && pipenv shell`
4. `cd server`
5. run the following in the terminal: `python seed.py`

   - if there are errors try to fix them they should be pretty easy to they are mostly dependency problems, mainly installing stuff with pip. try the following first:

     ```
     pip install faker
     pip install flask-sqlalchemy
     pip install SQLAlchemy-serializer
     pip install flask-bcrypt
     pip install Flask-Migrate
     pip install flask-restful
     pip install Flask-Cors
     pip install ipdb
     ```

     - if all installs with no hickups then continue on below, if not, then create a pr.

6. To run the server run the following in the terminal: `python app.py`
7. open another terminal from the apps root directory
8. `cd client`
   10 run the following in the terminal: `npm install`
9. run the following command to run the server for react: `npm start`
10. when you add a new date and submit the form you will need to restart your server (will fix later!)
11. when you edit a date and press enter you are going to need to restart your server AND logout and in again (will fix later!)
12. when you delete a date you are going to need to press home and logout
    then login again(will fix later!)

# the tim cli

## Setup

1. clone down
2. `cd tim-app`
3. `cd server`
4. run the following in the terminal: `pipenv install && pipenv shell`
5. run `python tim_cli.py` to run the cli
6. If there are errors try to solve it, they are most likely dependency issues. if you can't just create a new pr.

## Note

The app and the CLI are a bit buggy and NOT DONE YET, but they work. The main functionality works locally only. I will update this sometime in the future. Enjoy!
