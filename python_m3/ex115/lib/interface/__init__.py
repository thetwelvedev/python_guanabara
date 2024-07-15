def leiaInt(msg):
    while True:
        try:
            scan = int(input(msg)) #Vai ler a mensagem, que nem o scanf em C/o input pode apararecer abaixo da mensagem de print
        except ValueError:
            print('Recebemos apenas número em algarismo indo-arábicos')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados')
            break
        except Exception as erro:
            print(f'O problema encontrado foi {erro.__cause__}')
            continue
        else:  #Se der certo retorna o valor
            return scan


def linha(tam = 42):
    return '-' *tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for i, item in enumerate(lista):
        print(f'\033[33m{i+1}\033[m - \033[34m{item}\033[m')
    print(linha())
    opção = leiaInt('\033[32mSua Opção: \033[m') #Vai ser a opção do menu
    return opção