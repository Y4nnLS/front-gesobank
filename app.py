from flask import Flask, request, jsonify, render_template,redirect, url_for
import hashlib
from hash import hash_usersenha, hash_sla
import requests

app = Flask(__name__)

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

@app.route('/transferencia', methods=['POST', 'GET'])
def transferencia():
    if request.method == 'POST':
        valor = request.form['valor']
        data = request.form['data']
        destinatario = request.form['destinatario']
        telefone_destinatario = request.form['telefone_destinatario']

        return render_template('transferencia.html')
    else:
        return render_template('transferencia.html')


class Atividade:
    def __init__(self, tipo, data, valor, de=None, para=None, nome_cartao=None, numero_cartao=None,valor_emprestado=None):
        self.tipo = tipo
        self.data = data
        self.valor = valor
        self.de = de
        self.para = para
        self.nome_cartao = nome_cartao
        self.numero_cartao = numero_cartao
        self.valor_emprestado = valor_emprestado

historico_conta = [
    Atividade("Transferência Recebida", "2024-05-01", 1500, de="João da Silva", numero_cartao="123***********53"),
    Atividade("Transferência Enviada", "2024-05-03", 500, para="Maria Oliveira", numero_cartao="456***********32"),
    Atividade("Empréstimo", "2024-03-12", 1000, valor_emprestado=1000),
    Atividade("Cartão Salvo", "2024-05-07", 0, nome_cartao="Cartão de Crédito", numero_cartao="789***********71"),
    Atividade("Cartão Deletado", "2024-05-09", 0, nome_cartao="Cartão de Débito", numero_cartao="321***********84"),
]

@app.route('/historico')
def historico():
    return render_template('historico.html', historico=historico_conta)


if __name__ == "__main__":
    app.run(debug=True)