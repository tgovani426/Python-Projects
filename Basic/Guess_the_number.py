logo='''

 _____ _            _   _                 _                 _____                     _               _____                      
|_   _| |          | \ | |               | |               |  __ \                   (_)             |  __ \                     
  | | | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  \/_   _  ___  ___ ___ _ _ __   __ _  | |  \/ __ _ _ __ ___   ___ 
  | | | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | __| | | |/ _ \/ __/ __| | '_ \ / _` | | | __ / _` | '_ ` _ \ / _ \
  | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |    | |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | |_\ \ (_| | | | | | |  __/
  \_/ |_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|     \____/\__,_|\___||___/___/_|_| |_|\__, |  \____/\__,_|_| |_| |_|\___|
                                                                                               __/ |                             
                                                                                              |___/                              
'''
print(logo)
import random

EASY_LEVEL=10
HARD_LEVEL=5
def check_ans(user_number,com_number,turns):
    """checks answer against guess. Returns the  number of turns remaining """
    if com_number>user_number:
        print( "Too low")
        return turns-1
    elif com_number<user_number:
        print ("Too high")
        return turns-1
    elif com_number==user_number:
        print (f"\nYou got it! The answer was {com_number}.")

def set_dificulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level=='easy':
        return  EASY_LEVEL
    else:
        return  HARD_LEVEL

def game():
    print("Welcome to the number changing game!!!")
    print("I'm thinking of a number between 1 and 100")

    com_number=random.randint(1, 100)
    # print(com_number)
    
    turns = set_dificulty()
    user_number=0

    while user_number != com_number:
        print(f"You have {turns} attempts remaining to guess the number")
        
        user_number=int(input("Make a guess: "))

        turns=check_ans(user_number, com_number,turns)
        if turns==0:
            print(f"\nYou Loose!!!! The ans was {com_number}.")
            exit()
        elif user_number!=com_number:
            print("Guess Again!!!")
            

game()



 