#importando as bibliotecas usadas no jogo
from re import A
from secrets import choice
import time #import do time para usar na animacao da tela inicial
import pandas as pd #import do panda para ler a planiha com as palavras
import random #import do random para escolher a palavra do jogo
import os #import do os para limpar a tela do terminal
import images as im #importando o arquivo imagens para formar as telas

#criando a variavel do banco de dados e acessando o arquivo com as palavras
banco_de_dados_palavras = pd.read_excel('C:\\Users\\Daniel Jordan\\OneDrive\\Ironhack\\Projeto_Forca\\banco de dados forca.xlsx')
#sorteando o numero para escolher a palavra
escolha = random.randrange(0,90)
#definindo a palavra do jogo baseado ba variavel escolha
palavra_escolhida = (banco_de_dados_palavras.Descricao[escolha]).upper()
#acessando o tipo da palavra para colocar na tela do jogo
tipo_da_palavra = (banco_de_dados_palavras.Tipo[escolha]).upper()
#criando a lista das palavras para usar no jogo
letras = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
#inicializando variaveis
#criando lista para armazenar as letras erradas
letras_erradas = []
#criando uma lista para armazenar as letras corretas
letras_corretas = []
progresso = ''
#criando a variavel para controlar quantas vezes o usuario errou
erros = 0
#criando a variavel para armazenar quantas vezes o usuário acertou
acertos = 0
largura = 60
#criando a variavel que exibira a palavra oculta com o _
mensagem = len(palavra_escolhida) * '_  '

#limpando a tela do terminal
os.system('cls' if os.name == 'nt' else clear)
#carregando a tela de abertura
fps = 0 
#animacao de load na tela de abertura
while fps < 19:
    os.system('cls' if os.name == 'nt' else clear)
    im.tela_inicial()
    #printando a barra de progresso que incrementa em cada loop passando a ideia de animacao
    print('Carregando  ' + '█ ' * fps)
    fps += 1
    time.sleep(0.2)
    

time.sleep(1)
os.system('cls' if os.name == 'nt' else clear)
#criando dicionario com os caracteres que vao ser usado no jogo

#criando o dicionario que fazem a imagem do boneco da forca se formar
forca_status = {
            'forca_0' : (1,2,3,3,3,3),
            'forca_1' : (1,2,4,3,3,3),
            'forca_2' : (1,2,4,2,3,3),
            'forca_3' : (1,2,4,5,3,3),
            'forca_4' : (1,2,4,6,3,3),
            'forca_5' : (1,2,4,6,7,3),
            'forca_6' : (1,2,4,6,8,3),
            'forca_7' : (1,2,4,9,6,8)
            }
#criando funcao para limpar a tela e depois imprimir a tela atualizada
def imprimir_tela(indices:list,y=im.imagen_forca()):
    '''Imprime a tela do Jogo'''
    x = 0
    print('╔'+ 12*'═' +'╦' +('═'* 45)+'╗') #primeira linha da tela do jogo
    print('║'+ f' CHANCES: {7-erros} ║' + 16*' ' + 'JOGO DA FORCA' + 16*' ' + '║')#segunda linha da tela do jogo
    print('╠'+  12 *'═' + '╬' +'═'* 45 + '╣')#terceira linha da tela do jogo
    #criando laco para buscar do dicionario e imprimir o boneco
    for indice in indices:    
        if x == 5:
            print(f'{y[indice]}   ' + mensagem +(42 - len(mensagem)) * ' ' + '║')
        print(f'{y[indice]}' + (largura - 15) * ' ' + '║')
        x +=1
    print('╠' +'═'*12 +'╩' +'═'*45 + '╣')
    #criando a lista do alfabeto 
    linha_alfabeto = " ".join(letras).upper()
    #verificando se a letra esta na lista de letras erradas e colorindo ela de vermelho
    for l in linha_alfabeto:
        if l in letras_erradas:
            linha_alfabeto = linha_alfabeto.replace(l,'\033[91m' + l + '\33[0m')            
    
    print(F'║    {linha_alfabeto}     ║')
    print('╠' + '═'*58 + '╣')
    #imprimindo a categoria da palavra
    print('║  CATEGORIA - ' + tipo_da_palavra + ' '*(44 - (len(tipo_da_palavra))) + '║' )
    print('╚' + '═'*58 + '╝')



os.system('cls' if os.name == 'nt' else clear)
#limpando a tela e chamando a funcao de imprimir a tela ela usa o metodo get para consultar o dicionario e ver qual boneco ela tem que imrimir
imprimir_tela(forca_status.get('forca_0'))

status = forca_status.get('forca_0')

#criando o laco para o jogo ficar rodando
while True:
    mensagem = ''

    #capturando letra digitada pelo usuario
    letra_escolhida = input('\nDigite a letra: ').upper()
    os.system('cls' if os.name == 'nt' else clear) 
    #verificando se a letra digitada nao esta na lista de letras corretas ou na lista de letras erradas
    if letra_escolhida in letras_corretas or letra_escolhida in letras_erradas:
        os.system('cls' if os.name == 'nt' else clear)
        #atualizando a lista onde fica a palavra a ser acertada e verificando se o usuario ja digitou a letra caso ja tenha digitado ira dar uma mensagem
        for letra in palavra_escolhida:
            if letra in letras_corretas:
                mensagem += letra + '  '
            else:
                mensagem += '_  '
        imprimir_tela(status)
        print('Voce ja digitou esta letra!!!')
        continue
    #verificando se a letra escolhida exite na palavra escolhida e se ela ja nao esta nas lista de erradas 
    if letra_escolhida not in palavra_escolhida and letra_escolhida not in letras_erradas:
        letras_erradas.append(letra_escolhida)
        erros +=1
        #controle da linha da palavra
        for letra in palavra_escolhida:
            if letra in letras_corretas:
                mensagem += letra + '  '
            else:
                mensagem += '_  '
        #buscando o boneco baseado no número de erros
        status = forca_status.get('forca_'+ str(erros))
    else:
        #contabilizando os acertos
        if letra_escolhida not in letras_corretas and letra_escolhida not in letras_erradas and letra_escolhida  != "":
            acertos +=1
        #adicionando a letra escolhida na lista de letras corretas
        letras_corretas.append(letra_escolhida)
        #controle da linha da palavra
        for letra in palavra_escolhida:
            if letra in letras_corretas:
                mensagem += letra + '  '
                
            else:
                mensagem += '_  '
    
    imprimir_tela(status)
    #verificando se o usuario ja ganhou
    if acertos == len(''.join(set(palavra_escolhida.replace(' ', '')))):
        os.system('cls' if os.name == 'nt' else clear)
        im.tela_vitoria()
        #verificando se o usuario quer jogar novamente
        resposta = ''
        while resposta != 'S' and resposta != 'SIM' and resposta != 'N' and resposta != 'NAO':
            resposta = input('QUER JOGAR NOVAMENTE?').upper()
            print(resposta)
        #redefinindo variaveis para comecar um novo jogo
        if resposta == 'S' or resposta == 'SIM':
            escolha = random.randrange(0,90)
            palavra_escolhida = (banco_de_dados_palavras.Descricao[escolha]).upper()
            tipo_da_palavra = (banco_de_dados_palavras.Tipo[escolha]).upper()
            letras = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
            letras_erradas = []
            letras_corretas = []
            erros = 0
            acertos = 0
            largura = 60
            mensagem = len(palavra_escolhida) * '_  '
            status = forca_status.get('forca_0')
            os.system('cls' if os.name == 'nt' else clear)
            imprimir_tela(forca_status.get('forca_0'))
        if resposta == 'N' or resposta == 'NAO':
            break
    #verificando se o usuário perdeu o jogo       
    if erros == 7:
        os.system('cls' if os.name == 'nt' else clear)
        im.tela_game_over()
        print(f'              A PALAVRA ERA: {palavra_escolhida}\n')
        resposta = ''
        while resposta != 'S' and resposta != 'SIM' and resposta != 'N' and resposta != 'NAO':
            resposta = input('QUER JOGAR NOVAMENTE? ').upper()
            print(resposta)
        if resposta == 'S' or resposta == 'SIM':
            escolha = random.randrange(0,90)
            palavra_escolhida = (banco_de_dados_palavras.Descricao[escolha]).upper()
            tipo_da_palavra = (banco_de_dados_palavras.Tipo[escolha]).upper()
            letras = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
            letras_erradas = []
            letras_corretas = []
            erros = 0
            acertos = 0
            largura = 60
            mensagem = len(palavra_escolhida) * '_  '
            status = forca_status.get('forca_0')
            os.system('cls' if os.name == 'nt' else clear)
            imprimir_tela(forca_status.get('forca_0'))
        if resposta == 'N' or resposta == 'NAO':
            break
