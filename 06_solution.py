#Transportation Mode Selection
#Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = int(input('enter the distance in km:'))

if distance >=15:
    transport = "car"
elif distance >=3:
    transport = 'bike'
else:
    transport ="walk"

print(transport)
    