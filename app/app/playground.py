from model import db
from model import Client,Booking,Flight,Airport,Route,Country,City,Departure_Airport,Arrival_Airport,Aircraft_Model,Aircraft,Pilot,Technician,Cabin_Member,Client,Ticket,Admin,Check
import random
import hashlib
import datetime 
import string

db.create_all()
import time 
start = time.time()


departure_airport_code = "Brussels Airport"
departure_airport = Airport.query.filter_by(name="BRU").first()
print(departure_airport.code)
