from abc import ABC, abstractmethod
from .actions import DefaultAction, CsvAction
from .enums import FormatEnums


class HandlerAbstract(ABC):

    @abstractmethod
    def handle(self):
        pass


class Handler(HandlerAbstract):

    def __init__(self, data, source, dest, key) -> None:
        self.source = source
        self.dest = dest
        self.key = key
        self.data = data; 

    def get_action_class(self):
        if self.dest == FormatEnums.CSV.value:
            return  CsvAction
        return DefaultAction

    def get_action(self):
        action = self.get_action_class()
        return action(self.data, key=self.key)

    def handle(self):
        action = self.get_action()
        action.convert()
