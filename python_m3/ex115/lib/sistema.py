from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
#Verificar se o arquivo existe
arquivo = 'nomes.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)
while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        mostrarArquivo(arquivo)
    elif resposta == 2:
        cabeçalho('CADASTRANDO PESSOAS')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        print(f'Registro de {nome} adicionado!')
        adicionarPessoa(nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do programa... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)