import os
import math
def podeJogar(tabuleiro):
    for i in tabuleiro:
        if i == 0:
            return True
    else: return False

def parserNumero(numero):
    if numero == 0:
        return ' '
    elif numero == 1:
        return 'X'
    else:
        return 'O'
        
def PrintTabuleiro(tabuleiro):
    print(tabuleiro)
    print('  1 2 3')
    print(' -------')    
    for i in range(3):
        print(chr(i+65) + '|', end = '')
        for j in range(3):
            print(parserNumero(tabuleiro[i*3+j]), end= '|')
        print('\n -------')    

def jogada(turno, tabuleiro, maquina=False, posicao=0):
    if maquina:
        tabuleiro[posicao]=turno
        if turno == 1: return 2
        else: return 1
    valor =  input('digite a sua jogada: ')
    if valor == ':h':
        print('digite a sua jogada no formato "linha,coluna", por exemplo: A,1')
        return turno
    else:
        linha,coluna = list(valor.upper())
        linha = ord(linha)-65
        tabuleiro[linha*3+int(coluna)-1] = turno
        return inverteTurno(turno)

def checaVitoria(tabuleiro):
    string = "".join(map(str,tabuleiro))
    winConditions = (
        0b111000000,
        0b000111000,
        0b000000111,
        0b100100100,
        0b010010010,
        0b001001001,
        0b100010001,
        0b001010100
    )
    stringO = int(string.replace("1","0").replace("2","1"),2)
    stringX = int(string.replace("2","0"),2)
    vitoria = 0
    for i in range(len(winConditions)):
        if (stringX&winConditions[i]==winConditions[i]):
            vitoria = 1
            break
        elif (stringO&winConditions[i]==winConditions[i]):
            vitoria = 2
            break
    return vitoria

def inverteTurno(turno):
    if turno == 1: return 2
    else: return 1

def minValue(tabuleiro, turno, profundidade):
    minimo = math.inf
    resultado = checaVitoria(tabuleiro)
    if resultado == 1:
        return 10
    elif resultado == 2:
        return -10
    elif not podeJogar(tabuleiro):
        return 0
    for i in range(len(tabuleiro)):
        copiaTabuleiro = list(tabuleiro)
        if copiaTabuleiro[i] == 0:
            copiaTabuleiro[i] = turno
            contador = maxValue(copiaTabuleiro, 1, profundidade+1)
            minimo = min(contador,minimo)
    return minimo+profundidade

def maxValue(tabuleiro, turno, profundidade):
    maximo = -math.inf
    resultado = checaVitoria(tabuleiro)
    if resultado == 1:
        return 10
    elif resultado == 2:
        return -10
    elif podeJogar(tabuleiro):
        return 0
    for i in range(len(tabuleiro)):
        copiaTabuleiro = list(tabuleiro)
        if copiaTabuleiro[i] == 0:
            copiaTabuleiro[i] = turno
            contador = minValue(copiaTabuleiro, 2, profundidade+1)
            maximo = max(contador,maximo)
            
    return maximo-profundidade

def minMaxDecision(tabuleiro, turno, jogadas,tipo='m'):
    posicao = None
    valor = -math.inf
    for i in range(len(tabuleiro)):
        copiaTabuleiro = list(tabuleiro)
        if copiaTabuleiro[i] == 0:
            copiaTabuleiro[i] = 1
            if tipo == "m":
                contador  = minValue(copiaTabuleiro, 2, 0)
            if contador > valor:
                valor = contador
                posicao = i
    tabuleiro[posicao] = 2
    return tabuleiro

def main():
    tabuleiro = [0,0,0,0,0,0,0,0,0]
    fimDeJogo = False
    turno = 1
    jogadas=0
    while(not fimDeJogo):
        os.system('cls' if os.name == 'nt' else 'clear')
        PrintTabuleiro(tabuleiro)
        if(turno==2):
            tabuleiro=minMaxDecision(tabuleiro, turno, jogadas)
            proximoTurno = 1
            jogadas+=1
        else:
            proximoTurno = jogada(turno, tabuleiro)
            jogadas+=1
        vitoria = checaVitoria(tabuleiro)
        if vitoria == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            PrintTabuleiro(tabuleiro)
            print("X Ganhou!")
            fimDeJogo=True
        elif vitoria == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            PrintTabuleiro(tabuleiro)
            print("O ganhou!")
            fimDeJogo=True
        elif vitoria == 0 and jogadas == 9:
            os.system('cls' if os.name == 'nt' else 'clear')
            PrintTabuleiro(tabuleiro)
            print("Empate!")
            fimDeJogo=True
        turno = proximoTurno
main()
while(True):
    denovo = input("Deseja jogar novamente? (S/n): ")
    if denovo != "n":
        main()
    else:
        break
