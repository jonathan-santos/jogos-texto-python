import random

vidaLeptude = 3
vidaJaque = 3
vezJaque = True

print("Bem vindo as aventuras matemáticas de Leptude o Mago de patinete")
print("Leptude por algum motivo entra em batalha com o sapo mago professor de matemática interdimensional Jaque, para vencer dele você precisa acertar suas perguntas de matemática ou então ele vai te matar de tédio")

while(vidaLeptude > 0 and vidaJaque > 0):
    if(vezJaque):
        perguntaJaque = str(random.randint(1, 25))+"+"+str(random.randint(1,25))
        resposta = input("Jaque te ataca com a pergunta: quanto é "+perguntaJaque+"? ")
        print("A resposta da pergunta era",eval(perguntaJaque))
        if int(resposta) == eval(perguntaJaque):
            print("Acertou mizerávi")
        else:
            vidaLeptude-=1
            print("Errou mizerávi, agora você está com",vidaLeptude,"pontos de vida")
    else:
        resposta = eval(input("Agora Leptude, ataque jaque com uma conta de matemática: "))
        
        respostaJaque = random.randint(resposta - 1, resposta + 1)

        print("A resposta de sua pergunta é",resposta,"e Jaque respondeu ",respostaJaque)
        if resposta == respostaJaque:
           print("Jaque acertou sua pergunta")
        else:
            vidaJaque-=1
            print("Jaque errou sua pergunta. Agora Jaque está com",vidaJaque,"pontos de vida")

    print("")
    vezJaque = not(vezJaque)

if(vidaJaque > 0):
    print("Você perdeu a batalha e agora Jaque começa a te ensinar matemática, até que você morre de tédio")
else:
    print("Jaque perdeu a batalha, então você começa a zuar ele, ele fica nervoso e volta a sua dimensão para ter reforço de matemática")

print("FIN")
