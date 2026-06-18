class MusicPlayer:
    def play(self):
        print("Playing Music")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing Music on Spotify")

s = Spotify()

s.play()