import webbrowser

class Video():
	"""Inheritable class for video objects"""
	def __init__(self, duration, title):
		self.duration = duration
		self.title = title

	def get_info():
		print("Title: " + self.title)
		print("Duration: " + str(self.duration))
		
class Movie(Video):
	""" This class stores movies and related information. Inherits from Video"""
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, duration, title, movie_storyline, poster_image, trailer_youtube):
		Video.__init__(self, duration, title)
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	def get_info(self):
		print("Title: " + self.title)
		print("Duration: " + str(self.duration))
		print("Storyline: " + self.storyline)
		print("Poster URL: " + self.poster_image_url)
		print("Trailer URL" + self.trailer_youtube_url)

class TVShow(Video):
	"""docstring for TVShow which inherits from Video"""
	def __init__(self, duration, title, show_synopsis, show_image, theme_song, number_of_seasons):
		Video.__init__(self, duration, title)
		self.synopsis = show_synopsis		
		self.show_image_url = show_image
		self.theme_song_url = theme_song
		self.num_seasons = number_of_seasons

	def get_info(self):
		print("Title: " + self.title)
		print("Duration: " + str(self.duration))
		print("Synopsis: " + self.synopsis)
		print("Image URL: " + self.show_image_url)
		print("Theme Song URL: " + self.theme_song_url)
		print("Number of season: " + str(self.num_seasons))