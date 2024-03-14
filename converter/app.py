from .handler import Handler

class AppConverter:
    handler = Handler

    def __init__(self, api, source, to) -> None:
        self.api = api
        self.source = source
        self.to = to

    def convert(self):
        handler = self.handler(self.api, self.source, self.to)
        handler.handle()