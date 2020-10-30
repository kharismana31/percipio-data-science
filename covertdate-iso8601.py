from datetime import datetime

#format MM/DD/YYYY
d = "12/25/2017"
dateiso = datetime.strptime(d, "%m/%d/%Y").isoformat()
print(dateiso)

#format DD/MM/YY
d = "25/12/17"
dateiso = datetime.strptime(d, "%d/%m/%y").isoformat()
print(dateiso)

#format timestamp
d = 1514160000
dateiso = datetime.fromtimestamp(d).isoformat()
print(dateiso)

#format Day DD Month YYYY h:M:S
d = "Mon 25 Dec 2017 12:00:00"
dateiso = datetime.strptime(d, "%a %d %b %Y %H:%M:%S").isoformat()
print(dateiso)