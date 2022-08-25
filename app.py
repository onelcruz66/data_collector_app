from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234qwer@localhost/data_collector_app'
db = SQLAlchemy(app)
class Data(db.Model):
    __tablename__="user_data"
    id=db.Column(db.Integer, primary_key=True)
    fname_=db.Column(db.String(50))
    lname_=db.Column(db.String(50))
    email_=db.Column(db.String(120), unique=True)
    phone_=db.Column(db.BIGINT)
    height_=db.Column(db.Integer)
    weight_=db.Column(db.Integer)

    def __init__(self, fname_, lname_, email_, phone_, height_, weight_):
        self.fname_=fname_
        self.lname_=lname_
        self.email_=email_
        self.phone_=phone_
        self.height_=height_
        self.weight_=weight_



@app.route("/")

def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])

def success():
    if request.method == 'POST':
        fname = request.form["first_name"]
        lname = request.form["last_name"]
        email = request.form["email_name"]
        phone = request.form["phone_number"]
        height = request.form["height_amount"]
        weight = request.form["weight_amount"]
        data = Data(fname, lname, email, phone, height, weight)
        print(email, height, fname, lname, phone, height, weight)
        db.session.add(data)
        db.session.commit()
    return render_template("success.html")

if __name__ == '__main__':
    app.debug=True
    app.run()