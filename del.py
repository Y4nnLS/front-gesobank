from flask import Flask, request
from ..Controllers.UserController import UserController
from ..Controllers.CardController import CardController
from ..Controllers.TransferenceController import TransferenceController
from ..Controllers.LoanController import LoanController

def registrar_rotas(app:Flask):

    ###############
    ##  Usuário  ##
    ###############

    @app.route('/user/login', methods=['POST'])
    def login_user():
        data = request.get_json() 
        return UserController.login_user(data)
    
    @app.route('/user/register', methods=['POST'])
    def register_user():
        data = request.get_json() 
        return UserController.register_user(data)
    
    @app.route('/user/data', methods=['GET'])
    def user_data():
        data = request.get_json()
        return UserController.get_user_data(data)
    
    @app.route('/user/balance', methods=['GET'])
    def user_balance():
        data = request.get_json()
        return UserController.get_user_balance(data)
    
    @app.route('/user/check', methods=['POST'])
    def check_user():
        data = request.get_json() 
        return UserController.check_user(data)
    
    #####################
    ##  Transferencia  ##
    #####################

    @app.route('/transference', methods=['POST'])
    def transference():
        data = request.get_json()
        return TransferenceController.transference(data)
    
    ##################
    ##  Empréstimo  ##
    ##################

    @app.route('/loan', methods=['POST'])
    def loan():
        data = request.get_json()
        return LoanController.loan(data)

    ##############
    ##  Cartão  ##
    ##############

    @app.route('/card/register', methods=['POST'])
    def register_card():
        data = request.get_json() 
        return CardController.register_card(data)
    
    @app.route('/card/get', methods=['GET'])
    def get_card():
        data = request.get_json() 
        return CardController.get_card(data)
    
    @app.route('/card/get-one-card', methods=['GET'])
    def get_one_card():
        data = request.get_json() 
        return CardController.get_one_card(data)
    
    @app.route('/card/delete', methods=['DELETE'])
    def delete_card():
        data = request.get_json() 
        return CardController.delete_card(data)