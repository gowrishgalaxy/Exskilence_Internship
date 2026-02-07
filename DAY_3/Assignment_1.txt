class Camera:
    def __init__(self, camera_quality):
        self.camera_quality = camera_quality

    def display_camera_details(self):
        print("Camera:", self.camera_quality)


class MusicPlayer:
    def __init__(self, sound_quality):
        self.sound_quality = sound_quality

    def display_music_details(self):
        print("Music Player:", self.sound_quality)


class Smartphone(Camera, MusicPlayer):
    def __init__(self, brand, camera_quality, sound_quality):
        self.brand = brand
        Camera.__init__(self, camera_quality)
        MusicPlayer.__init__(self, sound_quality)
        

    def display_smartphone_details(self):
        print("Phone Brand:", self.brand)
        print("Camera:", self.camera_quality)
        print("Sound:", self.sound_quality)


phone1 = Smartphone("25MP", "Dolby Atmos", "Samsung F41")
phone1.display_smartphone_details()
