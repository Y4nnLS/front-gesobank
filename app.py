from flask import Flask, request, jsonify, render_template
import hashlib
from hash import hash_usersenha, hash_sla
import requests
# resposta = requests.get('link da api')
# print(resposta.status_code)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    features = request.json
    X = []
    senha = str(features['senha'])
    nome = str(features['nome'])
    userHash = hash_usersenha(nome, senha)
    passwordHash = hash_sla(nome)
    X.append(userHash)
    X.append(passwordHash)
    X.append(features['nome_completo'])
    X.append(features['cpf'])
    X.append(features['telefone'])
    
    
    
   
    return jsonify(X)

if __name__ == "__main__":
    app.run(debug=True)