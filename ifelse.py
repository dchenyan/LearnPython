#ifelse.py to learn if else statement syntax
movie = input ("enter the title of a movie you've watched recently:")
rating = float (input("On a scale of 1 to 10, how would you rate it?"))
if rating >=10:
    print(f"Wow, {movie} must be a fantastic movie")
elif rating >=7:
    print(f"{movie} is not bad")
else:
    print(f"Oh no, you don't like {movie}")