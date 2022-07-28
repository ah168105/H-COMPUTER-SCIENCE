#### ---- SETUP ---- ####

## -- Starting movie -- ##

movies = {
    "Spider-Man: Homecoming" : "2017",
    "Spider-Man: Far from Home" : "2019",
    "Spider-Man: No Way Home" : "2021"
}
## -- Intro -- ##

print("Welcome to Movie Times!")

#### ---- MAIN LOOP ---- ####

running = True
while running:

    ## -- Input and exiting -- ##

    title = input("\nEnter a movie title, or \"exit\" to end: ")
    if title == "exit":
        break

    ## -- Response -- ##

    if title in movies:
        print(movies[title])
    
    else:
        new_movie = input("That movie is not in our database. When was it released?")
        movies[title] = new_movie
        print("Thank you for the information")
