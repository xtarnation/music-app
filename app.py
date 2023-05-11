from flask import Flask, render_template, redirect, url_for, request

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
    conn = dbconnect.connect()
    c = conn.cursor()
    artist_sqliterow = c.execute('SELECT * FROM artists WHERE name=?', (artist,)).fetchone()
    artist_songs_sqliterow = c.execute(f'SELECT * FROM songs WHERE artist LIKE "%{artist}%"').fetchall()
    dbconnect.close(conn)

    artist_details = dict(artist_sqliterow)

    artist_songs = []
    for one in artist_songs_sqliterow:
        artist_songs.append(dict(one))

    return render_template('artistprofile.html', artist=artist, artist_details=artist_details, songs=artist_songs)


if __name__ == '__main__':
    app.run(debug=True)