print("**********")
print("bem vindo ao jogo de adivinhaçao")
print("**********")

numero_secreto = 77
total_de_tentativas = 3
rodada=1
while (rodada <= total_de_tentativas):
    print("tentativas {}".format(rodada,total_de_tentativas))

chute_str = input("digite o seu numero:")
print ("voce digitou:", chute_str) 
chute = int (chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute <numero_secreto

if (acertou):
    print("Parabéns! voce acertou!")
else:
    if(maior):
        print("o seu chute foi maior do que o numero secreto!")
    elif(menor)
       print("o seu chute foi menor do que o numero secreto!")

    rodada = rodada + 1
print("fim de jogo")