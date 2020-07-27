from model import db
from model import Client,Booking,Flight,Airport,Route,Country,City
db.create_all()


with open('airports.csv','r') as f:
    data = f.readlines()

cities = []
counter = 0
for row in data:
    airport_name = row.split(',')[1]
    city = row.split(',')[2][1:-1]
    if not city in cities:
        cities.append(city)
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
    print(counter)

db.session.commit()



print(cities)
print(len(cities))

"""db.session.add(booking)
db.session.commit()"""