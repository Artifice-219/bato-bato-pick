# *TODO: ( 5/5 )
# TODO A1: HAVE A WAY TO CLEAR THE CONSOLE PARA MAS MALINIS TIGNAN
# TODO A2: ONLY SHOW THE LEGAL MOVES IF THE USER MAKES AN ILLEGAL MOVE
# TODO A3: AT THE START OF THE GAME PLAYERS LIFE IS ZERO SO DONT RUN DECREMENT
# TODO A4: CLEAR THE OUTPUT PARA HINDI MAGPATONG PATONG
# TODO 6 : MOVED ON AS ANYTHING AFTER THIS IS FOR THE NEXT DESIGN ITERATION


choices = ['rock', 'paper', 'scissors']

class Player:
    # TODO A4: IS THE PLAYER LIFE DECREMENTED ? PARANG DI NAMAN NAGAGAMIT
    def __init__(self, life = None, score = None):
        
        if life is None:
            life = 0
        self.life = life
        
        if score is None:
            score = 0
        self.score = score
        
    # methods
    def get_life(self):
        return self.life
    
    def decrement_life(self):
        self.life -= 1
        
    def add_score(self):
        self.score += 1
    
    def get_score(self):
        return self.score

class Computer:
    def __init__(self, score = None):
        
        if score is None:
            score = 0
        self.score = score

    # methods
    def add_score(self):
        self.score += 1
    
    def get_score(self):
        return self.score

    
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
            choice = str(input("Youre turn, make a choice : ")).lower()
            # check if user choice is allowed
            if(choice in choices):
                return choice
            else:{
                print(f'{choice}  is not allowed choose another')
            }

new_player = Player()
new_computer = Computer(0)

def who_wins(user, computer):
    print(f' You : {user} | VS | Computer : {computer} \n')
    
    if(user == computer):
        print("Its a tie")
    elif(user == 'rock' and computer == 'scissors'):
        print('You win')
        new_player.add_score()
        
    elif(user == 'paper' and computer == 'rock'):
        print('You win')
        new_player.add_score()
        
    elif(user == 'paper' and computer == 'scissors'):
        print('You lose')
        new_computer.add_score()
        
    elif(user == 'scissors' and computer == 'paper'):
        print('You win')
        new_player.add_score()
        
    else:
        # *possible dito ka na mag decrement
        print('You lose')
        new_computer.minus_score()
                
    print(f'Current score player : {new_player.get_score()} computer : {new_computer.get_score()}')

def main():
    # TODO A5: CHANGE THIS CONDITION HERE KASI NAKA SET YAN SA 3 IF FOR SOME REASONS NAG JUMP TO 4 YUNG SCORING DI NA MATE-TERMINATE ANG PROGRAM
    while((new_player.get_score() != 3 ) and (new_computer.get_score() != 3) ):
        user = user_choice()
        computer = com_choice()

        who_wins(user, computer)


main()
