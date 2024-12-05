from flask import Flask, request, jsonify
from flask_cors import CORS
from connector_db import connection,cursor
import requests


#inicia a api
app = Flask(__name__)
CORS(app)

if not connection or not connection.is_connected():
    print("Conexão com banco de dados falhou.")
    exit(1)

#Rota health check
@app.route('/')

#Conecta APIs
def fetch_cep(cep):
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json")
    if response.status_code == 200:
        return response.json()
    return None

def index():
    return jsonify({"mesage": "API rodando com sucesso."})

def fetch_cep():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
    if response.status_code == 200:
        return response.json().get('bpi', {}).get('USD', {}).get('rate')
    return 'Unavailable'

@app.route('/clientes', methods[POST])
def create_client():
    data = request.json
    nome = data['nome']
    email = data['email']
    cep = data['cep']
    endereco_info = fetch_cep(cep)
    if endereco_info:
        endereco = f"{endereco_info['logradouro']}, {endereco_info['bairro']}, {endereco_info['localidade']}-{endereco_info['uf']}"
    else:
        endereco = "CEP inválido"

    query = "INSERT INTO clientes(nome, email, cep, endereco) VALUES (%s, %s, %s, %s)"
    values = (nome, email, cep, endereco)
    cursor.execute(query, values)
    connection.commit
    return jsonify({"Message: Cliente criado com sucesso."})
if __name__ == '__main__':
    app.run(debug=True)