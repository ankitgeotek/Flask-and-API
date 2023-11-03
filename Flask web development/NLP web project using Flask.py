
#render_template will load the html files in flask
from flask import Flask, redirect, render_template, request, session 
'''
session is a dictionary variable to store values, If somebody login we will set the value of session =1, that means user is logged in
and before entring in to any profile we will check for logged_in ==1 else redirect to ('/') that is login page
'''
#importing API wala file that we have made
import api

#for user information entry database import class Database from db file
from db import Database
dbo=Database()


# creating object of flask class with name app and pass name of current file using __name__

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'






# create a route using decorator
# route is as url
@app.route('/') #if somebody hit slash code witten in def will executed
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


#methods=['post'] telling data is coming htrough post and will not be visble in url
@app.route('/perform_registration', methods=['post'])   
def perform_registration():
    name=request.form.get('user_name')
    email=request.form.get('user_email')
    password= request.form.get('user_password')
    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html', message="Registration Successful kindly Login to proceed!!")    
                                        #message will be displayed on the login page 
    else:
        return render_template('register.html', message="Email already Exist!!")
                                                #message will be displayed on the login page 
    
    
#request is to receive the data


@app.route('/perform_login', methods=['post'])
def perform_login():
    email=request.form.get('user_email')
    password= request.form.get('user_password')
    response=dbo.search(email, password)

    if response:
        session['logged_in']='asd'
        return redirect('/profile')
    else:
        return render_template('/login.html', message='Incorrect email/password !!')
    

@app.route('/profile')
def profile():

    if session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if session:
        return render_template("NER.html")
    else:
        return redirect('/')



@app.route('/perform_ner', methods=['post'])
def perform_ner():

    
    if session:
        text=request.form.get('ner_text')
        response=api.ner(text)
        print(response)

        return render_template('ner.html', response=response)
    else:
        return redirect('/')


#debug=True will automatically update page if anything change in the page
app.run(debug=True)



