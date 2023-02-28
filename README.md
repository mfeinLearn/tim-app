# the-tim-app

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

## Note

This app is buggy but works. I will update this sometime in the future. Enjoy!
