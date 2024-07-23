from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
@app.route('/cardapio')
def cardapio():

    pizzas = [{'sabor': 'Camarão', 'preco': '150', 'imagem': 'pizzacamarao.jpg'},
              {'sabor': 'Calabresa', 'preco': '50', 'imagem': 'pizzacalabresa.jpg'},
              {'sabor': 'Nordestina', 'preco': '60', 'imagem': 'pizzanordestina.jpg'},
            ]
    return render_template('cardapio.html', pizzas=pizzas)