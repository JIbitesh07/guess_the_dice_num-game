print("Hello,user")
print("Welcome to the Guess the Dice Num game")
print("The rules of the game are:")
print("U have to enter a number between 1 to 6")
print("Then a dice will be rolled by the computer")
print("If your guess matches to that of the computer, you will get a point ")
print("Or else the computer will get a point")

computer_points=0
player_points=0



def game():
    dice="1"
    while dice!=0:
        dice=int(input("enter a number between 1 to 6:"))
        from random import randint
        x=randint(1,6)
        computer=x
        
        global player_points
        global computer_points
        if dice>=0 and dice<=6:
            if dice==0:
                print("Final computer points:",computer_points)
                print("Final player points:",player_points)
                if computer_points>player_points:
                    print("Computer Wins!!")
                elif player_points>computer_points:
                    print("Player Wins!!")
                elif player_points==computer_points:
                    print("Its a tie")
                print("bye")
            elif dice==computer:
                print("computer's choice",computer) 
                print("You win and computer lost")
                player_points=player_points+1
                
                print("Player_points:",player_points)
                print("Computer_points:",computer_points)
            elif dice!=computer and dice!=0:
                print("computer's choice",computer)
                print("You lost and computer won")
                computer_points=computer_points+1
                
                print("Player_points:",player_points)
                print("Computer_points:",computer_points)
            
                
        else:
            print("enter a number between 1 and 6")
game()                        
