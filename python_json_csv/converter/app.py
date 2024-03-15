from .handler import Handler

class AppConverter:
    handler = Handler

    def __init__(self, api, dest, key=None) -> None:
        self.api = api
        self.dest = dest
        self.key = key

    def convert(self):
        handler = self.handler(self.api, self.dest, self.key)
        handler.handle()