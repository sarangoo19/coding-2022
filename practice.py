def convert_feet_to_meters(distance_feet):
	return 0.3048 * distance_feet

def convert_inches_to_feet(distance_inches):
	return distance_inches / 12.0

def convert_inches_to_meters(distance_inches):
	return convert_feet_to_meters(convert_inches_to_feet(distance_inches))

print('I am here.')
distance_meter=10.0
print(distance_meter)
distance_meter=convert_feet_to_meters(200.0)
print(distance_meter)
print('Now I am done.')

print('1000 inches in meters are',convert_feet_to_meters(convert_inches_to_feet(1000.0)))

# If statements

if distance_meter>10.0
	print('Distance is greater than 10 meters.')
else:
	print('Distance is not than great.')

if False:
	print('It is false.')
else:
	print('It is not.')

print(distance_meter>10.0)

distance_meter=0
is distance_meter:
#is the same as not distance_meter==0.0
	print('What is distance?')
else:
	print('Distance is', distance_meter)



