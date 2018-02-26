import media
import fresh_tomatoes

black_panther = media.Movie("Black Panther",
                            "T'Challa, the King of Wakanda, rises to the throne in the isolated, technologically advanced African nation, but his claim is challenged by a vengeful outsider who was a childhood victim of T'Challa's father's mistake.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=dxWvtMOGAhw")

game_night = media.Movie("Game Night",
                         "A group of friends who meet regularly for game nights find themselves trying to solve a murder mystery.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQxMDE5NDg0NV5BMl5BanBnXkFtZTgwNTA5MDE2NDM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=qmxMAdV6s4U")
peter_rabbit = media.Movie("Peter Rabbit",
                           "Feature adaptation of Beatrix Potter's classic tale of a rebellious rabbit trying to sneak into a farmer's vegetable garden.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk5NzI0ODUwN15BMl5BanBnXkFtZTgwOTIxNjA0NDM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=7Pa_Weidt08")

annihilation = media.Movie("Annihilation",
                           "A biologist signs up for a dangerous, secret expedition where the laws of nature don't apply.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2Mjc2NzYxNl5BMl5BanBnXkFtZTgwMTA2OTA1NDM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=89OP78l9oF0")

Jumanji = media.Movie("Jumanji: Welcome to the Jungle",
                      "Four teenagers are sucked into a magical video game, and the only way they can escape is to work together to finish the game.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkyNDQ1MDc5OV5BMl5BanBnXkFtZTgwOTcyNzI2MzI@._V1_.jpg",
                      "https://www.youtube.com/watch?v=2QKg5SZ_35I")

The_15 = media.Movie("The 15:17 to Paris",
                     "Three Americans discover a terrorist plot aboard a train while in France.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY0NjUzNjYwOV5BMl5BanBnXkFtZTgwMzY1MDM0NDM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=IC_lnyn2R2Q")

mov = [black_panther, game_night, peter_rabbit, annihilation, Jumanji, The_15]
header = ['My Movies List','Good Action and Adventure movies', 'https://images-na.ssl-images-amazon.com/images/M/MV5BNTIzMjE4MTU2MV5BMl5BanBnXkFtZTgwODY1Nzc3NDM@._V1_SX1500_CR0,0,1500,999_AL_.jpg']
fresh_tomatoes.open_movies_page(mov,header)
