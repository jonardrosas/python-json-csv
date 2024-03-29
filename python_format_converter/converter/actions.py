from abc import ABC, abstractmethod
import csv
import time
import os
import xmltodict
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

    def get_storage_location(self):
        filename = self.generate_filename()
        base_path = os.getcwd() 
        if self.output_locaton:
            location = os.path.join(base_path, self.output_locaton)
            if not os.path.exists(location):
                os.makedirs(location)
            return os.path.join(location, filename)
        return os.path.join(base_path, filename)

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
        output_path = os.path.normpath(output_path)
        with open(output_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)
            print(f"successfully converted to csv {output_path}")
        

    def generate_filename(self):
        now = str(time.time()).split('.')[0]
        return f"csv_{now}.{self.ext}"


class XmlAction(ActionBase):
    ext = FormatEnums.CSV.XML

    def convert(self):
        data = {'root': self.get_data()}
        output_path = self.get_storage_location()
        output_path = os.path.normpath(output_path)
        xml_data = xmltodict.unparse(data)
        with open(output_path, 'w') as f:
            f.write(xml_data)

    def generate_filename(self):
        now = str(time.time()).split('.')[0]
        return f"filename_{now}.{self.ext}"
