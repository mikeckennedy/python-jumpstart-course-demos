import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'Title,Poster,Type,imdbID,Year'
)

search = 'capital'
url = 'http://www.omdbapi.com/?s={}&y=&plot=short&r=json'.format(search)

r = requests.get(url)
data = r.json()

results = data['Search']

# movies = []
# for result in results:
#     m = MovieResult(
#         Title=result['Title'],
#         Poster=result['Poster'],
#         Type=result['Type'],
#         imdbID=result['imdbID'],
#         Year=result['Year']
#     )
#     movies.append(m)

# def method_with_kws(pos1, **kwargs)
# pass

# movies = []
# for result in results:
#     m = MovieResult(**result)
#     movies.append(m)

movies = [
    MovieResult(**m)
    for m in results
]

print(movies)











