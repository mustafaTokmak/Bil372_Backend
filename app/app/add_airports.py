from model import db
from model import Client,Booking,Flight,Airport,Route,Country,City


with open('airports.csv','r') as f:
    data = f.readlines()
countries = []
cities = []
for row in data:
    name = row.split(',')[1]
    city = row.split(',')[2]
    country = row.split(',')[3][1:-1]
    if not country in countries:
        countries.append(country)
    code = row.split(',')[4]
print(countries)

"""db.session.add(booking)
db.session.commit()"""