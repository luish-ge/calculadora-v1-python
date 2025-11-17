import os

def multiplicacao(x, y):
    '''Função responsável pela multiplicação'''
    return x * y

def divisao(x, y):
    '''Função responsável pela divisão'''
    return x / y

def soma(x, y):
    '''Função responsável pela soma'''
    return x + y

def subtracao(x, y):
    '''Função responsável pela subtração'''
    return x - y

def encerrar_programa():
    os.system('cls')
    print('Programa encerrado, até logo!')

def nome_programa():
    titulo = 'ＣＡＬＣＵＬＡＤＯＲＡ'
    linha = '*' * (len(titulo))
    print(linha)
    print(titulo)
    print(linha)

def exibir_opcoes():
    '''Função responsável por exibir as opções de seleção'''
    print('1. Multiplicação')
    print('2. Divisão')
    print('3. Soma')
    print('4. Subtração')
    print('5. Encerrar programa')

def selecionar_valores_multiplicacao():
    '''Realiza o cálculo de multiplicação'''
    os.system('cls')
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))
    print('O resultado da multiplicação é: ', multiplicacao(x, y))
    retorno_menu()

def selecionar_valores_divisao():
    '''Realiza o cálculo de divisão'''
    os.system('cls')
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))
    print('O resultado da divisão é: ', divisao(x, y))
    retorno_menu()

def selecionar_valores_soma():
    '''Realiza o cálculo de soma'''
    os.system('cls')
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))
    print('O resultado da soma é: ', soma(x, y))
    retorno_menu()

def selecionar_valores_subtracao():
    '''Realiza o cálculo de subtração'''
    os.system('cls')
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))
    print('O resultado da subtração é: ', subtracao(x, y))
    retorno_menu()

def retorno_menu():
    '''Função para retornar ao menu após concluir o cálculo'''
    try:
         retorno = int(input('Digite 1 para retornar ao menu principal ou 2 para encerrar o programa.'))
         if retorno == 1:
                main()
         elif retorno == 2:
                encerrar_programa()
    except:
            opcao_errada()
            retorno_menu()
    
def opcao_escolhida():
    ''' Função responsável por direcionar o usuário para o tipo de cálculo selecionado na função "exibir_opcoes" '''
    try:
        numero_escolhido = int(input('Escolha uma opção: '))

        if numero_escolhido == 1:
            selecionar_valores_multiplicacao()
        elif numero_escolhido == 2:
            selecionar_valores_divisao()
        elif numero_escolhido == 3:
            selecionar_valores_soma()
        elif numero_escolhido == 4:
            selecionar_valores_subtracao()
        elif numero_escolhido == 5:
            encerrar_programa()
    except:
        print('O valor digitado não é um número, tente novamente.')
        opcao_escolhida()

def opcao_errada():
    '''Caso o usuário coloque uma letra ou número não correspondente as opções, mostra essa mensagem na tela'''
    print('A opção escolhida não condiz com nenhuma opção, tente novamente ou entre em contato com o fabricante da calculadora.')

def main():
    os.system('cls')
    nome_programa()
    exibir_opcoes()
    opcao_escolhida()

if __name__ == '__main__':
    main()


    
