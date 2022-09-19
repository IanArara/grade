###Poder selecionar quantas questões vão ser, qual a dificuldade, o assunto
###Buscar de uma planilha cada questão, que vai ser preenchida durante o internato
###Importar o randit para aleatorizar as questões pelos tipos de questões selecionadas


especialidade = input("Qual a área?\n")
nível = input("Qual a dificuldade?\n")
n_de_questões = int(input("Quantas questões você quer?\n"))


score = 0

comentário = "Esse é o comentário da questão" ###Substituir por um valor que vai ser retirado da planilha
resposta_certa = "a" ###Vai ser a conduta posta na planilha
resposta_errada = "b"
resposta_errada2 = "c"

def questão():
    global score
    resposta = input("Qual a resposta certa?\n a) asdfgfd \n b) efgrht \n c) fewgrehtr\n")
    if resposta == resposta_certa:
        print("Você acertou\n" + comentário)
        score += 1
    elif resposta == resposta_errada:
        print("Você errou, a resposta certa é a letra", resposta_certa)
    elif resposta == resposta_errada2:
        print("Você errou, a resposta certa é a letra", resposta_certa)
    else:
        print("Você não usou a, b ou c como resposta")

questão()
print(score)
#while n_de_questões != questões_rodadas:
#    print("Responda com a, b ou c")
#    questão()
