import os

def opcoes():
    print ('1. Cadastrar')
    print ('2. Listar')
    print ('3. ativar')
    print ('4. Sair\n')


def escolher_opcoes():
    valor_bruto = int(input('Escolha um valor:'))

    if valor_bruto == 1:
        print('voce escolheu cadastrar')
    elif valor_bruto == 2:
        print ('voce escolheu listar')
    elif valor_bruto == 3:
        print ('voce escolheu 3')
    else:
        os.system('clear')

def main():
    opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()