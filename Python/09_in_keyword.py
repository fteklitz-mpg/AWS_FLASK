movies_watched = {"The Batman", "Don't Look Up", "Year of the Dog"}
user_movie = input("enter a movie: ")

if user_movie in movies_watched:
    print(f"I have watched {user_movie}, too!" )
else:
    print("I have not watched it yet")