import media

toy_story = media.Movie("Toy Story",
	"About a boy and toys.",
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

# print(toy_story.storyline)
# print(avatar.storyline)
big_lebowski.show_trailer()