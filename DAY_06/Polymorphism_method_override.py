class media_player:
    def play(self):
        print("Playing media")


class audio_player(media_player):
    def play(self):
        print("Playing audio")


class video_player(media_player):
    def play(self):
        print("Playing video")


AP=audio_player()
AP.play()
VP=video_player()
VP.play()
