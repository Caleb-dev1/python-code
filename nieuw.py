from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welkom op mijn website!'

@app.route('/contact')
def contact():
    return 'Contactpagina'

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/contact')
def contact():
    return 'Contactpagina'

