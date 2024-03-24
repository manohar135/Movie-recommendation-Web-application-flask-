from flask import Flask, render_template, request, jsonify
import fetchmovies


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