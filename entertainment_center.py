import fresh_tomatoes
import media

#Instances of the Class Movie
zindagi = media.Movie("Zindagi Na Milegi Dobara",
  "Three friends decide to turn their fantasy vacation into reality after one of their number becomes engaged.",
  "https://upload.wikimedia.org/wikipedia/en/3/3d/Zindaginamilegidobara.jpg",
  "https://www.youtube.com/watch?v=FJrpcDgC3zU")


raging_bull = media.Movie("Raging Bull",
    "An emotionally self-destructive boxer's journey through life",
    "https://upload.wikimedia.org/wikipedia/en/5/5f/Raging_Bull_poster.jpg",
    "https://www.youtube.com/watch?v=YiVOwxsa4OM")

taxi_driver = media.Movie("Taxi Driver",
    "A mentally unstable Vietnam War veteran works as a night-time taxi driver in New York City",
    "https://upload.wikimedia.org/wikipedia/en/8/8f/Taxi_Driver_original_movie_poster.jpg",
    "https://www.youtube.com/watch?v=UUxD4-dEzn0"
                          )

dil_chahta_hai = media.Movie("Dil Chahta Hai",
     "Three inseparable childhood friends are just out of college. Nothing comes between them - until they each fall in love",
     "https://upload.wikimedia.org/wikipedia/en/d/db/Dil_Chahta_Hai.jpg",
     "https://www.youtube.com/watch?v=m13b25V0B10")

forrest_gump = media.Movie("Forrest Gump", 
     "Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
     "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
     "https://www.youtube.com/watch?v=bLvqoHBptjg")

dark_knight = media.Movie("Dark Knight",
     "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms",
     "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
     "https://www.youtube.com/watch?v=EXeTwQWrcwY")


#Storing the instance variables in an array for
movies = [zindagi,raging_bull,taxi_driver,dil_chahta_hai,forrest_gump,dark_knight]

#Calling the function open_movies_page from fresh_tomatoes module with movies as arguement
fresh_tomatoes.open_movies_page(movies)

