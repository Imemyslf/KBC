import time
import random
import Colors
from lifeline50 import ranopt
from KBC_Data import Questions, Money_Prices

# Initialize a variable to keep track of the player's earnings
money = 0
mokka_50 = 1
# Display a welcome message
print(f'\n\n{Colors.blue}WELCOME TO \'KON BANEGA CROREPATTI\'\n{Colors.reset}')

# Seed the random number generator with the current time to make shuffling random
random.seed(time.time())

# Loop through the questions
for i in range(len(Questions)):
    #Prompt the user to contiue playing.
    if (i == 5 or i == 10 or i == 15):
        print("\nKya app ghel jari rakhenge")
        choice = int(input(f"{Colors.yellow} 1.Jari rakhenge \n 2.Nahi \n{Colors.reset}"))
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

    # if (mokka_50 == 1):
    #     print("\n Do  you want to you the life-line?")
    #     life_line = int(input("1. 50-50\n Enter your Choice:-\t"))
    #     if ( life_line == 1 ):
    #         ranopt(Question,Options,Correct_Answer,i);
    #         mokka_50 = 0;
    # else:
    #     print("")

    # Prompt the user for their answer
    Answer = int(input('Enter your answer in (1-4) : '))
    time.sleep(3) # for Suspense

    # Check if the user's answer matches the correct answer
    if Correct_Answer in Options[Answer-1]:
        print(f'\n{Colors.green}Aap Jeeth Juke Hai {Money_Prices[i]} Rupay\n{Colors.reset}')
        money = Money_Prices[i]
    else:
        print(f'\n{Colors.red}Galat Jawaab Aapka khel Yahi Samapt Hota Hai!!\n{Colors.reset}')
        break

# Display the total earnings and a thank you message
print(f'\nAap apne saath {Colors.blue}{money}{Colors.reset} Rupay Lekar Ja Rahe Hai!!')
print(f'\n{Colors.pink}DHANYAWAAD HUMARA KHEL KHELNE KE LIYE{Colors.reset}')
print("\n\n")
