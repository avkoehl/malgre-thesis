f = open("ISO_no_unknown.txt", "r")
o = open("bastogne.json", "w")

record = ""
date = ""
longitude = ""
latitude = ""
country  = ""
city = ""

for line in f:
  line = line.rstrip()
  elements = line.split()
  record = elements[0]
  date = elements[1]
  longitude = elements[2]
  latitude = elements[3]

  country = elements[4]
  if len(elements) > 4:
    city = str(" ".join(elements[5:]))


  if (float(longitude) > 49.30 and float(longitude) < 50.60):
    if (float(latitude) > 5.50 and float(latitude) < 6.80):
      print ("{\"type\": \"Feature\", \"geometry\": {\"type\": \"Point\", \"coordinates\": [%s, %s]}, \"properties\": {\"record\": \"%s\", \"date\": \"%s\", \"country\": \"%s\", \"city\": \"%s\"}}," % (latitude, longitude, record, date, country, city), file=o)
      
      
