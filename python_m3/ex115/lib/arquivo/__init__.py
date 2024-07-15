from ex115.lib.interface import cabeçalho
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    with open(nome, 'w', encoding='utf-8') as arquivo:
        arquivo.write('')


def mostrarArquivo(nome):
    with open(nome, 'r', encoding='utf-8') as arquivo:
        cabeçalho('PESSOAS CADASTRADAS')
        nomes = arquivo.readlines() #Vai ler linha por linha
        for nome in nomes:
            nomeSeparado = nome.split(';') #Vai separar bem na parte que tem o ;
            nomeSeparado[1] = nomeSeparado[1].replace('\n', '') # vai substituir o \n por '' para não quebrar linha
            print(f'{nomeSeparado[0]:<30}{nomeSeparado[1]:>3} anos')

def adicionarPessoa(nome, idade):
    with open('nomes.txt', 'a+', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome};{idade}\n')