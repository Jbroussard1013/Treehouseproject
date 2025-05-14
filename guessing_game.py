import random
attempts = []
num = random.randint(1,10)

def start_game():
    try: 
        print("Welcome to the Number Guessing game.")
        tries = int(input("Please pick a number from 1-10. "))
        attempts.append(tries)

    except ValueError :
        print("Sorry, but that is an invalid number.Please try again. ")
        start_game()

    else:    
        while tries != num:
            if tries > 10:
                tries = int(input("The number you chose is to big.Try again. "))
                attempts.append(tries)
            elif tries < 1:
                tries = int(input("The number you chose is to small.Try again "))
                attempts.append(tries)
            elif tries > num:
                tries = int(input("The number is lower.Please try again. "))
                attempts.append(tries)
            elif tries < num: 
                tries = int(input("The number is higher.Please try again. "))
                attempts.append(tries)
         
        
        print("Congrats,you have chosen the the correct number! ")
        print("You have completed this game in {} attempts.".format(len(attempts)))
        print("Game Over.Thanks for playing!")



start_game()









