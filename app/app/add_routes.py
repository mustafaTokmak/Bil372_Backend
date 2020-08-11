from model import db
from model import Client,Booking,Flight,Airport,Route,Country,City,Departure_Airport,Arrival_Airport,Aircraft_Model,Aircraft,Pilot,Technician,Cabin_Member,Client,Ticket,Admin,Check
import random
import hashlib
import datetime 
import string

db.create_all()
import time 
start = time.time()

with open('routes.csv','r') as f:
    data = f.readlines()
with open('routes.csv','r') as f:
    data = f.readlines()


required_airport_ids = []
route_ids = []
for i in range(len(data)):
    pc = data[i].split(',')[0]
    if pc != 'PC':
            continue
    airport_id1 = data[i].split(',')[3]
    airport_id2 = data[i].split(',')[5]
    if not airport_id1 in required_airport_ids:
            required_airport_ids.append(airport_id1)
    if not airport_id2 in required_airport_ids:
            required_airport_ids.append(airport_id2)
    
counter = 0



with open('new_airports.csv','r') as f:
    data = f.readlines()
cities = []
counter = 0
for row in data:
    airport_id = row.split(',')[0]
   
    airport_name = row.split(',')[1]
    city = row.split(',')[2][1:-1]
   
    country = str(row.split(',')[3][1:-1])
    code = row.split(',')[4]
    country_obj = Country(name=country)
    if (Country.query.filter_by(name=country).first()):
        country_obj = Country.query.filter_by(name=country).first()
    else:
        db.session.add(country_obj)
        
    #print(city)
    city_obj = City(country=country_obj,name=city)
    if(City.query.filter_by(country=country_obj,name=city).first()):
        city_obj = City.query.filter_by(country=country_obj,name=city).first()
    else:
        db.session.add(city_obj)
    
    airport_obj = Airport(name=airport_name,city=city_obj,code=code,id=airport_id)
    if (Airport.query.filter_by(city=city_obj,name=airport_name).first()):
        airport_obj = Airport.query.filter_by(city=city_obj,name=airport_name).first()
    else:
        db.session.add(airport_obj)
    counter += 1
    if(counter % 100 ==0):
        print(counter)

    db.session.commit()

last = time.time()
t = last - start
print("time"+str(t))

counter=0
with open('new_routes.csv','r') as f:
    data = f.readlines()

for row in data:
    airline_id = row.split(',')[0]

   
    departure_airport_id = (row.split(',')[3])
    arrival_airport_id = (row.split(',')[5])
    print(departure_airport_id)
    print(arrival_airport_id)
    
    departure_airport = Airport.query.filter_by(id=departure_airport_id).first()
    print(departure_airport.name)
    arrival_airport = Airport.query.filter_by(id=arrival_airport_id).first()
    print(arrival_airport.name)


    dep_obj = Departure_Airport(dep_airport=departure_airport)
    if Departure_Airport.query.filter_by(dep_airport=departure_airport).first():
        dep_obj = Departure_Airport.query.filter_by(dep_airport=departure_airport).first()
    else:
        db.session.add(dep_obj)
    print(dep_obj.id)
    arr_obj = Arrival_Airport(ar_airport=arrival_airport)
    if Arrival_Airport.query.filter_by(ar_airport=arrival_airport).first():
        arr_obj = Arrival_Airport.query.filter_by(ar_airport=arrival_airport).first()
    else:
        db.session.add(arr_obj)
    print(arr_obj.id)
    route_obj = Route(departure_airport=dep_obj,arrival_airport=arr_obj)
    if Route.query.filter_by(departure_airport=dep_obj,arrival_airport=arr_obj).first():
        route_obj = Route.query.filter_by(departure_airport=dep_obj,arrival_airport=arr_obj).first()
    else:
        db.session.add(route_obj)
    counter += 1
    if(counter % 100 ==0):
        print(counter)
db.session.commit()

last = time.time()
t = last - start
print("time"+str(t))






counter=0
with open('planes.csv','r') as f:
    data = f.readlines()

for row in data:
    airline_id = row.split(',')[0]

    aircraft_model_name = row.split(',')[0]
    aircraft_model_code = row.split(',')[1]
    number_of_row = random.randint(10,51)
    if number_of_row < 15:
        number_of_col = 4
    elif number_of_row < 30:
        number_of_col = 6
    else:
        number_of_col = 10  
    aircraft_model_obj = Aircraft_Model(number_of_col=number_of_col,number_of_row=number_of_row,model_name=aircraft_model_name,model_code=aircraft_model_code)
    
    if Aircraft_Model.query.filter_by(model_name=aircraft_model_name,model_code=aircraft_model_code).first():
        aircraft_model_obj = Aircraft_Model.query.filter_by(model_name=aircraft_model_name,model_code=aircraft_model_code).first()

    else:
        db.session.add(aircraft_model_obj)
    counter += 1
    if(counter % 100 ==0):
        print(counter)
db.session.commit()

last = time.time()
t = last - start

print("time"+str(t))



for i in range(300):
    tail_num1 = random.randint(10,99)
    tail_num2 = random.randint(10,1000)
    letter = random.choice(string.ascii_letters).upper()
    tail_number = letter + str(tail_num1) + "-" + str(tail_num2)

    models = Aircraft_Model.query.all()
    model_index = random.randint(0,len(models)-1)
    model = models[model_index]

    aircraft_obj = Aircraft(tail_number=tail_number,model=model)
    db.session.add(aircraft_obj)
db.session.commit()



#PıLOTS
password_plain_text  = "123456"
models = Aircraft_Model.query.all()
for i in range(1000):
    a = i
    firstname = "mustafa" + str(random.randint(0,10000))
    lastname = "tokmak" + str(random.randint(0,10000))
    email = firstname+lastname+"@airline.com"
    salary = random.randint(50*1000,150*1000)
    experience = random.randint(5,45)

    m = hashlib.sha256()
    m.update(password_plain_text.encode())
    password = m.digest().hex()
    

    speciality_models = []
    for j in range(5):
        model_index = random.randint(0,len(models)-1)
        model = models[model_index] 
        speciality_models.append(model)
    pilot_obj = Pilot(firstname=firstname,lastname=lastname,email=email,password=password,salary=salary,experience=experience,speciality_models=speciality_models)
    db.session.add(pilot_obj)

db.session.commit()
  
#TECHNICIAN
password_plain_text  = "123456"
models = Aircraft_Model.query.all()
for i in range(1000):
    a = i
    firstname = "mustafa" + str(random.randint(0,10000))
    lastname = "tokmak" + str(random.randint(0,10000))
    email = firstname+lastname+"@airline.com"
    salary = random.randint(50*1000,150*1000)

    m = hashlib.sha256()
    m.update(password_plain_text.encode())
    password = m.digest().hex()
    
    

    speciality_models = []
    for j in range(5):
        model_index = random.randint(0,len(models)-1)
        model = models[model_index] 
        speciality_models.append(model)
    technician_obj = Technician(firstname=firstname,lastname=lastname,email=email,password=password,salary=salary,speciality_models=speciality_models)
    db.session.add(technician_obj)

db.session.commit()


#Cabin_Member
password_plain_text  = "123456"
for i in range(2000):
    a = i
    firstname = "mustafa" + str(random.randint(0,10000))
    lastname = "tokmak" + str(random.randint(0,10000))
    email = firstname+lastname+"@airline.com"
    salary = random.randint(50*1000,150*1000)

    m = hashlib.sha256()
    m.update(password_plain_text.encode())
    password = m.digest().hex()
    
    
    technician_obj = Cabin_Member(firstname=firstname,lastname=lastname,email=email,password=password,salary=salary)
    db.session.add(technician_obj)
db.session.commit()


#Admin
password_plain_text  = "qwerty"
for i in range(5):
    a = i
    firstname = "mustafa" + str(random.randint(0,10000))
    lastname = "tokmak" + str(random.randint(0,10000))
    email = firstname+lastname+"@airline.com"

    m = hashlib.sha256()
    m.update(password_plain_text.encode())
    password = m.digest().hex()
    
    
    cabin_member_obj = Cabin_Member(firstname=firstname,lastname=lastname,email=email,password=password)
    db.session.add(technician_obj)
db.session.commit()


#Flights
routes = Route.query.all()
aircrafts = Aircraft.query.all()
all_pilots = Pilot.query.all()
cabin_members = Cabin_Member.query.all()
counter = 0 
for i in range(5000):
    #Flight time
    flight_duration = random.randint(50,750)
    base_date = datetime.datetime.now() - datetime.timedelta(days=180)
    extra_hours = random.randint(10,365*24)
    estimated_departure_date_time = base_date + datetime.timedelta(hours=extra_hours)
    estimated_arrival_date_time = estimated_departure_date_time + datetime.timedelta(minutes=flight_duration)
    if(counter % 100 == 0 ):
        print(counter)
    now = datetime.datetime.now()
    delay = random.randint(30,400)
    is_delayed = random.randint(1,11) % 5 == 0 # %20 ihtimalle delay var 
    
    if estimated_arrival_date_time < now:
        if is_delayed:
            actual_departure_date_time = estimated_departure_date_time + datetime.timedelta(minutes=delay)
            actual_arrival_date_time = estimated_arrival_date_time + datetime.timedelta(minutes=delay)
        else:
            actual_departure_date_time = estimated_departure_date_time
            actual_arrival_date_time = estimated_arrival_date_time

        deviation = flight_duration*random.randint(-5,5)/100 # %5 sapma 
        actual_arrival_date_time = actual_arrival_date_time + datetime.timedelta(minutes=delay)

    #choose aircraft
    #TODO check avaliable
    #2 gün üstüste uçuş pilot aircraft ve crew member için yok
    is_aircraft_assigned = True
    aircraft_counter = 0
    while(True):
        aircraft_counter += 1
        if aircraft_counter > 250:
            is_aircraft_assigned = False
            break
        aircraft_index = random.randint(0,len(aircrafts)-1)
        aircraft = aircrafts[aircraft_index]
        avaliable = True
        for f in aircraft.used_flights:
           
            if not f.estimated_arrival_date_time < (estimated_departure_date_time - datetime.timedelta(days=1)) or f.estimated_departure_date_time > (estimated_arrival_date_time + datetime.timedelta(days=1)) :
                avaliable = False
                break
        if avaliable:
            break
    if not is_aircraft_assigned:
        continue

    #choose route
    route_index = random.randint(0,len(routes)-1)
    route = routes[route_index]
    

    #choose pilots 
    #TODO check avaliable
    pilots  = []
    pilot_counter = 0
    is_pilot_assigned = True
    for i in range(2):
        while(True):
            pilot_counter += 1
            #avoid infinite loop
            if pilot_counter > 500:
                 is_pilot_assigned = False
            pilot_index = random.randint(0,len(all_pilots)-1)
            pilot = all_pilots[pilot_index]
            avaliable = True
            for f in pilot.flights:
               
                if not f.estimated_arrival_date_time < (estimated_departure_date_time - datetime.timedelta(days=1)) or f.estimated_departure_date_time > (estimated_arrival_date_time + datetime.timedelta(days=1)) :
                    avaliable = False
                    break
            if not aircraft.model in pilot.speciality_models:
                avaliable = False
                break
            if avaliable:
                break

        pilots.append(pilot)
    if not is_pilot_assigned:
        continue
    #choose cabin_crew
    #TODO check avaliable
    cabin_crew = []
    cabin_member_counter = 0
    is_cabin_member_assigned = True
    for i in range(4):
        cabin_member_index = random.randint(0,len(cabin_members)-1)
        cabin_member = cabin_members[cabin_member_index]

        while(True):
            cabin_member_index = random.randint(0,len(cabin_members)-1)
            cabin_member = cabin_members[cabin_member_index]
            avaliable = True
            cabin_member_counter += 1
            #avoid infinite loop
            if cabin_member_counter > 500:
                is_cabin_member_assigned = False
            for f in cabin_member.flights:
               

                if not f.estimated_arrival_date_time < (estimated_departure_date_time - datetime.timedelta(days=1)) or f.estimated_departure_date_time > (estimated_arrival_date_time + datetime.timedelta(days=1)) :
                    avaliable = False
                    break
            if avaliable:
                break
        cabin_crew.append(cabin_member)
    if not is_cabin_member_assigned:
        continue
    if estimated_arrival_date_time < now:        
        flight_obj = Flight(route=route,aircraft=aircraft,
        actual_departure_date_time=actual_departure_date_time,
        actual_arrival_date_time=actual_arrival_date_time,
        estimated_departure_date_time=estimated_departure_date_time,
        estimated_arrival_date_time=estimated_arrival_date_time,
        flight_duration=flight_duration,
        pilots=pilots,cabin_crew=cabin_crew)
    else:
        flight_obj = Flight(route=route,aircraft=aircraft,
        estimated_departure_date_time=estimated_departure_date_time,
        estimated_arrival_date_time=estimated_arrival_date_time,
        flight_duration=flight_duration,
        pilots=pilots,cabin_crew=cabin_crew)
    db.session.add(flight_obj)
    db.session.commit()
    counter += 1
    
    #Tickets
    #ticket price capacity arttıkca azalıyor.
    #ticket price duration arttıkca artıyor.
    number_of_col = aircraft.model.number_of_col
    number_of_row = aircraft.model.number_of_row
    capacity = number_of_col * number_of_row

    base_price = 200 #180 kisi 60 dk 
    price = (base_price*(flight_duration/60)) 
    price = price * (1/(capacity/(30*6)))

    columns = string.ascii_letters[:number_of_col]
    for row in range(1,number_of_row+1):
        for c in columns:
            seat_no = c.upper()+str(row)
            ticket_obj = Ticket(seat_no=seat_no,flight=flight_obj,price=price,last_price=0)
            db.session.add(ticket_obj)
    db.session.commit()



#clients
password_plain_text  = "1234asdf"
counter = 0
for i in range(1000):
    a = i
    firstname = "mustafa" + str(random.randint(0,100000))
    lastname = "tokmak" + str(random.randint(0,100000))
    email = firstname+lastname+"@airline.com"
    phone_number = str(random.randint(100*1000,999*1000)) + str(random.randint(10*1000,99*1000))
    m = hashlib.sha256()
    m.update(password_plain_text.encode())
    password = m.digest().hex()
    counter += 1
    if(counter % 100 == 0 ):
        print(counter)
    
    client_obj = Client(firstname=firstname,lastname=lastname,phone_number=phone_number,email=email,password=password)
    db.session.add(client_obj)
    db.session.commit()


last = time.time()
t = last - start

#add admin

password_plain_text  = "1234asdf"
for i in range(5):
    firstname = "mustafa" + str(random.randint(0,100000))
    lastname = "tokmak" + str(random.randint(0,100000))
    email = firstname+lastname+"@airline.com"
    m = hashlib.sha256()
    m.update(password_plain_text.encode())
    password = m.digest().hex()
    admin_obj = Admin(firstname=firstname,lastname=lastname,email=email,password=password)
    db.session.add(admin_obj)
    db.session.commit()


#add checks
counter = 0
all_aircrafts = Aircraft.query.all()
all_technicians = Technician.query.all()
for aircraft in all_aircrafts:
    now = datetime.datetime.now()
    for i in range (-5,6):
        days = i*30
        while(True):
            temp_date = now - datetime.timedelta(days=days)
            used_flights = aircraft.used_flights
            is_temp_date_available = True
            for f in used_flights:
                dep_date = f.estimated_departure_date_time
                arr_date = f.estimated_arrival_date_time
                if dep_date.day == temp_date.day and dep_date.month == temp_date.month and dep_date.year == temp_date.year:
                    days += 1
                    is_temp_date_available = False
                    break
                elif arr_date.day == temp_date.day and arr_date.month == temp_date.month and arr_date.year == temp_date.year:
                    days += 1
                    is_temp_date_available = False
                    break
            if is_temp_date_available:
                break
        date = temp_date
    
        while(True):
            technician_index = random.randint(0,len(all_technicians)-1)
            technician = all_technicians[technician_index]
            avaliable = True
            
            for c in technician.responsible_checks:
                if c.date.day == date.day and c.date.month == date.month and c.date.year == date.year:
                    avaliable = False
            if not aircraft.model in technician.speciality_models:
                avaliable = False
            if avaliable:
                break
        is_checked = False
        if date < now :
            is_checked = True
        check_obj = Check(date=date,aircraft=aircraft,is_checked=is_checked,technician=technician)
        db.session.add(check_obj)
        db.session.commit()
        counter += 1
        if(counter % 100==0):
            print(counter)
                


last = time.time()
t = last - start
print("time"+str(t))
         


#add bookings 
now = datetime.datetime.now()

not_avaliable_clients = db.session.query(Client).join(Client.reservations).join(Booking.tickets).join(Ticket.flight).filter(Flight.estimated_departure_date_time<now)
avaliable_clients = Client.query.except_all(not_avaliable_clients)


all_tickets = Ticket.query.all()
all_clients = Client.query.all()
all_flights = Flight.query.all()


last = time.time()
t = last - start
print("time"+str(t))

counter = 0
for flight in all_flights:
    aircraft_model = flight.aircraft.model
    capacity = aircraft_model.number_of_col * aircraft_model.number_of_row
    used_capacity = int(capacity*(random.randint(1,10)/10))
    flight_tickets = flight.tickets
    random.shuffle(flight_tickets)
    flight_tickets = flight_tickets[:used_capacity]
    arr_time = flight.estimated_arrival_date_time
    dep_time = flight.estimated_departure_date_time

    print(flight.id)
    for ticket in flight_tickets:
        if not ticket.is_avaliable:
            continue
        client_counter = 0
        client_found = False
        client = None
        for candidate_client in all_clients:
            is_avaliable_client = True
            for r in candidate_client.reservations:
                for t in r.tickets:
                    if not (t.flight.estimated_departure_date_time > arr_time or t.flight.estimated_arrival_date_time < dep_time ):
                        is_avaliable_client = False
                        break
                    if not is_avaliable_client:
                        break
            if is_avaliable_client:
                client = candidate_client
                break
            
        
        if not client:
            break
        counter += 1
        client_bookings = client.reservations
        is_new_booking = random.randint(1,100) % 2 == 0 
        if is_new_booking and client_bookings:
            booking_index = random.randint(0,len(client_bookings)-1)
            booking_obj = client_bookings[booking_index]
        else:
            booking_code = random.randint(10*1000*1000,99*1000*1000)
            booking_obj = Booking(client=client,booking_code=booking_code)
            db.session.add(booking_obj)

        #calculate last price
        aircraft_model = ticket.flight.aircraft.model
        capacity = aircraft_model.number_of_col * aircraft_model.number_of_row
        sold = len(ticket.flight.tickets)
        price = ticket.price
        last_price = 0.5*price + (sold/capacity)*3*price # ilk bilet yarı fiyatı son bilet 3.5 kat fiyatı
        is_avaliable = False
        
        ticket.last_price = last_price
        ticket.booking = booking_obj
        ticket.is_avaliable = is_avaliable
        db.session.add(ticket)

    if (counter % 1000 == 0):
        print(counter)
        last = time.time()
        t = last - start
        print("time"+str(t))
    db.session.commit()










"""

for i in range(200*1000):
    #all_tickets  = Ticket.query.all().filter_by(is_avaliable=True)
    ticket_index = random.randint(0,len(all_tickets)-1)
    ticket = all_tickets[ticket_index]
    if not ticket.is_avaliable:
        continue
    
    

    arr_time = ticket.flight.estimated_arrival_date_time
    dep_time = ticket.flight.estimated_departure_date_time
    
    
    
    while(True):
        client_index = random.randint(0,len(all_clients)-1)
        client = all_clients[client_index]
        is_avaliable_client = True
        for r in client.reservations:
            for t in r.tickets:
                if not (t.flight.estimated_departure_date_time > arr_time or t.flight.estimated_arrival_date_time < dep_time ):
                    is_avaliable_client = False
        if is_avaliable_client:
            break
    
    client_bookings = client.reservations
    is_new_booking = random.randint(1,100) % 2 == 0 
    if is_new_booking and client_bookings:
        booking_index = random.randint(0,len(client_bookings)-1)
        booking_obj = client_bookings[booking_index]
    else:
        booking_code = random.randint(10*1000*1000,99*1000*1000)
        booking_obj = Booking(client=client,booking_code=booking_code)
        db.session.add(booking_obj)

    #calculate last price
    aircraft_model = ticket.flight.aircraft.model
    capacity = aircraft_model.number_of_col * aircraft_model.number_of_row
    sold = len(ticket.flight.tickets)
    price = ticket.price
    last_price = 0.5*price + (sold/capacity)*3*price # ilk bilet yarı fiyatı son bilet 3.5 kat fiyatı
    is_avaliable = False
    
    ticket.last_price = last_price
    ticket.booking = booking_obj
    ticket.is_avaliable = is_avaliable
    db.session.add(ticket)
    if (i % 1000 == 0):
        print(i)
        last = time.time()
        t = last - start
        print("time"+str(t))
        db.session.commit()
    




"""

last = time.time()
t = last - start
print("time"+str(t))