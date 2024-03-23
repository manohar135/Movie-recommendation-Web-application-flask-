import pandas as pd
import pickle as pkl
import requests
import numpy as np

with open('ML_model\listOf5.pkl', 'rb') as f:
    rlist = pkl.load(f)

rlist = np.array(rlist)

#Getting the title list of the movies
df = pd.read_csv("ML_model/tmdb_5000_movies.csv")
names = df["original_title"]

#provides five suggestion in the search
def searchMovies(substring):
    substring = substring.lower()
    searchMovies = []
    count = 0
    for s in names:
        if count > 4:
            break
        if substring in s.lower():
            count += 1
            searchMovies.append(s)
    
    return searchMovies

#Fetch movie posters
def fetch_poster(movie_id):
    try:
        response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=0c491a3828cefc4197b2ca0faa726826".format(movie_id))
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
    except requests.exceptions.RequestException as e:
        print(e)
        return fetch_poster(movie_id) #retry when error occurs

#reccomending 5 movies based on title
def reccomendMovies(title):
    movie_index = np.where(names == title)[0][0]
    rmovies = rlist[movie_index]

    rmovie_titles = list(df.loc[rmovies, 'original_title'].values)

    movie_ids = df.loc[rmovies, 'id'].values
    poster_urls = [fetch_poster(id) for id in movie_ids]
    return rmovie_titles, poster_urls

