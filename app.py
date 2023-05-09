from flask import Flask, render_template, redirect, url_for, request
import sqlite3

import dbconnect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/music')
def music():
    conn = dbconnect.connect()
    c = conn.cursor()
    songs_sqliterow = c.execute('SELECT * FROM songs').fetchall()
    dbconnect.close(conn)

    songs_dict = []
    for one in songs_sqliterow:
        songs_dict.append(dict(one))

    return render_template('music.html', songs=songs_dict)


@app.route('/artists')
def artists():
    conn = dbconnect.connect()
    c = conn.cursor()
    artists_sqliterow = c.execute('SELECT * FROM artists').fetchall()
    dbconnect.close(conn)

    artists_dict = []
    for one in artists_sqliterow:
        artists_dict.append(dict(one))

    return render_template('artists.html', artists=artists_dict)


@app.route('/artists/<artist>')
def artist(artist):
    return render_template('artistprofile.html', artist=artist)


if __name__ == '__main__':
    app.run(debug=True)