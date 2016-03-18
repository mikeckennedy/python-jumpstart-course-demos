import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'Title,Poster,Type,imdbID,Year'
)


class MovieClient:
    def __init__(self, search_text):

        if not search_text or not search_text.strip():
            raise ValueError('You must specify a search string.')

        self.search_text = search_text

    def perform_search(self):
        url = 'http://www.omdbapi.com/?s={}&y=&plot=short&r=json'.format(
            self.search_text)

        r = requests.get(url)
        data = r.json()

        results = data['Search']

        movies = [
            MovieResult(**m)
            for m in results
            ]
        movies.sort(key=lambda m: m.Title)

        return movies











