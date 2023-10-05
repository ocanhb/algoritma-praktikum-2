import math
lat1 = float(input("lintang titik 1 : "))
lon1 = float(input("bujur titik 1 : "))
lat2 = float(input("lintang titik 2 : "))
lon2 = float(input("bujur titik 2 : "))

lat1 = math.radians(lat1)
lon1 = math.radians(lon1)
lat2 = math.radians(lat2)
lon2 = math.radians(lon2)

dlat = lat2 - lat1
dlon = lon2 - lon1

R = 6371.0

a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

jarak = R * c

print(f"Jarak antara kedua titik adalah {jarak} kilometer")
