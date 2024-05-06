from flask import Flask, request, jsonify, render_template,redirect, url_for
from hash import hash_usersenha, hash_sla
import requests

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@app.route('/login',methods=['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        features = request.json
        senha = str(features['senha'])
        nome = str(features['nome'])
        userHash = hash_sla(nome)
        passwordHash = hash_sla(senha)
        url = 'http://localhost:5000/user/login'  # Substitua localhost:5000 pela URL correta do seu back-end
        dados = {"userHash": userHash, "passwordHash": passwordHash}
        response = requests.post(url, json=dados)
        print(response.json())  # Exibindo a resposta do back-end
        return jsonify(response)
    return render_template('login.html')


@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if(request.method == 'POST'):
        features = request.json
        senha = str(features['senha'])
        nome = str(features['nome'])
        name = str(features['nome_completo'])
        cpf = str(features['cpf'])
        phone = str(features['telefone'])
        userHash = hash_sla(nome)
        passwordHash = hash_sla(senha)
        url = 'http://localhost:5000/user/register'  # Substitua localhost:5000 pela URL correta do seu back-end
        dados = {"userHash": userHash, "passwordHash":passwordHash,"name": name,"cpf": cpf,"phone":phone}
        response = requests.post(url, json=dados)
        print(response.json())  # Exibindo a resposta do b
        return jsonify(response)
    return render_template('cadastro.html')

@app.route('/emprestimo', methods=['POST', 'GET'])
def emprestimo():
    if(request.method == 'POST'):
        features = request.json
        senha = str(features['senha'])
        nome = str(features['nome'])
        value = str(features['nome_completo'])
        userHash = hash_sla(nome)
        passwordHash = hash_sla(senha)
        url = 'http://localhost:5000/user/register'  # Substitua localhost:5000 pela URL correta do seu back-end
        dados = {"userHash": userHash, "passwordHash":passwordHash,"value": value}
        response = requests.post(url, json=dados)
        print(response.json())  # Exibindo a resposta do b
        return jsonify(response)
    return render_template('emprestimo.html')

@app.route('/transferencia', methods=['POST', 'GET'])
def transferencia():
    if request.method == 'POST':
        features = request.json
        senha = str(features['senha'])
        nome = str(features['nome'])
        value = request.form['valor']
        receiverName = request.form['destinatario']
        receiverCpf = request.form['CPF']
        receiverPhone = request.form['telefone']
        userHash = hash_sla(nome)
        passwordHash = hash_sla(senha)
        url = 'http://localhost:5000/transference'  # Substitua localhost:5000 pela URL correta do seu back-end
        dados = {"userHash": userHash, "passwordHash":passwordHash,"value": value,"receiverName": receiverName,"receiverCpf": receiverCpf,"receiverPhone": receiverPhone}
        response = requests.post(url, json=dados)
        print(response.json())  # Exibindo a resposta do b
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