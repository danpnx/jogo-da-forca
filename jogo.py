import os
import random
from time import sleep

print("- - - - - JOGO DA FORCA - - - - -")
playerName = input("Digite o seu nome: ")
playAgain = 'Y'

def welcome(playerName):
    print(f"Olá {playerName}. Seja bem-vindo(a) ao jogo da forca. Divirta-se!")

def gameRules():
    print("- - - - - COMO O JOGO FUNCIONA - - - - - ")
    print("1. Uma palavra é sorteada aleatoriamente..")
    print("2. O jogador deve dizer uma letra que pode estar -ou não- contida na palavra..")
    print("3. Vence caso acerte todas as letras que estão presentes na palavra..")
    print("3. Perde caso erre mais de seis vezes!")

def playTheGame():
    words = {
        "ampulheta": "Artefato usado para medição de tempo.",
        "borboleta": "Inseto que possui asas.",
        "embaixador": "Profissional que exerce função de diplomacia em relações exteriores.",
        "groselha": "Fruta vermelha rica em nutrientes. Bastante utilizada para a fabricação de xaropes, refrescos e geleias.",
        "pijama": "Tipo de roupa usado para dormir.",
        "quarentena": "Conjunto de medidas e restrições impostas a fim de satisfazer o isolamento"
    }
    randomList = random.choice( list (words.items()) )
    randomWord = list(randomList[0])
    randomTip = randomList[1]
    arrayRightChoices = ["_"] * len(randomWord)
    arrayWrongChoises = []
    countMistakes = 0

    while countMistakes <= 6:
        choosedLetter = input("Digite uma letra: ")
        letterCheck = '-1'

        for index in range(len(randomWord)):
            if choosedLetter == randomWord[index]:
                arrayRightChoices[index] = choosedLetter
                letterCheck = '1'
        
        if letterCheck == '1':
            print("Booooaaa! A letra está presente na palavra.")
            print(''.join(arrayRightChoices))
            print("____________________________________")
        else:
            print("Viiiish. Você errou a letra!")
            arrayWrongChoises.append(choosedLetter)
            print(f"Erros: {' | '.join(arrayWrongChoises)}")
            countMistakes += 1
            print("____________________________________")
            
        if arrayRightChoices == randomWord:
            print(f"PARABÉNS!!! Você conseguiu descobrir a palava: {''.join(arrayRightChoices)}")
            break
        
        if countMistakes == 5:
            print(f"DICA: {randomTip}")
        
        if countMistakes > 6:
            print(f"GG! A palavra era: {''.join(randomWord)}")

os.system('cls')
sleep(2)
welcome(playerName)
sleep(1)
gameRules()
print("----------------------------------------------- LOADING")
sleep(15)

while playAgain in 'Yy':
    os.system('cls')
    playTheGame()
    sleep(2)
    playAgain = input("Deseja jogar novamente? Y/N: ")
    while playAgain not in 'YyNn':
        playAgain = input("Resposta inválida. Por favor, digite novamente. Y/N: ")
    
    if playAgain in 'Nn':
        print("Até logo, noob!")