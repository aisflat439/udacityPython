import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
	"A story about a boy and his toys",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
	"A marine on an alien planet.",
	"http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")

big_lebowski = media.Movie("The Big Lebowski",
	"A dude abides",
	"http://upload.wikimedia.org/wikipedia/en/thumb/3/35/Biglebowskiposter.jpg/220px-Biglebowskiposter.jpg",
	"https://www.youtube.com/watch?v=ngV0RBhGZmE")

armageddon = media.Movie("Armageddon",
	"Oil rig drillers attempt to save the world.",
	"http://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Armageddon-poster06.jpg/220px-Armageddon-poster06.jpg",
	"https://www.youtube.com/watch?v=kg_jH47u480")

independence_day = media.Movie("Independence Day",
	"Aliens invade and humanity fights back",
	"http://upload.wikimedia.org/wikipedia/en/thumb/b/bb/Independence_day_movieposter.jpg/220px-Independence_day_movieposter.jpg",
	"https://www.youtube.com/watch?v=kA2WzBi2grE")

amelie = media.Movie("Amelie",
	"An eccentric French woman finds love",
	"http://upload.wikimedia.org/wikipedia/en/thumb/5/53/Amelie_poster.jpg/220px-Amelie_poster.jpg",
	"https://www.youtube.com/watch?v=HEFrLnS5sQY")

rounders = media.Movie("Rounders",
	"A law student takes on the poker world",
	"http://upload.wikimedia.org/wikipedia/en/thumb/6/67/RoundersPoster.jpg/220px-RoundersPoster.jpg",
	"https://www.youtube.com/watch?v=dtJvyTKe1iE")

movies = [toy_story, avatar, big_lebowski, armageddon, independence_day, amelie, rounders]

print(media.__module__)

#fresh_tomatoes.open_movies_page(movies)