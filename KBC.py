import time
import os
import random
import Colors
from lifeline import ranopt,poll,intro,mon
from KBC_Data import Questions, Money_Prices


money = 0
space = " "
mokka_50 = 1
mokka_poll = 1
counter_for_ll = 1

def ll(Questions_1=[],Options_1=[],Correct_Answer_1 = 0):
    print(Questions_1)
    # print(c_mokka_50,c_mokka_poll)
    # Initialize a variable leave to keep track of the player if they want to quit the game.
    global leave 
    leave = 1
    # Initialize a variable money to keep track of the player's earnings
    global money
    # Initialize a variable mokka_50 to keep track of the player's 50-50 life_line.
    global mokka_50,mokka_poll
    
    # mokka_50 = c_mokka_50
    # Initialize a variable to mokka_poll keep track of the player's Poll life_line.
    # mokka_poll = c_mokka_poll
    
    def lifeline():
        while(True):
            
            if (leave == 1): # if user haven't used the life_life
                print("\n Do  you want to use the life-line or You want to quit the game??")
                if (mokka_50 == 1 and mokka_poll == 1): # if user hasn't used the life
                    print(" 1. 50-50 \n 2. Poll")
                elif (mokka_50 == 0 and mokka_poll == 1): # if user hasn
                    print(f" {Colors.red}1. 50-50 {Colors.reset} \n 2. Poll")
                elif (mokka_poll == 0 and mokka_50 == 1):
                    print(f" 1. 50-50 \n {Colors.red}2. Poll{Colors.reset}")
                elif (mokka_poll == 0 and mokka_50 == 0):
                    print(f" {Colors.red}1. 50-50{Colors.reset} \n {Colors.red}2. Poll{Colors.reset}")
                
                li_li = int(input("\n Enter your Choice:-\t"))
            if li_li == 0 or li_li == 1 or li_li == 2:
                return li_li
            else:
                print("Sorry, you chose wrong options. Please try again")
                time.sleep(1)
                os.system('cls')
    life_line = lifeline()

    if ( life_line == 1 ):
        if ( mokka_50 == 1 ):
            Answer = ranopt(Question,Options,Correct_Answer,i)
            # Answer
            mokka_50 = 0  # user has used the life_line. 
            Answer.append(1)
            # Answer[2]  = 1
            # print(Answer)
            return Answer              
        else:
            print(f"\n {Colors.pink}Aap yeh life-line estmal kar juke hai!!{Colors.reset}")
            return False
            
    elif(life_line == 2):
        if (mokka_poll == 1):
            # print(Options)
            # print(Correct_Answer)
            poll_answer = poll(Question,Options,Correct_Answer,i)
            print(poll_answer)
            if(poll_answer[0] == 1):
                poll_answer.append(Options)
                poll_answer.append(2)
            else:
                poll_answer[0] = 0
                print(poll_answer)
                
                os.system('cls')
                mon(i)
                print(f'\nAapka {i+1} Sawal Tha {Money_Prices[i]} Rupay Ke Liye:- \n')
                print(Question)
                for j in range(len(Options)):
                    print(f'{j+1}) {Options[j]}')
                
                Correct_Answer_poll = int(input("Enter you Answer: "))
                poll_answer.append(Correct_Answer_poll)
                poll_answer.append(Options)
                poll_answer.append(2)
                
            mokka_poll = 0
            time.sleep(3)
            return poll_answer
        else:
            print("Aap yeh life-line estmal kar juke hai!!")
            return False
            
    elif (life_line == 0):
        if (i == 0):
            money = 0
            leave_game = [money,0]
            return leave_game
        else:
            money = Money_Prices[i-1]
            leave_game = [money,0]
            return leave_game
    else:
        return False 
        
    # if (life_line == 2 and mokka_poll == 1):
    #     if (poll_answer[0] == 0 and mokka_poll == 1):
    #         Answer = int(input('\n Enter your answer in (1-4) : '))
    #         print(f"\n Apka Jawab hai:- {Options[Answer - 1]}")
    #         mokka_poll = 0
    #         time.sleep(3) # for Suspense
    #     else:
    #         if (mokka_poll == 1):
    #             Answer =  poll_answer[1] + 1
    #             print(f"\n Apka Jawab hai:- {poll_answer[2]}")
    #             c_mokka_poll = 0
    #             time.sleep(3) # for Suspense
    # else:            

#Start of the game.... 
os.system('cls') # Clears the terminal screen 
# Display a welcome message
print(f'\n\n{Colors.blue}WELCOME TO \'KON BANEGA CROREPATTI\'\n{Colors.reset}')
intro()

# Seed the random number generator with the current time to make shuffling random
random.seed(time.time())

# Loop through the questions
for i in range(len(Questions)):
    
    #Prompt the user to contiue playing.
    if (i == 5 or i == 10 or i == 15):
        print("\nKya app ghel jari rakhenge")
        print(f"Dhanrashi apke pass hai {Money_Prices[i]}")
        print(f"{Colors.yellow} 1.Jari rakhenge \n 2.Nahi \n{Colors.reset}")
        choice = int(input("Enter Your Choice:-\t"))
        os.system('cls')
        if (choice == 2): # Game Over!!
                break
        
    # Randomly select a question, its options, correct answer, and description
    Question, Options, Correct_Answer, Description = Questions[i][random.randint(0, 4)].values()

    # Shuffle the answer options to present them in a random order
    random.shuffle(Options)

    mon(i)
    # Display the question and available options
    
    print(f'Aapka {i+1} Sawal Hai {Money_Prices[i]} Rupay Ke Liye:- \n')
    
    print(Question)
    
    for j in range(len(Options)):
        print(f'{j+1}) {Options[j]}')
    
    print("5) Life-line Or Leave the game!!")
    # Prompt the user for Life line Options.
            
    Answer = int(input('\n Enter your choice (1-5) : '))
    
    if (Answer == 5):
        
        if counter_for_ll == 1:
            Answer_life = ll(Question,Options,Correct_Answer)
            if Answer_life == False:
                counter_for_ll+=1
        
        if counter_for_ll > 1:
            os.system('cls')
            Answer_life = ll(Question,Options,Correct_Answer)
            
        
        if (Answer_life[len(Answer_life) - 1] == 1):
            if (len(Answer_life) == 2):
                Options = Answer_life [1]
                Answer = Answer_life [0]
            else:
                Answer = Answer_life[0]
                
        elif (Answer_life[len(Answer_life) - 1] == 2):
            if (len(Answer_life) == 5):
                Options = Answer_life[3]
                Answer = Answer_life[1] + 1
            else:
                Options = Answer_life[2]
                Answer = Answer_life[1]
        else :
                Answer = 0
                
        
    if (Answer == 0):        
        if (i == 0):
            money = 0
            break
        else:
            money = Money_Prices[i-1]
            break
    
            # break
    else:
    # Check if the user's answer matches the correct answer
        if Correct_Answer in Options[Answer-1]:
            print(f'\n {Colors.green}Aap Jeeth Juke Hai {Money_Prices[i]} Rupay\n{Colors.reset}')
            money = Money_Prices[i]
            time.sleep(3)# Timer to display that answer is correct.
            os.system('cls')# Clears the terminal screen
        
        else:
            
            print(f'\n{Colors.red}Galat Jawaab Aapka khel Yahi Samapt Hota Hai!!\n{Colors.reset}')
            
            if (i >= 0 and i < 5):
                money = 0
            elif (i > 5 and i < 10 ):
                money =  10000
            elif(i > 10 and i < 15):
                money =  320000
            else:
                money = Money_Prices[i]
            
            break

# Display the total earnings and a thank you message
print(f'\n Aap apne saath {Colors.blue}{money}{Colors.reset} Rupay Lekar Ja Rahe Hai!!')
print(f'\n {Colors.pink}DHANYAWAAD HUMARA KHEL KHELNE KE LIYE{Colors.reset}')
print("\n\n")