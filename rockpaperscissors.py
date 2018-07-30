import re

print('Welcome to Rock-Paper-Scissors')

games = eval(input('How many games of Rock-Paper-Scissors do you want to play? ')) 
# Because this game program involves the participation of another user
# I chose to assign an eval input statement to a variable so that I can call the game variable
# in my code when displaying the current iteration of the game number, the number of games won,
# and iterating through the number of games the user decides untile the total number of games has been played.
while games % 2 == 0:
        games = eval(input('Please enter an odd number of games: '))

        #I used the while loop here to ensure that my program knew that as long as the number the end-user inputed is an even number
        #(games variable) they cannot continue to the rest of the game. The end user will be repeatedly asked to "Please enter an odd number of games"
        # until they choose an odd number of games. Furhtermore, I used the modulo operator in the while loop to add further restrictions on what the
        # end-user can input to continue to the next phase of the game. I set the while loop to continously ask the end-user to "Please enter an odd
        # number of games" as long as the number they input is divisible by two with a remainder of 0, indicating that the user inputted an even number
        # ( games % 2 == 0 ). 

     
for i in range(1, games+1): # I used a for loop here to let my program know what to print as long as the end-user chooses a specific letter. Furthermore,
                            # I used the for loop start/end paramter, exemplified by the use of "in range(1, games+1)" to specify what number I want the loop
                            # to start at and by how many increments I want the game number to increase by before it ends at the number of games the end-user
                            # chose at the beginning of the game. The below print fields exemplifies what the program will repeatedly print until the loop
                            # is complete. 
    print('Game', i) # The program will print "Game i(the number that the game starts with and ends with - for exmaple, if the user choses 3 games, it will start
                     # with Game 1 and end with Game 3. 
    print('You can pick')
    print('R - Rock')
    print('P - Paper')
    print('S - Scissors')
    option = input('Please enter your choice: ').upper() # I created another variable called "option" to exemplify what the user chooses so I will be able to
                                                                 # use it in the rest of the loop to help the program determine what will be printed as long as the
                                                                 # loop is running and until the loop is completed as seen below. I used the strip and upper functions
                                                                 # that the computer acknowledges a lowercase or uppercase r, p, and s.
    if option == 'R':
        print('The computer picked Paper. You lose.')
    elif option == 'P':
        print('The computer picked Scissors. You lose.')
    else: 
        print('The computer picked Rock. You lose.')
print('You won 0 games.') # Because the rules stated that the user will never win, I hard coded this print statement to print that the user won no games. 
print('Computer won', games, 'games.') # Because the computer will always win, I wrote a print statement to indicate how many games the computer won which will
                                       # always be the amount of games the user inputted they wanted to play in the game variable.  
print('Computer wins!') # Because the computer will always win, I hard coded this print statement to print that the computer won. 
      

    
    
    

    
    
          
          
             
   
             
