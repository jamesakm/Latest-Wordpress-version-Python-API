#!/usr/bin/python3.6
import urllib.request
import simplejson as json
rawjson = urllib.request.urlopen("https://api.wordpress.org/core/version-check/1.7/").read()
version = json.loads(rawjson)
print(version["offers"][0]["version"])