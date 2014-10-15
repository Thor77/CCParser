How to use
==========
1. Place your plugin(s) in the `cc_platforms`-folder
2. edit the host and port variable at the first line of main.py
3. run `main.py`
4. Do a get-request on the host and port you set. The answer will look like this:  
`
{pluginname: [[title, artist, album], [title, artist, album], ...], ...}
`

How to write a plugin
=====================

1. Create a new .py-file in the `cc_platforms`-folder
2. Import the plugin-template `from cc_platform import Platform`
3. Create a child-class of the template `class MyPlugin(Platform)`
4. Override the `get_data` method of the template, it has to return the following data:  
`
[[title, artist, album], [title, artist, album], ...]
`
