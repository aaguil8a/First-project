import random

POINTS = 0

def start():
    
    game = input("Do you want to play again y/n")

    print("This is highest", POINTS)
    
    if game.lower() == "y":
        start_game()
    
    else: 
        print("Good DAY!")
        
    
    
    
def start_game():
    
    global POINTS
    
    print("------------------------------------")
    print("Welcome to the guessing number game! ")
    print("------------------------------------")
    
    
    answer = random.randint(1, 10)
    guess = 0
    attempt = 0 
    
    
    while guess != answer:
        
        try: 
            guess = int(input("Guess a number between 1 and 10: "))
            
            if guess > 10 or guess < 1:
                print("Out of range{}".format(guess))
            
            
            elif guess > answer:
                print("It's lower")
            
            
            elif guess < answer:
                print("It's higher")
                
            attempt += 1
        
        
        except ValueError as err:
            print("You need to enter number {}".format(err))
    
    
    POINTS = attempt 
    
    
    print("You got it!")
    print("------------------------------------")
    print("Game over")
    print("------------------------------------")
    print("THIS attempt", attempt)
    start()

    
    

start_game()







  
