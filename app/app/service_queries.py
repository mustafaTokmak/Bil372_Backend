
from model import db
from model import Client,Booking,Flight,Airport,Route,Country,City,Departure_Airport,Arrival_Airport,Aircraft_Model,Aircraft,Pilot,Technician,Cabin_Member,Client,Ticket,Admin,Check
import json
import hashlib
import datetime
from sqlalchemy import func
from sqlalchemy import desc

def register_as_client_db():
    client_obj = Client(firstname=firstname,lastname=lastname,phone_number=phone_number,email=email,password=password)
    result = True
def get_user_reservations_db(email):
    client = db.session.query(Client).filter_by(email=email).first()
    reservations = db.session.query(Booking).filter_by(client=client).all()
    print(len(reservations))
    user_reservations = []
    for r in reservations:
        reservation = {}
        reservation["booking_code"] = r.booking_code
        reservation["booking_id"] = r.id
        reservation["flights"] = []
        for t in r.tickets:
            flight = {}
            dep_date = t.flight.estimated_departure_date_time
            dep_airport_code = t.flight.route.departure_airport.dep_airport.code[1:-1]
            arr_airport_code = t.flight.route.arrival_airport.ar_airport.code[1:-1]
            route_string = dep_airport_code + " - " + arr_airport_code
            flight["depature_time"] = str(dep_date).split('.')[0]
            flight["route"] = route_string
            reservation["flights"].append(flight)
        user_reservations.append(reservation)
    return user_reservations

email = "mustafa13802tokmak74066@airline.com"
a = get_user_reservations_db(email)
print(len(a))
#print(json.dumps(a,indent=True))


def get_pilot_flights(email):
    
    pilot_flights = 
    return pilot_flights

def get_booking_tickets_db(booking_id):
    tickets = db.session.query(Booking).filter_by(id=booking_id).first().tickets
    booking_tickets = []
    for t in tickets:
        ticket = {}
        dep_date = t.flight.estimated_departure_date_time
        arr_date = t.flight.estimated_departure_date_time
        dep_airport_code = t.flight.route.departure_airport.dep_airport.code[1:-1]
        arr_airport_code = t.flight.route.arrival_airport.ar_airport.code[1:-1]
        route_string = dep_airport_code + " - " + arr_airport_code
        ticket["depature_time"] = str(dep_date).split('.')[0]
        ticket["arrival_time"] = str(arr_date).split('.')[0]
        ticket["route"] = route_string
        ticket["price"] = route_string
        ticket["booking_id"] = booking_id
        ticket["seat_no"] = t.seat_no
        ticket["ticket_id"] = t.id
        

        booking_tickets.append(ticket)
    return booking_tickets
booking_id = 4265
#a = get_booking_tickets_db(booking_id)
#print(json.dumps(a,indent=True))

def check_in_ticket_db(ticket_id):
    ticket = db.session.query(Ticket).filter_by(id=ticket_id).first()
    ticket.is_checked_in = True
    db.session.add(client_obj)
    db.session.commit()
    return True


import datetime
def get_flight_by_route_db(dep_city_name,arr_city_name):
    dep_city = db.session.query(City).filter_by(name=dep_city_name).first()
    arr_city = db.session.query(City).filter_by(name=arr_city_name).first()

    dep_city_airport = db.session.query(Airport).filter_by(city=dep_city).first()
    arr_city_airport = db.session.query(Airport).filter_by(city=arr_city).first()

    departure_airport = db.session.query(Departure_Airport).filter_by(dep_airport=dep_city_airport).first()
    arrival_airport = db.session.query(Arrival_Airport).filter_by(ar_airport=arr_city_airport).first()
    route = db.session.query(Route).filter_by(departure_airport=departure_airport).filter_by(arrival_airport=arrival_airport).order_by().first()
    now = datetime.datetime.now()

    flights = db.session.query(Flight).filter_by(route=route).filter(Flight.estimated_departure_date_time > now ).order_by(Flight.estimated_departure_date_time).all()
    flight_by_route = []
    for f in flights:
        flight = {}
        flight["estimated_departure_date_time"] = str(f.estimated_departure_date_time).split('.')[0]
        flight["estimated_arrival_date_time"] = str(f.estimated_arrival_date_time).split('.')[0] 
        flight["flight_id"] = f.id


        
        flight_by_route.append(flight)
        print(f.estimated_departure_date_time)

    return flight_by_route

arr_city = "Izmir"
dep_city = "Adana"

flights = get_flight_by_route_db(dep_city,arr_city)
print(len(flights))

#print(json.dumps(flights,indent=True))

def get_avaliable_tickets_for_flight(flight_id):
    flight = db.session.query(Flight).filter_by(id=flight_id).first()
    number_of_col = flight.aircraft.model.number_of_col
    number_of_row = flight.aircraft.model.number_of_row
    tickets = db.session.query(Ticket).filter_by(flight=flight).filter_by(is_avaliable=True).all()
    avaliable_tickets = []
    response = {}


    capacity = number_of_col * number_of_row
    sold = capacity - len(tickets)
    price = tickets[0].price
    last_price = 0.5*price + (sold/capacity)*3*price # ilk bilet yarı fiyatı son bilet 3.5 kat fiyatı
    is_avaliable = False
    for t in tickets:
        ticket = {}
        ticket['ticket_id'] = t.id
        ticket['seat_no'] = t.seat_no
        ticket['price'] = price


        avaliable_tickets.append(ticket)

    response["avaliable_tickets"] = avaliable_tickets
    response["number_of_col"] = number_of_col
    response["number_of_row"] = number_of_row
    
    return response
def create_new_booking(email,ticket_ids):


    return True

flight_id = 1
tickets = get_avaliable_tickets_for_flight(flight_id)
print(json.dumps(tickets,indent=True))
