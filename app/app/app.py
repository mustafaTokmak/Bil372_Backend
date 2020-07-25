from model import db
<<<<<<< HEAD
from model import Client,Booking
from model import app
from flask import request
=======
from model import User
from model import app

>>>>>>> 66176a3afc23ebd355f9f10bbceeca536b3b29bc
import random
import json

@app.route('/')
def hello_world():
    return 'Hello, World!'



<<<<<<< HEAD



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
=======
@app.route('/app', methods=['GET'])
@app.route('/app', methods=['GET'])
def main():
    response = {}
    for i in range(100):
        username = "admin" + str(random.randint(0,10000000000))
        email = "admin@example.com" + str(random.randint(0,10000000000))
        admin = User(username=username, email=email)
        db.session.add(admin)
        db.session.commit()
    print(User.query.all())
    for i in User.query.all():
        print(i)
    print(User.query.filter_by().first())
    print(User.query.filter_by().first().email)
    """try:
        #TODO sürekli istek atılmasına karşşı önlem alınacak
        remote_ip = request.remote_addr
        response = {"ip":str(remote_ip)}
        return json.dumps(response)
    except Exception as e:
        send_devops_mail(function="",email="",userid="",tenantid="",tenant_name="",error_type=str(request.url),platform="",content=str(request.get_data()))
        logger.exception("public_ip")
        response["ip"] = ""
        response["result"] = "False"
        response["message"] =  "public_ip error"""
    return json.dumps(response)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=False, host='0.0.0.0', port=5000)
>>>>>>> 66176a3afc23ebd355f9f10bbceeca536b3b29bc
