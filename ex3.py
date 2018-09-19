print("I will now count my chickens:")

# Prints Hens 30 (30/6 = 5, 25 + 5 = 30)
print("Hens", 25.0 + 30.0 / 6.0)
# Prints Roosters 97 (25 * 3) = 75 mod 4 = 3, 100 - 3 = 97
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

print("Now I will count the eggs:")
# (4 mod 2) = 0, (1/4) = . 25, (3+2+1-5) = 1, (1-0)-.25 + 6 = 6.75
print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

print("Is it true that 3 + 2 < 5 - 7?")
# -2 is less than 5, prints False
print(3.0 + 2.0 < 5.0 - 7.0)

print("What is 3 + 2?", 3.0 + 2.0)
print("What is 5 - 7?", 5.0 - 7.0)

print("Oh, what's why it's False.")

print("How about some more.")

print("Is it greater?", 5.0 > -2.0)
print("Is it greater or equal?", 5.0 >= -2.0)
print("Is it less or equal?", 5.0 <= -2.0)