import requests
from abc import ABC, abstractmethod
from .exceptions import NoKeyException


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
        if isinstance(data, dict):
            all_keys = [_key for _key in data.keys() if _key != key ]
            if key:
                if key in data:
                    return self.merged_data(data, key, all_keys)
                else:
                    raise NoKeyException(f"The key {key} does not exists on the source")
        return data

    def merged_data(self, data, key, all_keys):
        final_data = []
        for _data in data[key]:
            for _key in all_keys:
                if _key in data:
                    _data[_key] = data[_key]
            final_data.append(_data)
        return final_data


class FileReader(ReaderBase):

    def read(self):
        file = open(self.data, 'r')
        return file.readlines()
