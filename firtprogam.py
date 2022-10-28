import random
lista = []
chance = 5
digitadas = []


print('Escreve uma palavra por vez')
while True:

    palavras = input('Digite as palavras : ')
    if not palavras.isalpha():
        print('Digite apenas palavras')
        continue

    if len(palavras) > 28:
        print('Digite uma palavra que exista:')
        continue

    lista.append(palavras)
    secreta = random.choice(lista)

    if len(lista) >= 4:
         print('Vamos para o jogo !!!')
         break

while True:
    letra = input('Digite uma letra : ')
    if chance <= 0:
        print('Você perdeu!!!!!')
        break
    if len(letra) > 1:
        print('Digite apenas uma letra por vez')
        continue
    digitadas.append(letra)

    if letra in secreta:
        print(f'Acertou uma letra, "{letra}" existe na palavra')
    else:
        print(f'A letra {letra} não esta na palavra.')
        digitadas.pop()

    secreta_temp = ''
    for letra_sec in secreta:
        if letra_sec in digitadas:
            secreta_temp += letra_sec
        else:
            secreta_temp += '*'
    print(secreta_temp)
    if secreta_temp == secreta:
        print('Acertouuuu!!!!!!!')
        break
    if letra not in secreta:
            chance -= 1
            print(f'Voce tem agora agora  {chance} chances')














