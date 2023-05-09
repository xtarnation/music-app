from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/artists')
def artists():
    return render_template('artists.html')

if __name__ == '__main__':
    app.run(debug=True)