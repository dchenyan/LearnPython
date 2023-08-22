# Ask the user for a movie and a rating
movie = input("Enter the title of a movie you've watched recently: ")
rating = float(input("On a scale of 1 to 100, how would you rate it? "))
#movie = 'barbie'
#rating = 30
# Provide feedback based on the rating
if rating >= 90:
    print(f"Wow, {movie} must be a fantastic movie!")
elif rating >= 70:
    print(f"It sounds like {movie} was pretty good.")
elif rating >= 50:
    print(f"Okay, {movie} was average.")
else:
    print(f"Oh no, it seems like you didn't enjoy {movie} very much.")

