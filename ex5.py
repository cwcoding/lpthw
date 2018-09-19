name = 'Cory W'
age = 29 # years
height = 71.75 # inches
weight = 190 # lbs
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

def lbs_to_kg(lbs):
	return round(lbs * 0.45)

def inches_to_cm(inches):
	return round(inches * 2.54)

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {inches_to_cm(height)} centimeters tall")
print(f"He's {weight} pounds heavy.")
print(f"He is {lbs_to_kg(weight)} kilograms heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
