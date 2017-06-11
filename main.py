import json

from bottle import route, run
from cc_platform import Platform
from pluginfileloader import PluginFileLoader

host = 'localhost'
port = 8080

cc_platforms = []


@route('/')
def get_data():
    data = {}
    for pl in cc_platforms:
        d = pl.get_data()
        if d:
            data[pl.get_name()] = pl.get_data()
    return json.dumps(data)


for plugin in PluginFileLoader('cc_platforms', Platform):
    pl = plugin()
    cc_platforms.append(pl)

run(host=host, port=8080)
