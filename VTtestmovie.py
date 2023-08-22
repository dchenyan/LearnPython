# Ask the user for a movie and a rating
#movie = input("Enter the title of a movie you've watched recently: ")
#tempurature = float(input("On a scale of 1 to 100, how would you rate it? "))

#movie = 'barbie'
#rating = 65

# Provide feedback based on the rating
#if tempurature >= 90:
    #print("It's hot outside!")
#elif tempurature >= 70:
    #print("It's warm outside.")
#elif tempurature >= 50:
    #print("It's cool outside.")
#else:
    #print("It's cold outside!!")


humidity_index = 10
temperature = [21, 20, 19, 37, 55, 89, 106, -10]

for index in range(len(temperature)):
  temperature[index] = temperature[index] + humidity_index

for t in temperature:
  if t >= 90:
      print("It's hot outside!")
  elif t >= 70:
      print("It's warm outside.")
  elif t >= 50:
      print("It's cool outside.")
  else:
      print("It's cold outside!!")