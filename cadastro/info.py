def _mt_data_formata_cartao(mt_data):
    data_cartao = input("\nInforme a data de vencimento: ")
    data_cartao_verifica = data_cartao.replace(" ", "").replace("-", "").replace("/", "")

    digitos_data_cartao = []

    for caractere in data_cartao_verifica:
        if not caractere.isnumeric():
            digitos_data_cartao.append(caractere)

    if len(data_cartao_verifica) == 6 and len(digitos_data_cartao) == 0 and \
            int(data_cartao_verifica[0:2]) <= 12 and int(data_cartao_verifica[2:6]) >= 2022:

        data_cartao_re = f'{data_cartao_verifica[0:2]}/{data_cartao_verifica[4:6]}'

        print(f"\n{data_cartao_re}")

        mt_data.append(data_cartao_re)

    elif len(data_cartao_verifica) == 4 and len(digitos_data_cartao) == 0 and \
            int(data_cartao_verifica[0:2]) <= 12 and int(data_cartao_verifica[2:4]) >= 22:

        data_cartao_re = f'{data_cartao_verifica[0:2]}/{data_cartao_verifica[2:4]}'

        print(f"\n{data_cartao_re}")

        mt_data.append(data_cartao_re)

    else:
        print("\nData de vencimento invalida")

        _mt_data_formata_cartao(mt_data)


def data_def(mt_data_re):
    data = input("\nInforme sua data de nascimento: ")

    data_verifica = data.replace(" ", "").replace("-", "").replace("/", "")

    digitos_data = []

    for caractere_data in data_verifica:
        if not caractere_data.isnumeric():
            digitos_data.append(caractere_data)

    if len(data_verifica) == 8 and len(digitos_data) == 0 and int(data_verifica[0:2]) <= 31 and \
            int(data_verifica[2:4]) <= 12:

        data_re = f'{data_verifica[0:2]}/{data_verifica[2:4]}/{data_verifica[4:8]}'

        print(f"\n{data_re}")

        mt_data_re.append(data_re)

    elif len(data_verifica) == 6 and len(digitos_data) == 0 and int(data_verifica[0:2]) <= 31 and \
            int(data_verifica[2:4]) <= 12:

        data_re = f'{data_verifica[0:2]}/{data_verifica[2:4]}/20{data_verifica[4:6]}'

        print(f"\n{data_re}")

        mt_data_re.append(data_re)

    else:
        print("\ndigite uma data valida.")

        data_def(mt_data_re)


def cpf_def(cpf_re):
    try:
        cpf = int(input("\nInforme seu cpf: "))

        cpf_confirma = str(cpf)

        if len(cpf_confirma) == 11:
            cpf_formatado_re = f'{cpf_confirma[0:3]}.{cpf_confirma[3:6]}.{cpf_confirma[6:9]}-{cpf_confirma[9:12]}'

            print(f"\n{cpf_formatado_re}")

            cpf_re.append(cpf_formatado_re)

        else:
            print("\nDigite um CPF valido.")

            cpf_def(cpf_re)

    except ValueError:
        print("\nDigite um CPF valido.")

        cpf_def(cpf_re)


def nome_def(nome_re):
    nome = input("\nInforme seu nome completo: ").title()

    separa_nome = nome.split(" ")

    nome_verifica = nome.replace(" ", "")

    digitos_nome = []

    for caractere_nome in nome_verifica:
        if not caractere_nome.isalpha():
            digitos_nome.append(caractere_nome)

    if ' ' in nome and separa_nome[0] != separa_nome[-1] and len(digitos_nome) == 0:
        nome_formatado_re = f'{separa_nome[0]} {separa_nome[-1]}'

        print(f"\n{nome_formatado_re}")

        nome_re.append(nome_formatado_re)

    else:
        print("\nDigite um nome valido.")

        nome_def(nome_re)


def cartao_def(cartao_re, data_cartao_re):
    try:
        mt_data_re = []

        cartao = int(input("\nInforme o numero do cartão de credito: "))
        cartao_confirma = str(cartao)

        if len(cartao_confirma) == 16:
            cartao_formatado_re = f"{cartao_confirma[0: 4]}{8 * '*'}{cartao_confirma[12: 16]}"

            print(f"\n{cartao_formatado_re}")

            _mt_data_formata_cartao(mt_data_re)

            cartao_re.append(cartao_formatado_re)
            data_cartao_re.append(mt_data_re[0])

        elif len(cartao_confirma) == 15:
            cartao_formatado_re = f"{cartao_confirma[0: 4]}{7 * '*'}{cartao_confirma[11: 15]}"

            print(f"\n{cartao_formatado_re}")

            _mt_data_formata_cartao(mt_data_re)

            cartao_re.append(cartao_formatado_re)
            data_cartao_re.append(mt_data_re[0])

        elif len(cartao_confirma) == 14:
            cartao_formatado_re = f"{cartao_confirma[0: 4]}{6 * '*'}{cartao_confirma[10: 14]}"

            print(f"\n{cartao_formatado_re}")

            _mt_data_formata_cartao(mt_data_re)

            cartao_re.append(cartao_formatado_re)
            data_cartao_re.append(mt_data_re[0])

        elif len(cartao_confirma) == 13:
            cartao_formatado_re = f"{cartao_confirma[0: 4]}{5 * '*'}{cartao_confirma[9: 13]}"

            print(f"\n{cartao_formatado_re}")

            _mt_data_formata_cartao(mt_data_re)

            cartao_re.append(cartao_formatado_re)
            data_cartao_re.append(mt_data_re[0])

        else:
            print("\nCartão invalido.")

            cartao_def(cartao_re, data_cartao_re)

    except ValueError:
        print("\nCartão invalido.")

        cartao_def(cartao_re, data_cartao_re)
