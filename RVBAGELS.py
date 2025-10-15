#RVBAGELS

import random

DIGITOS = 3
OPORTUNIDADES = 10

def unNumeroSecreto():
    digitos = list('1234567890')
    random.shuffle(digitos)
    nSecreto = ''
    for i in range(DIGITOS):
        nSecreto += str(digitos[i])
#    print(digitos, ' ', nSecreto)
    return nSecreto

def tecleaNum():
    intento = ''
    while len(intento) != DIGITOS or not intento.isdecimal():
        intento = input('Teclea un numero de 3 digitos >')
    return intento

def intentos():
    numSecreto = unNumeroSecreto()
    print(numSecreto)
    intentoNum = 1
    while intentoNum <= OPORTUNIDADES:
        print('Intento: #{}'.format(intentoNum))
        numTecleado = tecleaNum()
        print(verificaPistas(numTecleado, numSecreto))
        if numTecleado == numSecreto:
            break
        intentoNum += 1
        if intentoNum > OPORTUNIDADES:
            print('Quieres jugar de nuevo? (Si / No)')
            if not input('>').lower().startswith('s'):
                print('Gracias por Jugar! ...')
                break

def verificaPistas(numTecleado, numSecreto):
    if numTecleado == numSecreto:
        return 'Lo lograste !!!'

    pistas = []
    
    for i in range(len(numTecleado)):
        if numTecleado[i] == numSecreto[i]:
            pistas.append('Fermi')
        elif numTecleado[i] in numSecreto:
            pistas.append('Pico')
    if len(pistas) == 0:
        pistas.append('Bagels')
    else:
        pistas.sort()
    return ''.join(pistas)

intentos()
