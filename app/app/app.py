from model import db
from model import Client,Booking,Flight,Airport,Route,Country,City,Departure_Airport,Arrival_Airport,Aircraft_Model,Aircraft,Pilot,Technician,Cabin_Member,Client,Ticket,Admin,Check
from model import app
from flask import request
import random
import json
import datetime
from flask import render_template


def find_user_type(email,password):
    user_type = ""
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
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/logout')
def logout():
    return 'Logout'






@app.route('/api/login', methods=['GET','POST'])
def login3():
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
        reservation["booking_code"] = r.id
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
    print(user_reservations)
    return user_reservations

@app.route('/api/get_user_reservations', methods=['GET','POST'])
def get_user_reservations():
    response = {}
    content = request.get_json()
    print(content)
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
        ticket["price"] = t.last_price
        ticket["booking_id"] = booking_id
        ticket["seat_no"] = t.seat_no

        booking_tickets.append(ticket)
    return booking_tickets

@app.route('/api/get_booking_tickets', methods=['GET','POST'])
def get_booking_tickets():
    response = {}
    content = request.get_json()
    print(content)
    booking_id = content["booking_id"]
    tickets = get_booking_tickets_db(booking_id)
    response["tickets"] = tickets
    return json.dumps(response,indent=True)




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
        ticket = f.tickets[0]
        aircraft_model = f.aircraft.model
        capacity = aircraft_model.number_of_col * aircraft_model.number_of_row
        sold = len(ticket.flight.tickets)
        price = ticket.price
        last_price = 0.5*price + (sold/capacity)*3*price
        flight["price"] = last_price
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
    
    response['flights'] = flight_by_route
    return json.dumps(response)


def get_flight_info_with_flight_id_db(flight_id):
    flight_info = {}
    flight = db.session.query(Flight).filter_by(id=flight_id).first()
    dep_date = flight.estimated_departure_date_time
    dep_airport_code = flight.route.departure_airport.dep_airport.code[1:-1]
    arr_airport_code = flight.route.arrival_airport.ar_airport.code[1:-1]
    route_string = dep_airport_code + " - " + arr_airport_code
            
    flight_info["flight_id"] = flight.id
        
    flight_info["dep_airport_code"] = dep_airport_code
    flight_info["arr_airport_code"] = arr_airport_code
    flight_info["estimated_departure_date_time"] = str(flight.estimated_departure_date_time).split('.')[0]
    flight_info["estimated_arrival_date_time"] = str(flight.estimated_arrival_date_time).split('.')[0] 
    flight_info["route"] = route_string

    
    ticket = flight.tickets[0]
    aircraft_model = flight.aircraft.model
    capacity = aircraft_model.number_of_col * aircraft_model.number_of_row
    sold = len(ticket.flight.tickets)
    price = ticket.price
    last_price = 0.5*price + (sold/capacity)*3*price
    flight_info["price"] = last_price



    return flight_info



@app.route('/api/get_flight_info_with_flight_id', methods=['GET','POST'])
def get_flight_info_with_flight_id():
    response = {}
    content = request.get_json()
    flight_id = content["flight_id"]
    flight_info = get_flight_info_with_flight_id_db(flight_id)
    print(flight_info)
    response = flight_info
    return json.dumps(response)



def register_as_client(firstname,lastname,password,email,phone_number):
    client = db.session.query(Client).filter_by(email=email).first()
    print(client)
    if client:
        return False
    client = Client(firstname=firstname,lastname=lastname,phone_number=phone_number,email=email,password=password)
    db.session.add(client)
    db.session.commit()
    return True

@app.route('/api/register_client', methods=['GET','POST'])
def register_client():
    response = {}
    content = request.get_json()
    print(content)
    firstname = content["firstname"]
    lastname = content["lastname"]
    password = content["password"]
    email = content["email"]
    phone_number = content["phone_number"]

    result = register_as_client(firstname,lastname,password,email,phone_number)

    response["result"] = result 
    return json.dumps(content)


def assign_client_to_flight(flight_id,email):
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

@app.route('/api/register_booking', methods=['GET','POST'])
def register_booking():
    response = {}
    content = request.get_json()
    print(content)
    email = content["email"]
    flights = content["flights_str"].split(",")[1:]


    client = db.session.query(Client).filter_by(email=email).first()

    booking_obj = Booking(client=client,booking_code=random.randint(1000*1000,9999*1000))
    db.session.add(booking_obj) 
    db.session.commit()


    booking_tickets = []

    for flight_id in flights:
        if not flight_id:
            continue
        flight = db.session.query(Flight).filter_by(id=flight_id).first()
        tickets = flight.tickets
        ticket_index = random.randint(0,len(tickets)-1)
        ticket = tickets[ticket_index]
        

        ticket = flight.tickets[0]
        aircraft_model = flight.aircraft.model
        capacity = aircraft_model.number_of_col * aircraft_model.number_of_row
        sold = len(ticket.flight.tickets)
        price = ticket.price
        last_price = 0.5*price + (sold/capacity)*3*price

        ticket.last_price = last_price
        ticket.is_avaliable = False
        print(flight_id)
        ticket.booking = booking_obj
        
        db.session.add(ticket)
        db.session.commit()
    print(booking_tickets)

   

        
    return json.dumps(response)


@app.route('/api/sql', methods=['GET','POST'])
def sql():
    response = {}
    content = request.get_json()
    print(content)
    sql = content["sql"]
    resultproxy = db.session.execute(sql)

    d, a = {}, []
    for rowproxy in resultproxy:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            if type(value) == datetime.datetime:
                value = str(value)
            d = {**d, **{column: value}}
        a.append(d)
    #response["result"] = result
    
    response["result"] = a
    return json.dumps(response,indent=True)





if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
