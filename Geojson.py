f = open ("all.txt", "r")
z = open ("points.json", "w")

for line in f:
  elements = line.split()
  date = elements[1]
  lat = elements[3]
  lng = elements[2]

  geojson = "{ \"type\": \"Feature\", \"geometry\": {\"type\": \"Point\", \"coordinates\": [%s , %s] }, \"properties\": { \"date\": \"%s\" }}," %(lat,lng, date) 
  print (geojson, file=z)
