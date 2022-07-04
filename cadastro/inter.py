from info import *
import pyodbc

print('''
Bem vindo ao banco de dados Nebur.

Cadastre ja o seu cartão!''')


def cadastro():
    nome = []
    cpf = []
    data = []
    cartao = []
    cartao_data = []

    nome_def(nome)
    cpf_def(cpf)
    data_def(data)
    cartao_def(cartao, cartao_data)

    try:
        print("\nAguarde em quanto salvamos suas informações...")

        dados_da_conexao = (
            'Driver={SQL Server};'
            'Server=FeelXPC;'
            'Database=Nebur;'
        )

        conexao = pyodbc.connect(dados_da_conexao)

        cursor = conexao.cursor()

        comando = f"""INSERT INTO Info_Client(Client_Name, CPF, Birth_Day, Number_Card, Expiration_Date)
                VALUES
                    ('{nome[0]}', '{cpf[0]}', '{data[0]}', '{cartao[0]}', '{cartao_data[0]}')"""

        cursor.execute(comando)
        cursor.commit()

    except Exception as erro:
        print(f"\nAlgo deu errado com a comunicação com o banco de dados.{erro}")

        cadastro()

    print("\nInformações salvas com sucesso.")

    def responder():
        resposta = int(input("""
Digite 1: Para fazer outro cadastro.
        
Digite 2: Para consultar suas informações.
        
Digite 3: Para sair.
    
> """))

        if resposta == 1:
            cadastro()

        elif resposta == 2:
            print(f"""
Nome: {nome[0]}
CPF: {cpf[0]}
Nascimento: {data[0]}
Numero do cartão: {cartao[0]}
Data de validade: {cartao_data[0]}""")

            responder()

        elif resposta == 3:
            print("\nMuito obrigado por escolher os nossos serviços.")

        else:
            print("\nNumero invalido")

            responder()

    responder()


cadastro()
