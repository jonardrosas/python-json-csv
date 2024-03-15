from abc import ABC, abstractmethod
import csv
import os
from datetime import datetime
from .reader import HttpReader, DefaultReader
from .enums import FormatEnums


class ActionAbstract(ABC):
    reader = None

    @abstractmethod
    def convert(self):
        pass


class ActionBase(ActionAbstract):
    reader = DefaultReader
    output_locaton = 'output'

    def __init__(self, data, key=None) -> None:
        self.data = data
        self.key = key

    def get_reader(self):
        if 'http' in self.data:
            return HttpReader
        return DefaultReader

    def get_data(self):
        reader = self.get_reader()
        reader_ins = reader(self.data)
        return reader_ins.read()

    def convert(self):
        data =  self.get_data()
        return data


class DefaultAction(ActionBase):
    pass


class CsvAction(ActionBase):
    ext = FormatEnums.CSV.value

    def get_header(self, data):
        if isinstance(data, dict):
            return list(data.keys())
        else:
            return list(data[0].keys())

    def get_data(self):
        reader = self.get_reader()
        reader_ins = reader(self.data)
        return reader_ins.read(key=self.key)

    def convert(self):
        data =  self.get_data()
        header = self.get_header(data)
        output_path = self.get_storage_location()
        with open(output_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)
            print(f"successfully converted to csv {output_path}")
        return data
        
    def get_storage_location(self):
        base_path = ''
        if self.output_locaton:
            base_path = self.output_locaton
        filename = self.generate_filename()
        return os.path.join(base_path, filename)

    def generate_filename(self):
        now = datetime.now()
        return f"csv_{now}.{self.ext}"



class XmlAction(ActionBase):

    def convert(self):
        print("Converting to xml")
