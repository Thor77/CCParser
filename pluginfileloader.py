import os

class PluginFileLoader:

    def __init__(self, path, blueprint=None):
        if not blueprint:
            blueprint = Plugin
        self.blueprint = blueprint
        self.path = path
        self.classes = []
        __import__(path)
        self.load_plugins()

    def __iter__(self):
        for cl in self.classes:
            yield cl

    def get_plugins(self):
        return self.classes

    def load_plugins(self):
        files = os.listdir(self.path)
        for f in files:
            if f.endswith('.py'):
                __import__(self.path + '.' + f.replace('.py', '', 1))
        self.classes = self.blueprint.__subclasses__()

class Plugin:
    def get_name(self):
        return self.__class__.__name__