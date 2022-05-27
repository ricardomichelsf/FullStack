import os
from flask import Flask, jsonify, request, render_template
from math import sqrt
import mysql.connector 

app = Flask(__name__)

db_connection = mysql.connector.connect(
    host='localhost', user='root', password='', database='bdbaraohand')

mycursor = db_connection.cursor()

print(db_connection)

@app.route('/')
def main():
    return render_template('indice.html')


@app.route('/calculaform', methods=['POST', 'GET'])
def criarPedido():
    sql = "INSERT INTO pedido (id_pedido, id_cliente, id_produto, valor_pedido) VALUES (%s, %s, %s, %s)"
    valores =  #COLOCAR OS VALORES DO FORM AQUI - STRING SEPARADOS POR VIRGULAS
    mycursor.execute(sql, valores)
    db_connection.commit()
    
    print(mycursor.rowcount, "record inserted.")

#QUANDO UM PEDIDO É CRIADO, PRECISA ALTERAR A TABELA DE INGREDIENTES (DIMINUIR 
# NA TABELA ESTOQUE)

    return criarPedido


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)


print(mycursor.rowcount, "record inserted.")