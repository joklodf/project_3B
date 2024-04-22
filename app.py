from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    middle_name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    occupation = db.Column(db.String(50), nullable=False)
    specialization = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(80), nullable=False)


@app.route('/index')
@app.route('/')
def index():
    persons = Person.query.all()
    return render_template("index.html", persons=persons)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/add-person', methods=['GET', 'POST'])
def addperson():
    if request.method == 'GET':
        return render_template("addperson.html")

    elif request.method == 'POST':
        surname = request.form['surname']
        name = request.form['name']
        middle_name = request.form['middle_name']
        age = request.form['age']
        occupation = request.form['occupation']
        specialization = request.form['specialization']
        image_file = request.files['photo']

        if image_file:
            filename = image_file.filename
            image_data = image_file.read()
            new_person = Person(surname=surname, name=name, middle_name=middle_name,
                                age=age, occupation=occupation, specialization=specialization, image=image_data)

            db.session.add(new_person)
            db.session.commit()
    return render_template("addperson.html")


@app.route('/get-slider-data')
def get_slider_data():
    persons = Person.query.order_by(Person.id).all()
    data = []
    for person in persons:
        data.append({
          "name": person.name,
          "middle_name": person.middle_name,
          "surname": person.surname,
          "age": person.age,
          "occupation": person.occupation,
          "specialization": person.specialization,
          "image": base64.b64encode(person.image).decode("utf-8")
        })
    return jsonify(data)


if __name__ == '__main__':

    app.run()

