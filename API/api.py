from flask import Flask, render_template, url_for, flash, redirect, request
import time
import sqlite3
from get import get_query
from forms import RegistrationForm, LoginForm
from datetime import datetime
from predict import predict, prepare
import cv2
import os
from werkzeug.utils import secure_filename
#from flask.ext.uploads import UploadSet, configure_uploads, IMAGES


app=Flask(__name__)
UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])
app.config['SECRET_KEY'] = '91bf371c3d08b9198caf8ee553e3c298'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]



@app.route("/")
@app.route("/home")
def home():
    time= datetime.now()
    return render_template('home.html', posts=posts, time=time)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f' Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title= 'Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/THD-NTH", methods=['GET'])
def de_query():
    src=get_query()
    final=[]
    final=predict("img.jpg")
    return render_template('query.html', src=src, final=final)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/apply_test", methods=['GET','POST'])
def apply_test():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            filename= "img.jpg"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('apply_test.html')

@app.route ("/uploaded_file", methods=['GET'])
def uploaded_file():
    IMAGE_DIR='./../static/img.jpg'
    final=[]
    final=predict('./static/img.jpg')
    return render_template('uploaded_image.html', src=IMAGE_DIR, final=final)


if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
