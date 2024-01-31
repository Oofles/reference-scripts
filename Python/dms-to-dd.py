# Conversion from DMS to Decimal Degrees
def dms_to_dd(degrees, minutes, seconds):
    return degrees + (minutes/60) + (seconds/3600)

# Provided coordinates
lat_dms = (39, 52, 30)  # Latitude in DMS
long_dms = (20, 0, 36)  # Longitude in DMS

# Convert to Decimal Degrees
lat_dd = dms_to_dd(*lat_dms)
long_dd = dms_to_dd(*long_dms)

print("Latitude in DD:", lat_dd)
print("Longitude in DD:", long_dd)

label = "Combined:"
print(label + ' ' + str(lat_dd), long_dd, sep=', ')
