import media
import fresh_tomatoes

Robo=media.Movie("Robo",
                 "Robo 2.0 - An action 3-D film",
                 "https://i.pinimg.com/originals/a1/39/89/a139891e8ecab9e0fb4bc9dd74154064.jpg",
                 "https://www.youtube.com/watch?v=2wvq8hdGdAw",
                 "3-D film",
                 "Official Teaser of our Magnum Opus 2.0 Starring Rajinikanth, Akshay Kumar, Amy Jackson")

Chalo_story=media.Movie("Chalo",
                        "Chalo Trailer | Naga Shaurya, Rashmika Mandanna | Ira Creations | Theatrical Trailer",
                        "http://www.ratingdada.com/images/3/11222017115115am_chalo.jpg",
                        "https://www.youtube.com/watch?v=6_BxEjvWsqs",
                        "Drama",
                        "Venky Kudumula--(Story,Screenplay,Direction) || Naga Shaurya, Rashmika Madanna")
#print(toy_story.storyline)

katamraudu=media.Movie("Katamrayudu",
                       "It is Beautuful love song",
                       "http://mananela.com/wp-content/uploads/2016/12/Katamarayudu.jpg",
                       "https://www.youtube.com/watch?v=zggQw2wb60M",
                       "Action",
                       "Kishore Kumar Parsadani--(Director) || Pawan Kalyan, Shruthi Hasan")
Nartanasala=media.Movie("Nartanasala",
                        "Narthanasala Teaser || Narthanasala Movie Latest Trailer || Naga Shaurya, Kashmira, Yamini || 2018",
                        "https://i.ytimg.com/vi/uY4pp0mgpmc/maxresdefault.jpg",
                        "https://www.youtube.com/watch?v=uY4pp0mgpmc",
                        "Romantic",
                        "Srinivas Chakravarthi--(Director) || Naga Shaurya, Yamini Bhaskar")
Geetha_govindam=media.Movie("Geetha Govindam",
                            "Geetha Govindam ReleaseTrailer || Vijay Devarakonda||Rithika||Fan Made",
                            "https://akm-img-a-in.tosshub.com/indiatoday/images/story/201808/Geetha_Govindam_3.jpeg?lViC8c3iiHCmONeSNIQ9waMy4RbtVFou",
                            "https://www.youtube.com/watch?v=UVqbymdrLGs",
                            "Family Entertainer",
                            "Parasuram--(Director) || Vijay Devarakonda, Rashmika Mandanna")

#print(katamraudu.storyline)

#katamraudu.show_trailer()

movies=[Robo,Chalo_story,katamraudu,Nartanasala,Geetha_govindam]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
