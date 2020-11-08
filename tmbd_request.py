import urllib.request
import json
import sys

api_key = sys.argv[1]

response = urllib.request.urlopen('https://api.themoviedb.org/3/movie/550?api_key=' + api_key)
json_response = json.load(response)

print(json_response)