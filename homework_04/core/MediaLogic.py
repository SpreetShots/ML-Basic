from core.BaseLogicClass import MediaFile

class AudioFile(MediaFile):

    def info(self):
        print(f"basic: {self.metadata}, audio: {self.audio}")

    def convert(self, target_format, out_path):
        print("Конвертация аудио файла")

    def extract_features(self):
        print("Извлечь аудио-фичи")
    
class VideoFile(MediaFile):

    def info(self):
        print(f"basic: {self.metadata}, video: {self.video}")

    def transcode(self, profile, out_path):
        print("транскодирование по профилю, например 720р")

    def thumbnail(self, time_seconds):
        print("сделать превью видео по тайм-коду")
    
class PhotoFile(MediaFile):

    def info(self):
        print(f"basic: {self.metadata}, photo: {self.photo}")

    def resize(self, width, height, out_path):
        print("Изменить размер изображения")

    def analyze(self):
        print("Распознать что-то на изображении")