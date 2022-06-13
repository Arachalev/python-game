import random
#ROCK PAPER SCISSORS GAME




#Array of possible answers to the game 
answers = ['r','p','s']



def computerChoice():
    compChoice = random.choice(answers)
    return compChoice

def userInput():
    print("Enter a value for the game. R or P or S \n")
    while True:
        userChoice = input("Enter your choice: ")
        isNumber = containsNumber(userChoice)
        if(isNumber):
            print("Enter a valid input[not a number] ...(e.g R,P or S ")
            continue
        elif(len(userChoice)>1):
            print("Enter only one character...(e.g R,P, or S")
            continue
        elif(userChoice.lower() not in answers): 
            print("Invalid answer, please choose between 'R', 'P' or 'S'") 
            continue          
        else:
            break
    return userChoice.lower()   
    

def containsNumber(value):
    if True in [char.isdigit() for char in value]:
        return True
    return False

def intro():
    print("welcome to the ROCK, PAPER, SCISSORS GAME.... \n")
    print("'R' = ROCK \n 'P' = PAPER \n 'S' = SCISSORS \n")

def restart():
    print("Restart game : 'Y' \n End game : 'Q'")
    while True:
        answer = input("Enter your choice: ")
        isNumber = containsNumber(answer)
        if(isNumber):
            print("Enter a valid input ...(e.g Y or Q")
            continue
        elif(len(answer)>1):
            print("Enter only one character...(e.g Y or Q")
            continue
        else:
            break
    return answer.lower()
    
def results (comp, player):
    if (player == 'r'):
        player = "Rock"
    elif (player == 'p'):
        player = "Paper"
    elif (player == 's'):
        player = "Scissors"
    if (comp == 'r'):
        comp = "Rock"
    elif (comp == 'p'):
        comp = "Paper"
    elif (comp == 's'):
        comp = "Scissors"
    return comp, player

def gameResult():
    while True:
        comp = computerChoice()
        player = userInput()
        fullComp, fullPlayer =  results(comp,player)

        # print("Computer:{} \n Player:{}".format(comp,player))
        print(f"Computer: {fullComp} \n Player: {fullPlayer} \n")

        if(comp == player):
            print("The game is a draw, restarting")
            continue
        elif (player == 'r'):
            if(comp == 'p'):
                print("Paper cover rocks \n Computer wins!!")
            else:
                print("Rock smashes scissors \n Player wins!!")
        elif (player == 'p'):
            if(comp == 'r'):
                print("Paper covers rock \n Player wins!!")
            else:
                print("Scissors cut through paper \n Computer wins!!")
        elif (player == 's'):
            if(comp == 'r'):
                print("Rock smashes scissors \n Computer wins!!")
            else:
                print("Scissors cut through paper \n Player wins!!")
        
        restartGame = restart()
        if(restartGame == 'y'):
            continue
        else:
            break

def game():
    gameResult()

game()
         


     

    






