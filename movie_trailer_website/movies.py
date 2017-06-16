import media
import fresh_tomatoes

# list_of_movies is a list which stores movies
list_of_movies = []

# Creating beautiful_mind
# Instance of Movie
# Each instance has title, stotyline, link to a poster and link to a youtube trailer
beautiful_mind = media.Movie("A Beautiful Mind",
                            ("A Beautiful Mind is a 2001 American biographical drama film based on the"
                            " life of John Nash, a Nobel Laureate in Economics."),
                            "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                            "https://www.youtube.com/watch?v=JV2PSWSyi0s")

# Adding beautiful_mind to the list
list_of_movies.append(beautiful_mind)

jason_bourne = media.Movie("Jason Bourne",
                        ("In the film, Bourne remains on the run from CIA hit squads as he tries to uncover"
                        " hidden truths about his father."),
                        "https://upload.wikimedia.org/wikipedia/en/b/b2/Jason_Bourne_%28film%29.jpg",
                        "https://www.youtube.com/watch?v=F4gJsKZvqE4")

# Adding jason_bourne to the list
list_of_movies.append(jason_bourne)

good_will = media.Movie("Good Will Hunting",
                        ("The film follows 20-year-old South Boston laborer Will Hunting, an unrecognized genius who,"
                        " as part of a deferred prosecution agreement after assaulting a police officer,"
                        " becomes a client of a therapist and studies advanced mathematics with a renowned professor."),
                        "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=PaZVjZEFkRs")

# Adding good_will to the list
list_of_movies.append(good_will)

shawshank = media.Movie("The Shawshank Redemption",
                        ("The film tells the story of Andy Dufresne, a banker who is sentenced to life in Shawshank State Penitentiary"
                        " for the murder of his wife and her lover, despite his claims of innocence."),
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=K_tLp7T6U1c")

# Adding shawshank to the list
list_of_movies.append(shawshank)

little_rascals = media.Movie("The Littel Rascals",
                            ("The film is an adaptation of Hal Roach's Our Gang, a series of short films of the"
                            " 1920s, 1930s, and 1940s (many of which were broadcast on television as The Little Rascals)"
                            " which centered on the adventures of a group of neighborhood children."),
                            "https://upload.wikimedia.org/wikipedia/en/6/6f/Little_rascals_ver2.jpg",
                            "https://www.youtube.com/watch?v=Svdb1XXVX_c")

# Adding little_rascals to the list
list_of_movies.append(little_rascals)

karate_kid = media.Movie("The Karate Kid",
                        "The Karate Kid is a 1984 American martial arts drama film.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a9/Karate_kid.jpg",
                        "https://www.youtube.com/watch?v=n7JhKCQnEqQ")

# Adding karate_kid to the list
list_of_movies.append(karate_kid)

# Calling open_movies_page function in fresh_tomatoes
# Passing it the list_of_movies
fresh_tomatoes.open_movies_page(list_of_movies)
