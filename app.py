from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>ALHAMDULILLAH</h1>'

@app.route('/muaaz')
def magic():
    return '<h1>ALHAMDULILLAH</h1> <h2>MuAaZ</h2>'

if __name__ == '__main__':
    app.run()
