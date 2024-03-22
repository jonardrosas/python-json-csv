import requests
from abc import ABC, abstractmethod
from .exceptions import NoKeyException, HttpRequestError


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
        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, dict):
                all_keys = [_key for _key in data.keys() if _key != key ]
                if key:
                    if key in data:
                        return self.flatten(data, key, all_keys)
                    else:
                        raise NoKeyException(f"The key {key} does not exists on the source")
            return data
        else:
            raise HttpRequestError(f"Error while ready the path {self.data}")

    def flatten(self, data, key, all_keys):
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
