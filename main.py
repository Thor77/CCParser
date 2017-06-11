host = 'localhost'
port = 8080

from pluginfileloader import PluginFileLoader
from cc_platform import Platform
from bottle import route, run, template
import json

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

#route(url, callback=func)
run(host=host, port=8080)
