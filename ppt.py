# fazer uma lista com pedra, papel e tesoura
import random


it = {
    1:"pedra",
    2:"papel", 
    3:"tesoura"
}

def selectFromNumber(i):
    randomlyChosen = it[i]
    recebido = input("\npedra, papel ou tesoura?\n\n--> ")
    print ("--> ",randomlyChosen)
    if (randomlyChosen == recebido):
        print("é igual...")
    elif (  (randomlyChosen == "pedra" and recebido == "tesoura") or 
            (randomlyChosen == "tesoura" and recebido == "papel") or 
            (randomlyChosen == "papel"   and recebido =="pedra")):
        print("ganhaste!!!")
    else: 
        print("perdeste desta vez...")




def main():
    print("Bem vindo ao jogo do pedra papel ou tesoura")
    input("vamos jogar?\n")
    selectFromNumber(random.randint(1,3))
    aux = True
    while aux:
        if (input("jogamos outra vez?\n-> ") == "sim"):
            selectFromNumber(random.randint(1,3))
        else:
            aux = False
    print("bye")

main()
