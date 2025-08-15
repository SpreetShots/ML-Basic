from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


# Интерфейс хранилища
class Storage(ABC):
    @abstractmethod
    def save(self, path, files):
        print("Сохранить файл по переданному пути")

    @abstractmethod
    def open(self, path):
        print("Открыть файл")

    @abstractmethod
    def delete(self, path):
        print("Удалить файл")

    @abstractmethod
    def exists(self, path):
        print("Проверить существует ли файл")

    @abstractmethod
    def get_url(self, path):
        print("Получить URL файла")
    

# Базовый класс медиа-файла
class MediaFile(ABC):
    def __init__(self, metadata, storage, path):
        self.metadata = metadata
        self.storage = storage
        self.path = path

    def save(self, content):
        print("Сохранить файл в хранилище")

    def delete(self):
        print("Удалить файл из хранилища")

    def exists(self):
        print("Проверить существует ли файл в хранилище")

    def url(self):
        print("Получить URL файла из хранилища")

    @abstractmethod
    def info(self):
        print("Вернуть информацию о файле")
        
@dataclass
class VideoMetadata:
    duration_seconds: Optional[float] = None
    width: Optional[int] = None
    height: Optional[int] = None
    codec: Optional[str] = None
    
@dataclass
class PhotoMetadata:
    width: Optional[int] = None
    height: Optional[int] = None
    format: Optional[str] = None
    camera: Optional[str] = None

@dataclass
class AudioMetadata:
    duration_seconds: Optional[float] = None
    sample_rate: Optional[int] = None
    channels: Optional[int] = None
    format: Optional[str] = None
    
@dataclass
class BasicMetadata:
    name: str
    size: Optional[int] = None
    created_at: Optional[datetime] = None
    owner: Optional[str] = None
