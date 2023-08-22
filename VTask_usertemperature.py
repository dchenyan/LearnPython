 #Ask the user for a temperature
temperature = float(input("What is the temperature in degrees Farenheit? "))  
  
# Provide feedback based on the temperature
if temperature >= 90:
    print("It's hot outside!")
elif temperature >= 70:
    print("It's warm outside.")
elif temperature >= 50:
    print("It's cool outside.")
else:
    print("It's cold outside.")