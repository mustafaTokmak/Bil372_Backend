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

    tickets = db.relationship("Ticket", back_populates="booking")
    #extras
    def __repr__(self):
        return '<booking_id %r>' % self.id  
    
    
    
 
    
pilots_table = db.Table('pilots_table',
    db.Column('flight_id', db.Integer, db.ForeignKey('flight.id')),
    db.Column('pilot_id', db.Integer, db.ForeignKey('pilot.id'))
)

cabin_crew = db.Table('cabin_crew',
    db.Column('flight_id', db.Integer, db.ForeignKey('flight.id')),
    db.Column('cabin_member_id', db.Integer, db.ForeignKey('cabin_member.id'))
)

pilot_speciality = db.Table('pilot_speciality',
    db.Column('pilot_id', db.Integer, db.ForeignKey('pilot.id')),
    db.Column('aircraft_model_id', db.Integer, db.ForeignKey('aircraft_model.id'))
)
class Flight(db.Model):
    __tablename__ = 'flight'
    id = db.Column(db.Integer, primary_key=True)

    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))
    route = db.relationship("Route", back_populates="flights")

    aircraft_id = db.Column(db.Integer, db.ForeignKey('aircraft.id'))
    aircraft = db.relationship("Aircraft", back_populates="used_flights")

    actual_departure_date_time = db.Column(db.Date)
    actual_arrival_date_time = db.Column(db.Date)
    
    estimated_departure_date_time = db.Column(db.Date)
    estimated_arrival_date_time = db.Column(db.Date)

    pilots = db.relationship("Pilot",secondary=pilots_table,back_populates="flights")
    cabin_crew = db.relationship("Cabin_Member",secondary=cabin_crew,back_populates="flights")

    tickets = db.relationship("Ticket", back_populates="flight")
    



class Pilot(db.Model):
    __tablename__ = 'pilot'
    id = db.Column(db.Integer, primary_key=True)
    flights = db.relationship("Flight",secondary=pilots_table,back_populates="pilots")
    firstname = db.Column(db.String(120))
    lastname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False) #HASH
    
    salary = db.Column(db.Integer)
    speciality_models = db.relationship("Aircraft_model",secondary=pilot_speciality, back_populates="pilots")
    experience = (db.Integer)
    #if aircraft seat == bu uçuşa ait satılmış bilet sayısı
class Cabin_Member(db.Model):
    __tablename__ = 'cabin_member'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(120))
    lastname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False) #HASH
    
    salary = db.Column(db.Integer)
    flights = db.relationship("Flight",secondary=cabin_crew,back_populates="cabin_crew")


technician_speciality = db.Table('technician_speciality',
    db.Column('technician_id', db.Integer, db.ForeignKey('technician.id')),
    db.Column('aircraft_model_id', db.Integer, db.ForeignKey('aircraft_model.id'))
)
class Technician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    responsible_checks = db.relationship("Check", back_populates="technician")
    firstname = db.Column(db.String(120))
    lastname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False) #HASH
    
    salary = db.Column(db.Integer)
    
    model_id = db.Column(db.Integer, db.ForeignKey('aircraft_model.id'))
    speciality_models = db.relationship("Aircraft_model",secondary=technician_speciality, back_populates="technicians")

class Technician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    responsible_checks = db.relationship("Check", back_populates="technician")
    firstname = db.Column(db.String(120))
    lastname = db.Column(db.String(120))
    salary = db.Column(db.Integer)
    
    model_id = db.Column(db.Integer, db.ForeignKey('aircraft_model.id'))
    speciality_models = db.relationship("Aircraft_model",secondary=technician_speciality, back_populates="technicians")


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price =  db.Column(db.Integer)
    is_avaliable = db.Column(db.Boolean,default=True)
    
    is_checked_in = db.Column(db.Boolean,default=False)

    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'))
    booking = db.relationship("Booking", back_populates="tickets")
    
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'))
    flight = db.relationship("Flight", back_populates="tickets")
    
    seat_no = db.Column(db.Integer)

class Aircraft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_of_col = db.Column(db.Integer)
    number_of_row = db.Column(db.Integer)
    
    model_id = db.Column(db.Integer, db.ForeignKey('aircraft_model.id'))
    model = db.relationship("Aircraft_model", back_populates="aircrafts")

    used_flights = db.relationship("Flight", back_populates="aircraft")
    checks = db.relationship("Check", back_populates="aircraft")

class Aircraft_model(db.Model):
    __tablename__ = 'aircraft_model'
    id = db.Column(db.Integer, primary_key=True)
    aircrafts = db.relationship("Aircraft", back_populates="model")

    technicians = db.relationship("Technician",secondary=technician_speciality, back_populates="speciality_models")

    pilots = db.relationship("Pilot",secondary=pilot_speciality, back_populates="speciality_models")
    

    model_name = db.Column(db.String(120))

class Check(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    is_checked = db.Column(db.Boolean)
    aircraft_id = db.Column(db.Integer, db.ForeignKey('aircraft.id'))
    aircraft = db.relationship("Aircraft", back_populates="checks")

    technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'))
    technician = db.relationship("Technician", back_populates="responsible_checks")
    


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
    flights = db.relationship("Flight", back_populates="route")
    departure_airport_id = db.Column(db.Integer, db.ForeignKey('departure_airport.id'))
    departure_airport = db.relationship("Departure_Airport", back_populates="route")
    
    arrival_airport_id = db.Column(db.Integer, db.ForeignKey('arrival_airport.id'))
    arrival_airport = db.relationship("Arrival_Airport", back_populates="route")



class Airport(db.Model):
    __tablename__ = 'airport'
    id = db.Column(db.Integer, primary_key=True)
    as_arrival = db.relationship("Arrival_Airport",back_populates="ar_airport")
    as_departure =  db.relationship("Departure_Airport",back_populates="dep_airport")
    

    name = db.Column(db.String(80), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    city = db.relationship('City',back_populates="airports")
    
    code = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return '<Airport_name %r>' % self.name  

class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    cities = db.relationship('City',back_populates="country")
class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship('Country',back_populates="cities")

    airports = db.relationship('Airport',back_populates="city")

