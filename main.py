import json
import turtle
import urllib.request
import time

#astronauts in the ISS right now

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('Astronauts on the ISS:', result['number'])

people = result['people']

for p in people:
  print(p['name'], 'in', p['craft'])

print()
#latitude and longitude of where the ISS is right now

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Latitude:', lat)
print('Longitude:', lon)

#turtle map
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

#turtle face 

screen.register_shape('ISS.gif')
ISS = turtle.Turtle()
ISS.shape('ISS.gif')
ISS.setheading(90)

ISS.penup()
ISS.goto(lon, lat)

# Espoo, Finland

lat = 60.2055
lon = 24.6559

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

#time when the ISS will fly past 

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
over = result['response'][1]['risetime']

style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)