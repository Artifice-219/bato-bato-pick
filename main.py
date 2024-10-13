# *TODO: 0 ( 2/2 )
# TODO 7 : TRACK THE NUMBER OF WINS, might also need a computer class for this  WHOEVER GOT 3 CORRECT WINS WOULD BE WINNER AND THE GAME ENDS
# TODO 9 : REMEMBER HAVE A MAIN FUNCTION THAT WILL SERVE AS THE CODE DRIVER


choices = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self, life):
        self.life = 3
    # methods
    def get_life(self):
        return self.life
    
    def decrement_life(self):
        self.life -= 1
    
    
    
def random_num():
    import random
    return random.randint(0,2)

def com_choice():
    index = random_num()
    return choices[index]

def user_choice():
    #* prints all choices here
    print('Allowed moves :')
    print(*choices, sep = " ," )
    
    while True:
            # TODO 11: NORMALIZE THE INPUT HERE
            choice = str(input("Youre turn, make a choice : "))
            # check if user choice is allowed
            if(choice in choices):
                return choice
                #TODO 8 : CHECK IF THE BREAK STATEMENT HERE IS UNREACHABLE
                #TODO 9 : HAVE A USER PROMPT NA MALING INPUT SYA
                break


def who_wins(user, computer):
    
    # TODO 10 : FIND A WAY TO BETTER CODE THIS SHIT
    print(f'Youre choice = {user} , Computer choice = {computer} \n')
    
    if(user == computer):
        print("Its a tie")
    elif(user == 'rock' and computer == 'scissors'):
        print('You win')
    elif(user == 'paper' and computer == 'rock'):
        print('You win')
    elif(user == 'paper' and computer == 'scissors'):
        print('You lose')
    elif(user == 'scissors' and computer == 'paper'):
        print('You win')
    else:
        # *possible dito ka na mag decrement
        # TODO 12: DECREMENT USER LIFE EACH TIME THIS CODE RUNS IT MEANS TALO KASI
        print('You lose')

user = user_choice()
computer = com_choice()

who_wins(user, computer)

