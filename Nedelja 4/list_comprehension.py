squared = [elem**2 for elem in range(1, 101)]
print(squared)
squared_even = [elem**2 for elem in range(1, 101) if elem % 2 == 0]
print(squared_even)

movies = ["The Godfather", "The Wizard of Oz", "Citizen Kane", "Pulp Fiction"]
movies_starts_with_the = [movie for movie in movies if movie.startswith("The")]
print(movies_starts_with_the)

movies = [("The Godfather", 1972), ("The Wizard of Oz", 1939),
          ("Citizen Kane", 1941), ("Pulp Fiction",1994)]

# Izdvojiti one filmove (samo naslov) koji su izasli nakon 1980 godine
movies_after_1980 = [title.lower() for (title, year) in movies if year > 1980]
print(movies_after_1980)

movies = [("The Godfather", 1972, "drama"), ("The Wizard of Oz", 1939, "drama"),
          ("Citizen Kane", 1941, "drama"), ("Pulp Fiction",1994, "drama")]

# Izdvojiti sve drama filmove snimljene izmedju 1970. i 2000. godine
drama_movies = [{title: {"year": year, "genre": genre}} 
                    for (title, year, genre) in movies 
                    if 1970 < year < 2000 and genre == "drama" ]
print(drama_movies)

# Za listu unijetih cijena vratiti cijene bez PDV-a kao novu listu
lista_cijana = [100, 200, 300, 250, 1000]
lista_cijena_bez_pdva = [round(cijena - cijena * 0.21, 2) for cijena in lista_cijana]
print(lista_cijena_bez_pdva)