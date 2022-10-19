# importa as libs que serão usadas no projeto
from flask import Flask, jsonify, render_template
from dados import load


# instancia o flask 
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

# cria uma rota chamada /carros onde ira retornar todas as marcas
@app.get('/carros')
def returncarros():
    # carrega o arquivo json na variavel marcas
    marcas = load('carros.json')

    # faz a contagem da quantidade de carros e da quantidade de marcas cadastradas
    c_marcas = 0
    c_carros = 0
    for c, v in marcas.items():
        c_marcas +=1
        c_carros += len(v)

    return jsonify({"quantidade de marcas": c_marcas}, {'quantidade carros': c_carros}, {'carros': marcas})


# cria uma rota chamada /carros que tem um parâmetro marca, e que retorna uma marca especifica
@app.get('/carros/<marca>')
def returncarrosmarca(marca : str):
    # carrega o arquivo json na variavel marcas
    marcas = load('carros.json')
    return {'carros' : marcas[marca]}


if __name__ == '__main__':
    app.run(debug=True)