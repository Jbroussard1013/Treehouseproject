import random
attempts = []
num = random.randint(1,10)

def start_game():
    print("Welcome to the Number Guessing game")
    tries = int(input("Please pick a number from 1-10. "))
    attempts.append(tries)
    while tries != num:
        if tries > 10:
            tries = int(input("The number you chose is to big.Please select a number between 1-10. "))
            attempts.append(tries)
        elif tries < 1:
            tries = int(input("The number you chose is to small.Please select a number between 1-10."))
            attempts.append(tries)
        elif tries > num:
            print("Sorry,but that is incorret,the number is lower.")
            tries = int(input("Please try again. "))
            attempts.append(tries)
        elif tries < num:
            print ("Sorry, but that is incorrect, the number is higher. ") 
            tries = int(input("Please try again. "))
            attempts.append(tries)

        

    print("Congrats, you have chosen the the correct number! ")
    print("You have completed this game in {} attempts.".format(len(attempts)))
    print("Game Over")


start_game()









