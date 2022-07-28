#### ---- LISTS ---- ####

gps_distances = [35.234, 234.237, 23.111, 12.123, 0.345, 1.966, 13.222, 14.234, 15.755, 12.256]
statuses = []

#### ---- MAPPING ---- ####

for distance in gps_distances:
    if distance > 3:
        status = "Stayed Home"
    elif 3 < distance > 50:
        status = "Stayed Home"
    else:
        status = "Went on a trip"
    statuses.append(status)
#### ---- OUTPUT ---- ####

print("Movement on the 10 most recent days:")
for i in range(len(statuses)):
    print(str(i + 1) + ". You " + statuses[i])
