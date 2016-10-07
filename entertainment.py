import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch7v=vwyn185NOC4")
print(toy_story.storyline)

raging_bull = media.Movie("Raging Bull","An emotionally self-destructive boxer's journey through life, as the violence and temper that leads him to the top in the ring destroys his life outside it.",
                     "https://upload.wikimedia.org/wikipedia/en/5/5f/Raging_Bull_poster.jpg",
                     "https://www.youtube.com/watch?v=YiVOwxsa4OM")

taxi_driver = media.Movie("Taxi Driver",
                          "A mentally unstable Vietnam War veteran works as a night-time taxi driver in New York City where the perceived decadence and sleaze feeds his urge for violent action, attempting to save a preadolescent prostitute in the process.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8f/Taxi_Driver_original_movie_poster.jpg",
                          "https://www.youtube.com/watch?v=UUxD4-dEzn0"
                          )

#print(toy_story.storyline) 
dil_chahta_hai = media.Movie("Dil Chahta Hai", "Three inseparable childhood friends are just out of college. Nothing comes between them - until they each fall in love, and their wildly different approaches to relationships creates tension.",
                             "https://upload.wikimedia.org/wikipedia/en/d/db/Dil_Chahta_Hai.jpg",
                             "https://www.youtube.com/watch?v=9coA7bcpJII")
ratatouille = media.Movie("Ratatouille", "Storyline", "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch2v=c3sBBRxDAgk")
midnight_in_paris = media.Movie("Midnight in Paris","Storyline",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg","https://www.youtube.com/watch2v=atLg2wQ12mvu")
hunger_games = media.Movie("Hunger Games", "Storyline",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg","https://www.youtube.com/watch2v=PbA63a7H0bo")

movies = [toy_story,raging_bull,taxi_driver,dil_chahta_hai,ratatouille,midnight_in_paris,hunger_games]
fresh_tomatoes.open_movies_page(movies)

#print(avatar.storyline)
#avatar.show_trailer()
#taxi_driver.show_trailer()

print(media.Movie.__module__)
