from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/mustafa/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mustafa:magic_pass@localhost:5432/test'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)



class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False) #HASH
    first_name = db.Column(db.String(80))
    reservations = db.relationship("Booking", back_populates="client")

    def __repr__(self):
        return '<client_id %r>' % self.id  


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client = db.relationship("Client", back_populates="reservations")

    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'))
    flight = db.relationship("Flight", back_populates="bookings")
    def __repr__(self):
        return '<booking_id %r>' % self.id  
    
    
    

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookings = db.relationship("Booking",back_populates="flight")

    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))
    route = db.relationship("Route", back_populates="flights")

    aircraft_id = db.Column(db.Integer, db.ForeignKey('aircraft.id'))
    aircraft = db.relationship("Aircraft", back_populates="used_flights")

    actual_departure_date_time = db.Column(db.Date)
    actual_arrival_date_time = db.Column(db.Date)
    
    estimated_departure_date_time = db.Column(db.Date)
    estimated_arrival_date_time = db.Column(db.Date)
    

class Aircraft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_of_seats = db.Column(db.Integer)
    company = db.Column(db.String(120), unique=True, nullable=False)#table eklenecek
    model = db.Column(db.String(120), unique=True, nullable=False)#table eklenecek
    used_flights = db.relationship("Flight", back_populates="aircraft")
    checks = db.relationship("Check", back_populates="aircraft")
class Check(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date=db.Column(db.Date)
    is_checked = db.Column(db.Boolean)
    aircraft_id = db.Column(db.Integer, db.ForeignKey('aircraft.id'))
    aircraft = db.relationship("Aircraft", back_populates="checks")

    technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'))
    technician = db.relationship("Technician", back_populates="responsible_checks")
    
class Technician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    responsible_checks = db.relationship("Check", back_populates="technician")
    firstname = db.Column(db.String(120))
    lastname = db.Column(db.String(120))
    salary = db.Column(db.Integer)

    





class Departure_Airport(db.Model):
    __tablename__ = 'departure_airport'
    id = db.Column(db.Integer, primary_key=True)
    route = db.relationship("Route", back_populates="departure_airport")

    airport_id = db.Column(db.Integer, db.ForeignKey('airport.id'))
    dep_airport = db.relationship("Airport", back_populates="as_departure")
    
class Arrival_Airport(db.Model):
    __tablename__ = 'arrival_airport'
    id = db.Column(db.Integer, primary_key=True)
    route = db.relationship("Route", back_populates="arrival_airport")
    
    airport_id = db.Column(db.Integer, db.ForeignKey('airport.id'))
    ar_airport = db.relationship("Airport", back_populates="as_arrival")
    

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flights = db.relationship("Flight", back_populates="")
    departure_airport_id = db.Column(db.Integer, db.ForeignKey('departure_airport.id'))
    departure_airport = db.relationship("Departure_Airport", back_populates="route")
    
    arrival_airport_id = db.Column(db.Integer, db.ForeignKey('arrival_airport.id'))
    arrival_airport = db.relationship("Arrival_Airport", back_populates="route")



class Airport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    as_arrival = db.relationship("Arrival_Airport",back_populates="ar_airport")
    as_departure =  db.relationship("Departure_Airport",back_populates="dep_airport")
    

    name = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False) #table oluşturulacak
    country = db.Column(db.String(80), nullable=False) #table oluşturulacak
    code = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return '<Airport_name %r>' % self.name  


"""
class Fligt_Team(db.Model):
    pilot =  db.Model(db.Integer, primary_key=True)
    #estimated_departure_date = 
class Route(db.Model):
    route_id = db.Model(db.Integer, primary_key=True)
    #departure_airport_id = 
    arrival_airport_id =
class Airport(db.Model):
    airport_id = db.Column(db.DateTime)"""
