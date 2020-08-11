from model import db
from model import Client,Booking,Flight,Airport,Route,Country,City
from model import app
from flask import request
import random
import json


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

@app.route('/api/get_user_reservations', methods=['GET','POST'])
def get_user_reservations():
    response = {}
    content = request.get_json()
    email = content["email"]
    password = content["password"]
    user_type = find_user_type(email,password)
    response["user_type"] = user_type
    return json.dumps(response)

@app.route('/api/get_reservations_', methods=['GET','POST'])
def login():
    response = {}
    content = request.get_json()
    email = content["email"]
    password = content["password"]
    user_type = find_user_type(email,password)
    response["user_type"] = user_type
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



@app.route('/add_airports', methods=['GET','POST'])
def add_airports():
    response = {}
    content = request.get_json()
    for i in range(1):
        name = "esenboga" + str(random.randint(0,10000000000))
        code = "ESB" + str(random.randint(0,10000000000))
        
        
        country_name = "turkey"+str(random.randint(0,10000000000))
        country = Country(name=country_name)
        
        city_name = "ankara" + str(random.randint(0,10000000000)) 
        city = City(country=country,name=city_name)

        airport = Airport(name=name,city=city,code=code)
        if(Airport.query.filter_by(name=name).first()):
            airports = Airport.query.filter_by(name=name)
            print("TRUE")
            print(len())
        else:
            print("FALSE")
        
        db.session.add(city)
        db.session.add(country)
        #db.session.add(airport)
        db.session.commit()
        

        
    return json.dumps(response)



@app.route('/get_reservations', methods=['GET','POST'])
def get_reservations():
    response = {}
    content = request.get_json()
    str_list =[]
    for i in range(1):
        client = Client.query.all()[i]
        for r in client.reservations:
            print(r)
            str_list.append(str(r.id))
    response["str_list"] = str_list
    return json.dumps(response)





if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
