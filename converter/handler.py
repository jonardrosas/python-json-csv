from abc import ABC, abstractmethod
from .actions import ActionDefault


class HandlerAbstract(ABC):

    @abstractmethod
    def handle(self):
        pass



class Handler(HandlerAbstract):

    def __init__(self, data, from_type, to_type) -> None:
        self.from_type = from_type
        self.to_type = to_type
        self.data = data; 

    def _get_action(self):
        return ActionDefault(self.data)

    def handle(self):
        action = self._get_action()
        action.convert()
