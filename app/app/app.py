from model import db
from model import Client,Booking,Flight,Airport,Route,Country,City
from model import app
from flask import request
import random
import json
import datetime


def find_user_type(email,password):
    user_type = ""
    print(db.session.query(Client).filter_by(email=email,password=password))
    if db.session.query(Client).filter_by(email=email,password=password).first():
        print("Client")
        user_type = "Client"
    if db.session.query(Cabin_Member).filter_by(email=email,password=password).first():
        print("Cabin_Member")
        user_type = "Cabin_Member"
    if db.session.query(Pilot).filter_by(email=email,password=password).first():
        print("Pilot")
        user_type = "Pilot"
    if db.session.query(Technician).filter_by(email=email,password=password).first():
        print("Technician")
        user_type = "Technician"
    if db.session.query(Admin).filter_by(email=email,password=password).first():
        print("Admin")
        user_type = "Admin"
    return user_type


@app.route('/')
def hello_world():
    return 'Hello, World!'






@app.route('/api/register_as_client', methods=['GET','POST'])
def register_as_client():
    response = {}
    content = request.get_json()
    for i in range(10):
        client_id = random.randint(0,100000000)
        phone_number = "admin" + str(random.randint(0,10000000000))
        email = "admin@example.com" + str(random.randint(0,10000000000))
        password = str(random.randint(0,10000000000))
        first_name = "mustafa" + str(random.randint(0,10000000000))
        
        client = Client(phone_number=phone_number,email=email,password=password,first_name=first_name)
        db.session.add(client)
        db.session.commit()
    return json.dumps(response)




@app.route('/api/login', methods=['GET','POST'])
def login():
    response = {}
    content = request.get_json()
    email = content["email"]
    password = content["password"]
    user_type = find_user_type(email,password)
    response["user_type"] = user_type
    return json.dumps(response)

def get_user_reservations_db(email):
    client = db.session.query(Client).filter_by(email=email).first()
    reservations = db.session.query(Booking).filter_by(client=client).all()
    print(len(reservations))
    user_reservations = []
    for r in reservations:
        reservation = {}
        reservation["booking_code"] = r.booking_code
        reservation["flights"] = []
        for t in r.tickets:
            flight = {}
            dep_date = t.flight.estimated_departure_date_time
            dep_airport_code = t.flight.route.departure_airport.dep_airport.code[1:-1]
            arr_airport_code = t.flight.route.arrival_airport.ar_airport.code[1:-1]
            print(dep_airport_code)
            print(arr_airport_code)
            route_string = dep_airport_code + " - " + arr_airport_code
            flight["depature_time"] = str(dep_date).split('.')[0]
            flight["route"] = route_string
            reservation["flights"].append(flight)
        user_reservations.append(reservation)
    return user_reservations

@app.route('/api/get_user_reservations', methods=['GET','POST'])
def get_user_reservations():
    response = {}
    content = request.get_json()
    email = content["email"]
    
    reservations = get_user_reservations_db(email)
    response["reservations"] = reservations
    return json.dumps(response)



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

        booking_tickets.append(ticket)
    return booking_tickets

@app.route('/api/get_booking_tickets', methods=['GET','POST'])
def get_booking_tickets():
    response = {}
    content = request.get_json()
    booking_id = content["booking_id"]
    tickets = get_booking_tickets_db(booking_id)
    response["tickets"] = tickets
    return json.dumps(response)




def check_in_ticket_db(ticket_id):
    ticket = db.session.query(Ticket).filter_by(id=ticket_id).first()
    ticket.is_checked_in = True
    db.session.add(client_obj)
    db.session.commit()
    return True

@app.route('/api/check_in_ticket', methods=['GET','POST'])
def check_in_ticket():
    response = {}
    content = request.get_json()
    ticket_id = content["ticket_id"]
    result = check_in_ticket_db(ticket_id)
    
    response["result"] = str(result)
    return json.dumps(response)



@app.route('/api/get_avaliable_tickets_for_flight', methods=['GET','POST'])
def get_avaliable_tickets_for_flight():
    response = {}
    content = request.get_json()
    dep_city_name = content["dep_city_name"]
    arr_city_name = content["arr_city_name"]
    flights = get_avaliable_tickets_for_flight(flight_id)
    response["flights"] = flights
    
    return json.dumps(response)


def get_flight_by_route_db(dep_city_name,arr_city_name):
    dep_city = db.session.query(City).filter_by(name=dep_city_name).first()
    arr_city = db.session.query(City).filter_by(name=arr_city_name).first()
    print(dep_city.id)
    print(arr_city.id)

    dep_city_airport = db.session.query(Airport).filter_by(city=dep_city).first()
    arr_city_airport = db.session.query(Airport).filter_by(city=arr_city).first()
    print(dep_city_airport.id)
    print(arr_city_airport.id)


    departure_airport = db.session.query(Departure_Airport).filter_by(dep_airport=dep_city_airport).first()
    arrival_airport = db.session.query(Arrival_Airport).filter_by(ar_airport=arr_city_airport).first()
    print(departure_airport.id)
    print(arrival_airport.id)
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

@app.route('/api/get_flight_by_route', methods=['GET','POST'])
def get_flight_by_route():
    response = {}
    content = request.get_json()
    dep_city_name = content["dep_city_name"]
    arr_city_name = content["arr_city_name"]

    flight_by_route = get_flight_by_route_db(dep_city_name,arr_city_name)
    
    response['flight'] = flight_by_route
    return json.dumps(response)





@app.route('/register_booking', methods=['GET','POST'])
def register_booking():
    response = {}
    content = request.get_json()
    for i in range(100):
        client = Client.query.all()[i%10]
        
        print(client)
        booking = Booking(client_id=client.id)
        db.session.add(booking)
        db.session.commit()
    return json.dumps(response)


        

        
    return json.dumps(response)





if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
