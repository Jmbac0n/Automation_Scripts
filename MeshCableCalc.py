print("Mesh Network Cable calculator")
print("")

userval = input() # Takes input from the user as a string

x = int(userval) # Converts the string into an integer for calculation

result = (x * (x - 1)) / 2 # Mesh topology calculation for cables needed

print(result) # Output
