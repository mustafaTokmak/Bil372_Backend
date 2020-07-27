from model import db
from model import Client,Booking,Flight,Airport,Route,Country,City,Departure_Airport,Arrival_Airport,Aircraft_Model,Aircraft,Pilot,Technician,Cabin_Member,Client,Ticket,Admin,Check

import hashlib
import datetime
from sqlalchemy import func
from sqlalchemy import desc


#add client 
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

password_plain_text = "1234asdf"
m = hashlib.sha256()
m.update(password_plain_text.encode())
password = m.digest().hex()
find_user_type("mustafa99263tokmak42823@airline.com",password)


# tarih aralığındaki rotadaki uçuşlar
def find_all_flights(start_date,end_date):
    flights_query = db.session.query(Flight).filter(Flight.estimated_departure_date_time > start_date).filter(Flight.estimated_departure_date_time < end_date )
    print(len(flights_query.all()))
    return flights_query

def find_city_to_city(start_date,end_date,departure_city,arrival_city):
    avaliable_date_flights_query = find_all_flights(start_date,end_date)
    #create route 
    #departure_city_obj = db.session.query(Flight).filter_by(name=departure_city).first()
    #arrival_city_obj = db.session.query(Flight).filter_by(name=arrival_city)
    Departure_Airport 
    Arrival_Airport
    print(departure_city)
    #route = db.session.query(Route).join(Route.departure_airport).join(Departure_Airport.dep_airport).join(Airport).filter_by(Route.departure_airport.dep_airport.city.name__eq__(departure_city)).all()
    dep_city = db.session.query(City).filter_by(name=departure_city).first()
    arr_city = db.session.query(City).filter_by(name=arrival_city).first()
    
    dep_airport = db.session.query(Airport).filter_by(city=dep_city).first()
    ar_airport = db.session.query(Airport).filter_by(city=arr_city).first()
    print(ar_airport.name)

    departure_airport = db.session.query(Departure_Airport).filter_by(dep_airport=dep_airport).first()
    arrival_airport = db.session.query(Arrival_Airport).filter_by(ar_airport=ar_airport).first()
    
    route = db.session.query(Route).filter_by(departure_airport=departure_airport,arrival_airport=arrival_airport).first()
    flights = avaliable_date_flights_query.filter_by(route=route).all()

    for f in flights:
        print("From: "+ dep_airport.name + " To: " + ar_airport.name +" Flight id "+str(f.id) +"  Departure Date: " +str(f.estimated_departure_date_time))
    return flights
    #route = db.session.query(Route).join(Route.departure_airport).join(Route.departure_airport.dep_airport).join(Route.departure_airport.dep_airport.city).filter(Route.departure_airport.dep_airport.city.name==departure_city).all()
    #print(len(route))

start_date =  datetime.datetime.now()
end_date = start_date + datetime.timedelta(days=180)

departure_city = "Fort Hope"
arrival_city = "Dubendorf"
flights = find_city_to_city(start_date,end_date,departure_city,arrival_city)
flight_id = 5 #flights[0].id

# koltuk seçimi ve bileti alma 
def get_avaliable_tickets_for_flight_id(flight_id):
    all_tickets =  db.session.query(Ticket).join(Flight).filter(Flight.id==flight_id).all()
    tickets = db.session.query(Ticket).join(Flight).filter(Flight.id==flight_id).filter(Ticket.is_avaliable==True).all()
    print(len(all_tickets))
    print(len(tickets))

    
    return tickets
tickets = get_avaliable_tickets_for_flight_id(flight_id)
print("get_avaliable_tickets_for_flight_id")
print(len(tickets))
#print(tickets)
# uçuş bilgileri booking no seat no vs 

# pilot kendi uçuşlarını sırasıyla görme 
def get_pilot_flights(email):
    flights = db.session.query(Pilot).filter_by(email=email).first().flights
    for f in flights:
        print(str(f.estimated_departure_date_time))
    #TODO sort flights
    return flights
pilot_email = "mustafa9166tokmak6229@airline.com"

flights = get_pilot_flights(pilot_email)
print("get_pilot_flights")
print(len(flights))

#technician

#crew 
def get_cabin_member_flights(email):
    flights = db.session.query(Cabin_Member).filter_by(email=email).first().flights
    for f in flights:
        print(str(f.estimated_departure_date_time))
        print(str(f.estimated_departure_date_time))
    #TODO sort flights
    return flights
cabin_member_email = "mustafa7565tokmak4096@airline.com"

flights = get_cabin_member_flights(cabin_member_email)
print("get_cabin_member_flights")
print(len(flights))


# en çok uçan pilot 
#TODO flight duration eklenecek
def get_most_flights_pilot():
    a = db.session.query(Pilot).join(Pilot.flights).query(func.sum(Flight.score).label("total_score"))
    print(len(a))
#print("get_most_flights_pilot")
#get_most_flights_pilot()



# en çok uçan uçak

# en çok bakım yapan teknisyen 

#uçaga 

# pilot uçuş iptal

# 2 şehir arası uçuş var mı 

def get_all_check_for_technician(email):
    flights = db.session.query(Technician).filter_by(email=email).first().flights
    return flights

#Expected income = capacity * price
# en pahalı bilet 
def get_most_expensive_sold_ticket():
    ticket = db.session.query(Ticket).filter(Ticket.last_price != None).order_by(desc(Ticket.last_price)).first()
    print(type(ticket))
    return ticket
print("get_most_expensive_sold_ticket")
ticket = get_most_expensive_sold_ticket()
print(ticket.price)

# en çok para getiren uçuş
def get_most_income_flight():
    income = func.sum(Ticket.last_price).label('income')
    most_income_flight_id, income = db.session.query(Ticket.flight_id,income).filter(Ticket.last_price != None).group_by(Ticket.flight_id).order_by(income.desc()).first()
    most_income_flight = db.session.query(Flight).filter_by(id=most_income_flight_id).first()
    print(most_income_flight.id)
    print(income)
    return most_income_flight,income
get_most_income_flight()

def get_min_income_flight():
    income = func.sum(Ticket.last_price).label('income')
    min_income_flight_id, income = db.session.query(Ticket.flight_id,income).filter(Ticket.last_price != None).group_by(Ticket.flight_id).order_by(income.asc()).first()
    min_income_flight = db.session.query(Flight).filter_by(id=min_income_flight_id).first()
    print(min_income_flight.id)
    print(income)
    return min_income_flight,income
get_min_income_flight()

def get_min_income_rate_flight():
    return 1
def get_max_income_rate_flight():
    return 1

def get_client_booking_info(client_email):
    return 1



# yenisini ekle  
# en az para getiren uçuş 

# admin yeni uçuş ekler pilot ve crew otomatik 
#verilen rotaya yeni uçuş ekle otomatik 
def add_new_flight_with_route(departure_date,departure_city,arrival_city):
    return 1