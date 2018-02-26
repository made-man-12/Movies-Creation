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

mov = [black_panther, game_night]
header = ['My Movies List','Good Action and Adventure movies', 'https://images-na.ssl-images-amazon.com/images/M/MV5BNTIzMjE4MTU2MV5BMl5BanBnXkFtZTgwODY1Nzc3NDM@._V1_SX1500_CR0,0,1500,999_AL_.jpg']
fresh_tomatoes.open_movies_page(mov,header)