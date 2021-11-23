import csv
import pandas as pd
import matplotlib.pyplot as plt


rows = []
with open("Star_with_gravity.csv") as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    rows.append(row)

headers = rows[0]
headers[0] = 'index' 
print(headers)
df = pd.read_csv('Star_with_gravity.csv')
star_name = df['Star_name'].tolist()
star_name.pop(0)
mass = df['Mass'].tolist()
mass.pop(0)
radius = df['Radius'].tolist()
radius.pop(0)
distance = df['Distance'].tolist()
distance.pop(0)
gravity = df['Gravity'].tolist()
gravity.pop(0)

plt.figure(figsize = (10,5))
plt.title('Stars Vs Mass')
plt.xlabel('Name')
plt.ylabel('Mass')
plt.bar(star_name[0:9], mass[0:9])
print(plt.show())
plt.figure(figsize = (10,5))
plt.title('Stars Vs Radius')
plt.xlabel('Name')
plt.ylabel('Radius')
plt.bar(star_name[0:9], radius[0:9])
print(plt.show())
plt.figure(figsize = (10,5))
plt.title('Stars Vs Distance')
plt.xlabel('Name')
plt.ylabel('Distance')
plt.bar(star_name[0:9], distance[0:9])
print(plt.show())
plt.figure(figsize = (10,5))
plt.title('Stars Vs Gravity')
plt.xlabel('Name')
plt.ylabel('Gravity')
plt.bar(star_name[0:9], gravity[0:9])
print(plt.show())
final_planet_list = []
for planet_data in rows:
  temp_dict = {
      'name' : planet_data[1],
      'distance' : planet_data[2],
      'planet_mass' : planet_data[3],
      'planet_radius' : planet_data[4],
      'gravity' : planet_data[5],
  }
  final_planet_list.append(temp_dict)
print(final_planet_list)