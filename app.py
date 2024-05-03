from flask import Flask, request, jsonify, render_template,redirect, url_for
import hashlib
from hash import hash_usersenha, hash_sla
import requests
# resposta = requests.get('link da api')
# print(resposta.status_code)

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('login.html')
@app.route('/', methods=['POST', 'GET'])
@app.route('/login',methods=['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        features = request.json
        X = []
        senha = str(features['senha'])
        nome = str(features['nome'])
        userHash = hash_usersenha(nome, senha)
        passwordHash = hash_sla(nome)
        X.append(userHash)
        X.append(passwordHash)
        return jsonify(X)
    return render_template('login.html')


@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if(request.method == 'POST'):
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
    return render_template('cadastro.html')

@app.route('/emprestimo', methods=['POST', 'GET'])
def emprestimo():
    return render_template('emprestimo.html')

if __name__ == "__main__":
    app.run(debug=True)