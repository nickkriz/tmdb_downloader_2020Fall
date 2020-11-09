import urllib.request
import json
import sys
import os
import time

api_key = sys.argv[1]

if not os.path.exists('json_files'):
	os.mkdir('json_files')

response = urllib.request.urlopen('https://api.themoviedb.org/3/movie/latest?api_key=' + api_key)
json_response = json.load(response)

movie_count = int(json_response['id'])
print(movie_count)

movie_start = movie_count-5
# movie_start = 1

for i in range(movie_start,movie_count):
	print(i)
	movie_id = str(i)
	response = urllib.request.urlopen('https://api.themoviedb.org/3/movie/' + movie_id + '?api_key=' + api_key)
	json_response = json.load(response)
	# print(json_response)
	f = open("json_files/tmdb" + movie_id + ".json", "w")
	f.write(json.dumps(json_response))
	f.close()
	time.sleep(15)
