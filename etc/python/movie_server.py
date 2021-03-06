import pymongo
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient


def load_all_movies():
    client = MongoClient('Localhost', 27017)
    db = client.dbsparta.movies
    return list(db.find({}, {'_id': 0}))  # 다가지고오는데, id는 0 -> 가지고 오지마 1 -> 가지고왕

def find_movie_by_title(t):
    if t == None:
        return load_all_movies()
    client = MongoClient('Localhost', 27017)
    db = client.dbsparta.movies
    return list(db.find({'title':t}, {'_id': 0}))


def find_movie_by_rank(r):
    if r== None:
        return load_all_movies()
    client =MongoClient('Localhost', 27017)
    db = client.dbsparta.movies
    return list(db.find({'rank':int(r)}, {'_id':0}))

def write_movie(movie):
    # {'rank' :1, 'title: '제목', 'score' : '10.0'}
    client=MongoClient('Localhost',27017)
    db = client.dbsparta.movies
    db.insert_one(movie)


def run_server():
    server = Flask('무비서버')
    @server.route('/', methods=['get'])
    def home():
        return render_template('movies.html')

    @server.route('/movies', methods=['GET'])
    def movies():
        title_found = []
        rank_found = []

        title = request.args.get('title')
        rank = request.args.get('rank')

        if title is None and rank is None:
            return jsonify(load_all_movies())

        if title is not None:
            title_found = find_movie_by_title(title)

        if rank is not None:
            rank_found = find_movie_by_rank(rank)

        found = title_found + rank_found
        return jsonify(found)

    @server.route('/movies', methods=['POST'])
    def add_movie():
        title = request.form['title']
        rank = request.form['rank']
        score = request.form['score']

        if title is None or rank is None or score is None:
            result = {'message': 'parameter not filled', 'result': 'error'}
            return jsonify(result)


        movie = {'rank':int(rank), 'title':title, 'score':score}
        write_movie(movie)
        result = {'message': 'Good', 'result': 'success'}
        return jsonify(result)

        return 'OK'


    server.run('0.0.0.0', port=5000, debug=True)
run_server()