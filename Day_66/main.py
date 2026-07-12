from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import os

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv():
        return False

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}



with app.app_context():
    db.create_all()

load_dotenv()
my_secure_password = os.getenv("MY_SECURE_PASSWORD", "defaultpassword")


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def get_random():
    return Cafe.query.order_by(db.func.random()).first().to_dict()

@app.route("/one/<int:cafe_id>", methods=['GET'])
def get_one(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    return jsonify(error={"Not Found": "No cafe with that id."}), 404


@app.route("/all", methods=['GET'])
def get_all():
    return [cafe.to_dict() for cafe in Cafe.query.all()]


@app.route("/search", methods=['GET'])
def search():
    location = request.args.get("location")
    name = request.args.get("name")
    if not location and not name:
        return jsonify(error={"Bad Request": "Provide 'location' or 'name' parameter."}), 400
    query = db.select(Cafe)
    if location:
        query = query.where(db.func.lower(Cafe.location) == location.lower())
    if name:
        query = query.where(db.func.lower(Cafe.name) == name.lower())
    cafes = db.session.execute(query).scalars().all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    if location and name:
        return jsonify(error={"Not Found": f"Sorry, we do not have a cafe called {name} in {location}."}), 404
    elif location:
        return jsonify(error={"Not Found": f"Sorry, we do not have a cafe in {location}."}), 404
    else:
        return jsonify(error={"Not Found": f"Sorry, we do not have a cafe called {name}."}), 404


# HTTP POST - Create Record

@app.route("/add/<string:password>", methods=["POST"])
def add(password):
    if password != my_secure_password:
        return jsonify(error={"Forbidden": "You do not have permission to add a new cafe."}), 403
    new_cafe = Cafe(
        name=request.form.get("name", "").title(),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location", "").title(),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": f"Successfully added the new cafe with id {new_cafe.id} and name {new_cafe.name}."})


# HTTP PUT/PATCH - Update Record

@app.route("/update_price/<int:cafe_id>/<string:password>", methods=["PUT", "PATCH"])
def update_price(cafe_id, password):
    if password != my_secure_password:
        return jsonify(error={"Forbidden": "You do not have permission to update the price of this cafe."}), 403
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        new_price = request.form.get("new_price")
        if new_price:
            # Fix: capture old price first
            old_price = cafe.coffee_price
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(response={"success": f"Successfully updated the price of {cafe.name} from {old_price} to {new_price}."})
        return jsonify(error={"Bad Request": "Provide 'new_price' parameter."}), 400
    return jsonify(error={"Not Found": "No cafe with that id."}), 404


# HTTP DELETE - Delete Record

@app.route("/close_cafe/<int:cafe_id>/<string:password>", methods=["DELETE"])
def close_cafe(cafe_id, password):
    if password != my_secure_password:
        return jsonify(error={"Forbidden": "You do not have permission to delete this cafe."}), 403
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": f"Successfully closed the cafe with id {cafe.id} and name {cafe.name}."})
    return jsonify(error={"Not Found": "No cafe with that id."}), 404


if __name__ == '__main__':
    app.run(debug=True)
