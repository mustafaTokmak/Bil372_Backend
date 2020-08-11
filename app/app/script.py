with open('routes.csv','r') as f:
    data = f.readlines()
airport_ids = []
new_routes = []
for i in range(len(data)):
    pc = data[i].split(',')[0]
    if pc != 'PC':
            continue
    new_routes.append(data[i])
    airport_id1 = data[i].split(',')[3]
    airport_id2 = data[i].split(',')[5]
    if not airport_id1 in airport_ids:
            airport_ids.append(airport_id1)
    if not airport_id2 in airport_ids:
            airport_ids.append(airport_id2)
    
print(len(airport_ids))

with open('new_routes.csv','w') as f:
    for i in new_routes:
        f.write(i)



with open('airports.csv','r') as f:
    data = f.readlines()
cities = []
counter = 0
new_airports = []
for row in data:
    airport_id = row.split(',')[0]
    if not airport_id in airport_ids:
        continue
    new_airports.append(row)



with open('new_airports.csv','w') as f:
    for i in new_airports:
        f.write(i)

