f = open("ISO_no_unknown.txt", "r")
o = open("germany.json", "w")

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
  dates = date.split("-")
  longitude = elements[2]
  latitude = elements[3]

  country = elements[4]
  if len(elements) > 4:
    city = str(" ".join(elements[5:]))


  if (float(longitude) > 47.70 and float(longitude) < 54.31):
    if (float(latitude) > 5.77 and float(latitude) < 16.02):
      if(dates[0] == "1944" and (dates[1] == "07" or dates[1] == "08" or dates[1] == "09" or dates[1] == "10" or dates[1] == "11")):
        print ("{\"type\": \"Feature\", \"geometry\": {\"type\": \"Point\", \"coordinates\": [%s, %s]}, \"properties\": {\"record\": \"%s\", \"date\": \"%s\", \"country\": \"%s\", \"city\": \"%s\"}}," % (latitude, longitude, record, date, country, city), file=o)
      
      
