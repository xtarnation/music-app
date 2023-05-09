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
    songs_dict = []
    for one in songs_sqliterow:
        songs_dict.append(dict(one))

    length = len(songs_dict)
    return render_template('music.html', songs=songs_dict, length=length)

@app.route('/artists', methods=['GET', 'POST'])
def artists():
    if request.method == 'POST':
        artist = request.form['artist']
        return redirect(url_for('artist', artist=artist))
    return render_template('artists.html')

@app.route('/artists/<artist>')
def artist(artist):
    return render_template('artistprofile.html', artist=artist)

if __name__ == '__main__':
    app.run(debug=True)