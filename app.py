from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "3b5166042bf25f08b3aa16bfab4db5c9"

# set light database URI for development, this is file on local machine
#/// --> should be created in current directory
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

class User (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = "default.jpg")
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        #defines how object is printed out
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime(20), nullable = False, default =datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    #we use lowercase user as we reference tablename which is lowercase
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)

    def __repr__(self):
        #defines how object is printed out
        return f"Post('{self.title}', '{self.date_posted}')"


inquiries = [
    {
       "author": "Philipp Wahler",
        "location": "Hammelburg",
        "payment": 20,
        "title": "Looking for Babysitters",
        "content": "I'm looking for yada yada yada",
        "date_posted": "22.03.2020" 

    },
    {
       "author": "Max Schulte",
        "location": "St.Gallen",
        "payment": 30,
        "title": "Where am I",
        "content": "I am confused",
        "date_posted": "22.03.2020" 

    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/babysitting")
def babysitting():
    return render_template("babysitting.html", inquiries=inquiries, title = "Babysitting" )


@app.route("/registrieren", methods = ["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #adds flash message
        flash(f"Account für {form.username.data} erstellt!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title= "Registrieren", form=form)

@app.route("/einloggen")
def login():
    form = LoginForm()
    return render_template("login.html", title= "Einloggen", form=form)













if __name__ == "__main__":
    app.run(debug=True)