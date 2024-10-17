# *TODO: 0 ( 4/4 )
# TODO ENDER: MOVED ON TO THE NEXT PROJECT AS ANYTHING AFTER THIS IS FOR THE NEXT DESIGN ITERATION
# TODO A1: HAVE A WAY TO CLEAR THE CONSOLE PARA MAS MALINIS TIGNAN
# TODO A2: ONLY SHOW THE LEGAL MOVES IF THE USER MAKES AN ILLEGAL MOVE
# TODO A3: AT THE START OF THE GAME PLAYERS LIFE IS ZERO SO DONT RUN DECREMENT


choices = ['rock', 'paper', 'scissors']

# TODO 14: HAVE SOME DEFAULT VALUES HERE PARA DI MO NA NEED MAG PASS NG 0 VALUES WHEN CREATING A NEW OBJECT
# TODO 15: ITS NOT A RIGHT-MINUS-WRONG SETUP NEED PA BA TALAGA YUNG MINUS_SCORE()
class Player:
    def __init__(self, life, score):
        self.life = 3
        self.score = 0
    # methods
    def get_life(self):
        return self.life
    
    def decrement_life(self):
        self.life -= 1
        
    def add_score(self):
        self.score += 1
    
    def minus_score(self):
        self.score += 1
    
    def get_score(self):
        return self.score

class Computer:
    def __init__(self, score):
        self.score = 0
    # methods
    def add_score(self):
        self.score += 1
    
    def minus_score(self):
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

# TODO 13: YOU INITIALIZED A USER AND PLAYER CLASS HERE, RETHINK IF MAY MAS BETTER NA APPROACH
new_player = Player(0,0)
new_computer = Computer(0)

def who_wins(user, computer):
    # TODO 16: HAVE A MUCH BETTER WAY TO OUTPUT THAN THIS
    print(f'Youre choice = {user} , Computer choice = {computer} \n')
    
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
        new_computer.add_score()
                
    print(f'Current score player : {new_player.get_score()} computer : {new_computer.get_score()}')

def main():
    
    while((new_player.get_score() != 3 ) and (new_computer.get_score() != 3) ):
        user = user_choice()
        computer = com_choice()

        who_wins(user, computer)


main()
