from core.BaseLogicClass import Storage

# Локальное файловое хранилище
class LocalStorage(Storage):
    def save(self, path, files):
        print("Сохранить файл")

    def open(self, path):
        print("Открыть файл")

    def delete(self, path):
        print("Удалить файл из локального хранилища")

    def exists(self, path):
        print("Проверить существует ли файл")

    def get_url(self, path):
        print("Вернуть путь до файла")