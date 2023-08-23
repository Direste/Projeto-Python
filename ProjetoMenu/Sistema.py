from ProjetoMenu.lib.interface import *
from ProjetoMenu.lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sisema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opcao válida!\033[m')
    sleep(2)