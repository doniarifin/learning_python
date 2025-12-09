import json
import requests

class Movie:
  def __init__(self) -> None:
     pass
  def get_data(self, base_url: str, head: str, param)-> json:
     request = requests.get(base_url, headers=head, params=param)
     return json.loads(request.content)

# https://rapidapi.com/
url: str = "https://movies-ratings2.p.rapidapi.com/ratings"
querystring = {"id":"tt0111161"}

api_key: str = "YOUR_API_KEY"
api_host: str = "movies-ratings2.p.rapidapi.com"
headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': api_host
}

api1: Movie = Movie()

get_movies = api1.get_data(url, headers, querystring)

print(get_movies)