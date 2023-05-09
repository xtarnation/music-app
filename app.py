from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/music')
def music():
    return render_template('music.html')

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