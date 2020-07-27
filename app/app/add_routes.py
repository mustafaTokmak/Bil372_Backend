from model import db
from model import Client,Booking,Flight,Airport,Route,Country,City,Departure_Airport,Arrival_Airport,Aircraft_Model,Aircraft,Pilot,Technician,Cabin_Member,Client
import random
import hashlib
import datetime 
import string

db.create_all()
import time 
start = time.time()

with open('routes.csv','r') as f:
    data = f.readlines()

counter = 0



with open('airports.csv','r') as f:
    data = f.readlines()
cities = []
counter = 0
for row in data:
    
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
    
    airport_obj = Airport(name=airport_name,city=city_obj,code=code)
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
with open('routes.csv','r') as f:
    data = f.readlines()

FR_rows = []
for row in data:
    airline_id = row.split(',')[0]
    if airline_id == "FR":
        FR_rows.append(row)
print(len(FR_rows))
    

for row in FR_rows:
    airline_id = row.split(',')[0]

   
    
    try:
        departure_airport_id = int(row.split(',')[3])
        arrival_airport_id = int(row.split(',')[5])
    except:
        continue
    departure_airport = Airport.query.filter_by(id=departure_airport_id).first()
    arrival_airport = Airport.query.filter_by(id=arrival_airport_id).first()


    dep_obj = Departure_Airport(dep_airport=departure_airport)
    if Departure_Airport.query.filter_by(dep_airport=departure_airport).first():
        dep_obj = Departure_Airport.query.filter_by(dep_airport=departure_airport).first()
    else:
        db.session.add(dep_obj)

    arr_obj = Arrival_Airport(ar_airport=arrival_airport)
    if Arrival_Airport.query.filter_by(ar_airport=arrival_airport).first():
        arr_obj = Arrival_Airport.query.filter_by(ar_airport=arrival_airport).first()
    else:
        db.session.add(arr_obj)
     
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
    print(tail_number)

    models = Aircraft_Model.query.all()
    print(len(models))
    model_index = random.randint(0,len(models)-1)
    print(model_index)
    model = models[model_index]
    print(model)

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
    print(password)
    

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
    print(password)
    

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
    print(password)
    
    
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
    print(password)
    
    
    cabin_member_obj = Cabin_Member(firstname=firstname,lastname=lastname,email=email,password=password)
    db.session.add(technician_obj)
db.session.commit()


#Flights
routes = Route.query.all()
aircrafts = Aircraft.query.all()
all_pilots = Pilot.query.all()
cabin_members = Cabin_Member.query.all()
for i in range(10000):
    #Flight time
    flight_duration = random.randint(50,750)
    base_date = datetime.datetime.now() - datetime.timedelta(days=180)
    extra_hours = random.randint(10,365*24)
    estimated_departure_date_time = base_date + datetime.timedelta(hours=extra_hours)
    estimated_arrival_date_time = estimated_departure_date_time + datetime.timedelta(minutes=flight_duration)

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
    while(True):
        aircraft_index = random.randint(0,len(aircrafts)-1)
        aircraft = aircrafts[aircraft_index]
        avaliable = True
        for f in aircraft.used_flights:
            if not f.estimated_arrival_date_time < estimated_departure_date_time - datetime.timedelta(days=1) or f.estimated_departure_date_time > estimated_arrival_date_time + datetime.timedelta(days=1) :
                avaliable = False
                break
        if avaliable:
            break

    #choose route
    print(len(routes))
    route_index = random.randint(0,len(routes)-1)
    print(route_index)
    route = routes[route_index]
    

    #choose pilots 
    #TODO check avaliable
    pilots  = []
    for i in range(2):
        while(True):
            pilot_index = random.randint(0,len(all_pilots)-1)
            pilot = all_pilots[pilot_index]
            avaliable = True
            for f in pilot.flights:
                if not f.estimated_arrival_date_time < estimated_departure_date_time - datetime.timedelta(days=1) or f.estimated_departure_date_time > estimated_arrival_date_time + datetime.timedelta(days=1) :
                    avaliable = False
                    break
            if avaliable:
                break

        pilots.append(pilot)
    
    #choose cabin_crew
    #TODO check avaliable
    cabin_crew = []
    for i in range(4):
        print(len(pilots))
        cabin_member_index = random.randint(0,len(cabin_members)-1)
        print(cabin_member_index)
        cabin_member = cabin_members[cabin_member_index]

        while(True):
            cabin_member_index = random.randint(0,len(cabin_members)-1)
            cabin_member = cabin_members[cabin_member_index]
            avaliable = True
            for f in cabin_member.flights:
                if not f.estimated_arrival_date_time < estimated_departure_date_time - datetime.timedelta(days=1) or f.estimated_departure_date_time > estimated_arrival_date_time + datetime.timedelta(days=1) :
                    avaliable = False
                    break
            if avaliable:
                break
        cabin_crew.append(cabin_member)
    if estimated_arrival_date_time < now:        
        flight_obj = Flight(route=route,aircraft=aircraft,
        actual_departure_date_time=actual_departure_date_time,
        actual_arrival_date_time=actual_arrival_date_time,
        estimated_departure_date_time=estimated_departure_date_time,
        estimated_arrival_date_time=estimated_arrival_date_time,
        pilots=pilots,cabin_crew=cabin_crew)
    else:
        flight_obj = Flight(route=route,aircraft=aircraft,
        estimated_departure_date_time=estimated_departure_date_time,
        estimated_arrival_date_time=estimated_arrival_date_time,
        pilots=pilots,cabin_crew=cabin_crew)
    db.session.add(flight_obj)
    #Tickets
    #ticket price capacity arttıkca azalıyor.
    #ticket price duration arttıkca artıyor.
    number_of_col = aircraft.model.number_of_col
    number_of_row = aircraft.model.number_of_row
    columns = string.ascii_letters[:number_of_col]
    for row in range(1,number_of_row+1):
        for c in columns:
            seat_no = c.upper()+str(row)
            ticket_obj = Ticket(seat_no=seat_no,flight=flight_obj)
            db.session.add(ticket_obj)
    



#clients
password_plain_text  = "1234asdf"
for i in range(10000):
    a = i
    firstname = "mustafa" + str(random.randint(0,10000))
    lastname = "tokmak" + str(random.randint(0,10000))
    email = firstname+lastname+"@airline.com"
    phone_number = str(random.randint(10*1000,99*1000)) + str(random.randint(10*1000,99*1000))
    m = hashlib.sha256()
    m.update(password_plain_text.encode())
    password = m.digest().hex()
    print(password)
    
    
    client_obj = Client(firstname=firstname,lastname=lastname,phone_number=phone_number,email=email,password=password)
    db.session.add(client_obj)
db.session.commit()


last = time.time()
t = last - start
print("time"+str(t))

