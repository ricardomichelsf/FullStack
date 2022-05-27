import os
from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('calculo.html')


@app.route('/calcule', methods=['POST', 'GET'])
def calcule():
    valor1 = request.form['v1']
    valor2 = request.form['v2']
    operacao = request.form['operacao']
    v1 = int(valor1)
    v2 = int(valor2)

    if operacao == 'somar':
        resultado = v1 + v2
    elif operacao == 'subtrair':
        resultado = v1 - v2
    elif operacao == 'multiplicar':
        resultado = v1 * v2
    elif operacao == 'raiz':
        resultado = math.sqrt(v1)
    elif operacao == 'log':
        resultado = math.log(v1)
    elif operacao == 'expo':
        resultado = math.pow(v1,v2)
    elif operacao == 'divisao':
        if v1 == 0 or v2 == 0:
            resultado = "Erro divisao por 0"
        else:
            resultado = v1 / v2
    return str(f'O total é: {resultado}')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)