import requests
from abc import ABC, abstractmethod


class ReaderAbstract(ABC):
    @abstractmethod
    def read(self):
        pass


class ReaderBase(ReaderAbstract):

    def __init__(self, data) -> None:
        self.data = data

    def read(self):
        return []


class DefaultReader(ReaderBase):

    def read(self):
        return super().read()


class HttpReader(ReaderBase):

    def read(self, key=None):
        resp = requests.get(self.data)
        data = resp.json()
        if key and key in data:
            return data[key]
        return data


class FileReader(ReaderBase):

    def read(self):
        file = open(self.data, 'r')
        return file.readlines()