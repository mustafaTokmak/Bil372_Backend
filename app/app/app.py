from model import db
from model import Client,Booking
from model import app
from flask import request
import random
import json

@app.route('/')
def hello_world():
    return 'Hello, World!'






@app.route('/register_as_client', methods=['GET','POST'])
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


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
