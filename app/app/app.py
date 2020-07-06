from model import db
from model import User
from model import app

import random
import json

@app.route('/')
def hello_world():
    return 'Hello, World!'



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
