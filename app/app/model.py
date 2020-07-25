from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/mustafa/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mustafa:magic_pass@localhost:5432/test'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)



class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client = db.relationship("Client", back_populates="reservations")
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False) #HASH
    first_name = db.Column(db.String(80))
    reservations = db.relationship("Booking", back_populates="client")

    def __repr__(self):
        return '<client_id %r>' % self.id  


        #flight_id = db.Column(db.Integer, db.ForeignKey('flight.flight_id'))
    
"""
class Flight(db.Model):
    flight_id = db.Model(db.Integer, primary_key=True)
    #flight_team_id = 
    reservations = db.relationship("Booking")

class Fligt_Team(db.Model):
    pilot =  db.Model(db.Integer, primary_key=True)
    #estimated_departure_date = 
class Route(db.Model):
    route_id = db.Model(db.Integer, primary_key=True)
    #departure_airport_id = 
    arrival_airport_id =
class Airport(db.Model):
    airport_id = db.Column(db.DateTime)"""
