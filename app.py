import os

def opcoes():
    print ('1. Cadastrar')
    print ('2. Listar')
    print ('3. ativar')
    print ('4. Sair\n')

def finalizar_app():
    os.system('clear')
    print('Digite uma opcao valida \n')
    main()

def opcao_invalida():
    print('opcao invalida\n')
    main()


def escolher_opcoes():
    try:
        valor_bruto = int(input('Escolha um valor:'))

        if valor_bruto == 1:
            print('voce escolheu cadastrar')
        elif valor_bruto == 2:
            print ('voce escolheu listar')
        elif valor_bruto == 3:
            print ('voce escolheu 3')
        elif valor_bruto == 4:
            finalizar_app()
        else:
            opcao_invalida()
            os.system('clear')
    except:
            opcao_invalida()
def main():
    opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()