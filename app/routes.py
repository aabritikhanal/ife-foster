import os
from app import app
from flask import render_template, request, redirect, session, url_for 
app.secret_key = b'K#\x1f_\xa4\xbe\x19Gk\x90\xb7K]\xcd\x0e\xa3'

from flask_pymongo import PyMongo
# name of database
app.config['MONGO_DBNAME'] = 'database' 
# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:A11272003k@cluster0-s7trw.mongodb.net/database?retryWrites=true&w=majority' 

mongo = PyMongo(app)

# INDEX
@app.route('/')
@app.route('/index')
def index():
    # connect to the database
    collection = mongo.db.project_users
    # pull data from database
    project_users = collection.find({}).sort("user")
    # use data 
    return render_template('index.html', project_users = project_users)
    
# SIGN-UP:
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method =="POST":
        # take in the info they gave us, check if username is taken, if username is available put into a database of users
        project_users = mongo.db.project_users
        existing_user = project_users.find_one({"username":request.form['username']})
        if existing_user is None:
            project_users.insert({"username":request.form['username'],"password":request.form['password']})
            return redirect(url_for('index'))
        else:
            message = "That username is taken. Try logging in, or try a different usename"
            return render_template('signup.html', message = message)
    else:
        return render_template('signup.html', message = "welcome!!!")
        
@app.route('/login', methods=['GET','POST'])

def login():
    project_users = mongo.db.project_users
    #use the username to find the account
    existing_user = project_users.find_one({"username":request.form["username"]})
    if existing_user:
        #check if the password is right
        if existing_user['password'] == request.form["password"] :
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            return "Your password doesn't match your username."
    else:
        return "There is no user with that username. Try making an account."

# lOG OUT
@app.route('/logout')

def logout():
    session.clear()
    return redirect('/')
    
@app.route ('/dog_profiles', methods= ["GET", "POST"])

def dog_profiles():
    return render_template('dog_profiles.html')

@app.route ('/jack_profile', methods= ["GET", "POST"])

def jack_profile():
    # if request.method == ['GET']:
    #     print("Post page")
    #     return render_template('dog_profiles.html')
    # else:
        print("Get Page")
        project_users = mongo.db.project_users
        existing_user = project_users.find_one({"username":request.form['username']})
        if existing_user is None:
            project_users.insert({"username":request.form['username'],"password":request.form['password']})
            return render_template('jack_profile.html')
        else:
            message = "That username is taken. Try logging in, or try a different usename"
            return render_template('signup.html', message = message)
        return render_template('jack_profile.html')
@app.route ('/generic', methods= ["GET", "POST"])
def generic():
    return render_template('generic.html')
    
@app.route ('/service', methods=['GET', 'POST'])
def service():
    return render_template('service.html')
    
@app.route ('/cart', methods=['GET', 'POST'])
def cart():
    return render_template('cart.html')