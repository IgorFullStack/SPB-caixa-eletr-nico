# Cadastro
def get_user_name():
    """Get user name"""
    return input("Informe seu nome: ")

def validate_card_number():
    """Validate card number"""
    while True:
        cartao_numero = input("Informe o número do seu cartão (16 digitos): ")
        if len(cartao_numero) == 16 and cartao_numero.isdigit():
            formatted_cartao_numero = ".".join([cartao_numero[i:i+4] for i in range(0, len(cartao_numero), 4)])
            print("Cartão válido \n")
            return formatted_cartao_numero
        else:
            print("Cartão inválido")

def main():
    nome = get_user_name()
    cartao_numero = validate_card_number()
    print(f'Usuario: {nome} \nCartão: {cartao_numero} \n')

    # Caixa Eletrônico
    saldo = 5200.0

    while True:
        print("Em que posso ajudar?")
        opcao = int(input("[1] Sacar \n[2] Extrato \n[3] Depositar \n[0] Sair \n: "))

        if opcao == 1:
            try:
                print(f"Saldo total: R${saldo:.2f} \n")
                valor = float(input("Informe a quantia para saque: "))
                if saldo >= valor:
                    print("Realizando saque... \n")
                    saldo -= valor
                    print(f"Saldo total de {nome}: R${saldo:.2f} \n")
                else:
                    print("Saldo insuficiente!")
            except ValueError:
                print("Valor de saque inválido. Por favor, insira um número.")

        elif opcao == 2:
            print("Exibindo o extrato...")
            print(f"Saldo total de {nome}: R${saldo:.2f} \n")

        elif opcao == 3:
            try:
                print(f"Saldo total: R${saldo:.2f} \n")
                valor = float(input("Informe a quantia para depositar: "))
                if valor > 0:
                    print("Realizando depósito... \n")
                    saldo += valor
                    print(f"Saldo total de {nome}: R${saldo:.2f} \n")
                else:
                    print("Valor de depósito inválido. Por favor, insira um número.")
            except ValueError:
                print("Valor de depósito inválido. Por favor, insira um número.")

        elif opcao == 0:
            print("Saindo...")
            print(f"Obrigado por ser nosso cliente, tenha um bom dia senhor(a) {nome}!")
            break

        else:
            print("Opção inválida. Por favor, insira 1, 2, 3 ou 0. \n")

if __name__ == "__main__":
    main()
