from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Получаем случайную цитату
    quote = get_random_quote()
    return render_template('index.html', quote=quote)

@app.route('/new_quote')
def new_quote():
    # Получаем новую случайную цитату
    quote = get_random_quote()
    return jsonify(quote)

def get_random_quote():
    response = requests.get('https://api.quotable.io/random', verify=False)
    data = response.json()
    return {'content': data['content'], 'author': data['author']}

if __name__ == '__main__':
    app.run(debug=True)