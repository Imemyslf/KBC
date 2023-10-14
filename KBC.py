import time
import os
import random
import Colors
from lifeline50 import ranopt
from KBC_Data import Questions, Money_Prices

# Initialize a variable to keep track of the player's earnings
money = 0
# Initialize a variable to keep track of the player's 50-50 life_line.
mokka_50 = 1
leave = 1

os.system('cls') # Clears the terminal screen
# Display a welcome message
print(f'\n\n{Colors.blue}WELCOME TO \'KON BANEGA CROREPATTI\'\n{Colors.reset}')

# Seed the random number generator with the current time to make shuffling random
random.seed(time.time())

# Loop through the questions
for i in range(len(Questions)):
    
    #Prompt the user to contiue playing.
    if (i == 5 or i == 10 or i == 15):
        print("\nKya app ghel jari rakhenge")
        print(f"{Colors.yellow} 1.Jari rakhenge \n 2.Nahi \n{Colors.reset}")
        choice = int(input("Enter Your Choice:-\t"))
        os.system('cls')
        if (choice == 2): # Game Over!!
                break
        
    # Randomly select a question, its options, correct answer, and description
    Question, Options, Correct_Answer, Description = Questions[i][random.randint(0, 4)].values()

    # Shuffle the answer options to present them in a random order
    random.shuffle(Options)

    
    # Display the question and available options
    print(f'Aapka {i+1} Sawal Hai {Money_Prices[i]} Rupay Ke Liye:- \n')
    print(Question)
    for j in range(len(Options)):
        print(f'{j+1}) {Options[j]}')

    # Prompt the user for Life line Options.
    if (mokka_50 == 1 or leave == 1): # if user haven't used the life_life
        print("\n Do  you want to use the life-line or You want to quit the game??")
        life_line = int(input(" 1. 50-50 \n 2. No, I am fine.\n 0. Quit.\n Enter your Choice:-\t"))
        if ( life_line == 1 ):
            ranopt(Question,Options,Correct_Answer,i);
            mokka_50 = 0; # user has used the life_line.
        elif (life_line == 0):
            if (i == 0):
                money = 0
            else:
                money = Money_Prices[i-1]
            break
    else:
        print('')
        

    # Prompt the user for their answer
    Answer = int(input(' Enter your answer in (1-4) : '))
    time.sleep(3) # for Suspense

    # Check if the user's answer matches the correct answer
    if Correct_Answer in Options[Answer-1]:
        print(f'\n{Colors.green}Aap Jeeth Juke Hai {Money_Prices[i]} Rupay\n{Colors.reset}')
        money = Money_Prices[i]
        time.sleep(3)# Timer to display that answer is correct.
        os.system('cls')# Clears the terminal screen
    else:
        print(f'\n{Colors.red}Galat Jawaab Aapka khel Yahi Samapt Hota Hai!!\n{Colors.reset}')
        break

# Display the total earnings and a thank you message
print(f'\nAap apne saath {Colors.blue}{money}{Colors.reset} Rupay Lekar Ja Rahe Hai!!')
print(f'\n{Colors.pink}DHANYAWAAD HUMARA KHEL KHELNE KE LIYE{Colors.reset}')
print("\n\n")