import requests
from abc import ABC, abstractmethod


class ActionAbstract(ABC):
    reader = None

    @abstractmethod
    def convert(self):
        pass


class ActionBase(ActionAbstract):

    def __init__(self, data) -> None:
        self.data = data

    def parse_request(self, data):
        request = requests.get(data)
        return request.json()

    def get_data(self):
        if 'http' in self.data:
            return self.parse_request(self.data)
        return self.data

    def convert(self):
        print("Action base convert")


class ActionDefault(ActionBase):

    def convert(self):
        data =  self.get_data()
        return data
        print("Action Default convert", data)

