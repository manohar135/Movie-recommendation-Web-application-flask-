from flask import Flask, render_template, request, jsonify
import fetchmovies

# #Loding the list of movies to be reccomend
# with open('ML_model\listOf5.pkl', 'rb') as f:
#     movie_rec_list = pkl.load(f)


# #Getting the title list of the movies
# df = pd.read_csv("ML_model/tmdb_5000_movies.csv")
# names = list(df["original_title"])

# #Fetch movie posters
# def fetch_poster(movie_id):
#     print(movie_id)
#     response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=0c491a3828cefc4197b2ca0faa726826".format(movie_id))
#     data = response.json()
#     return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

# #provides five suggestion in the search
# def returnFive(substring):
#     substring = substring.lower()
#     searchMovies = []
#     count = 0
#     for s in names:
#         if count > 4:
#             break
#         if substring in s.lower():
#             count += 1
#             searchMovies.append(s)
    
#     return searchMovies


# #reccomending 5 movies based on title
# def reccomendMovies(title):
#     movie_index = df[df['original_title'] == title].index[0]
#     movie_rec_indexs = movie_rec_list[movie_index]

#     movie_titles = list(df.loc[movie_rec_indexs, 'original_title'].values)

#     movie_ids = df.loc[movie_rec_indexs, 'id'].values
#     poster_urls = [fetch_poster(id) for id in movie_ids]
#     return movie_titles, poster_urls


app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def Home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        data = request.json
        if data['is_rec']:
            titles, posters = fetchmovies.reccomendMovies(data['str'])
            data = {'titles': titles, 'posters': posters}
            return jsonify(data)
        else:
            return jsonify(fetchmovies.searchMovies(data['str']))
    


if __name__ == "__main__":
    app.run(debug=True)