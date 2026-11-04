# Jogo de adivinhação completo. Para rodar: python jogo.py

import random

limite = 100
numero_secreto = random.randint(1, limite)
tentativas = 0
acertou = False

nome = input("Qual é o seu nome? ")
print("Bem-vindo ao jogo,", nome)
print("Estou pensando em um número de 1 a", limite)

while not acertou:
    palpite = int(input("Seu palpite: "))

    if palpite < 1 or palpite > limite:
        print("Palpite fora do intervalo! Esse não conta como tentativa.")
    else:
        tentativas = tentativas + 1

        if palpite == numero_secreto:
            print("Acertou em", tentativas, "tentativas!")
            acertou = True
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print("Muito baixo!")

print("Fim de jogo. Parabéns,", nome)
