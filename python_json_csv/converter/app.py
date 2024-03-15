from .handler import Handler

class AppConverter:
    handler = Handler

    def __init__(self, api, source, to, key) -> None:
        self.api = api
        self.source = source
        self.to = to
        self.key = key

    def convert(self):
        handler = self.handler(self.api, self.source, self.to, self.key)
        handler.handle()