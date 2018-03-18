import fresh_tomatoes
import media

# the following objects represent some of my favourite movies

fight_club = media.Movie("Fight Club",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

spaceballs = media.Movie("Spaceballs",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/4/45/Spaceballs.jpg/220px-Spaceballs.jpg",
                         "https://www.youtube.com/watch?v=WZsVNkx7NLw")

hitchhikers_guide = media.Movie("Hitchhiker's Guide to the Galaxy (2005)",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Hitchhikers_guide_to_the_galaxy.jpg/220px-Hitchhikers_guide_to_the_galaxy.jpg",
                                "https://www.youtube.com/watch?v=eLdiWe_HJv4")

robocop = media.Movie("RoboCop (1987)",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/1/16/RoboCop_%281987%29_theatrical_poster.jpg/220px-RoboCop_%281987%29_theatrical_poster.jpg",
                      "https://www.youtube.com/watch?v=zbCbwP6ibR4")

total_recall = media.Movie("Total Recall (1990)",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Total_recall.jpg/220px-Total_recall.jpg",
                           "https://www.youtube.com/watch?v=2DwNb-ZGVjE")

langoliers = media.Movie("The Langoliers",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/8/83/The_Langoliers_%28TV_miniseries%29.jpg/250px-The_Langoliers_%28TV_miniseries%29.jpg",
                         "https://www.youtube.com/watch?v=zJocfhzC6xU")

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy (2014)",
                                      "https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg",
                                      "https://www.youtube.com/watch?v=2Uwp2K5AO3Y")

fifth_element = media.Movie("The Fifth Element",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/6/65/Fifth_element_poster_%281997%29.jpg/220px-Fifth_element_poster_%281997%29.jpg",
                            "https://www.youtube.com/watch?v=fQ9RqgcR24g")

zootopia = media.Movie("Zootopia",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")

# add my favourite movies to a list
movies = [fight_club, spaceballs, hitchhikers_guide, robocop, total_recall, langoliers, guardians_of_the_galaxy, fifth_element, zootopia]

# use the fresh_tomatoes module to create a HTML page showcasing my list of favourite movies
fresh_tomatoes.open_movies_page(movies)
