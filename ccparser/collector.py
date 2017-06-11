from ccparser.platforms import available_platforms

from ccparser import config


class CCCollector:
    def __init__(self, config='config.ini'):
        self.loaded_platforms = []
        self.configuration = config.load(config)

        wanted_platforms = self.configuration.get(
            'General', 'platforms').split(',')

        self._load_platforms(platforms=self.configuration.get())

    def _load_platforms(self, platforms):
        for platform in available_platforms:
            if not platforms or platform.name in platforms:
                self.loaded_platforms.append(platform(self))
