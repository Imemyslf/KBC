import time
import re
import os
import random
import Colors
from lifeline import ranopt,poll,intro,mon,swap,ques
from KBC_Data import Questions, Money_Prices


money = 0
space = " "
mokka_50 = 1
mokka_poll = 1
mokka_swap = 1
counter_for_ll = 1

def ll(value = 0):
    # print(Questions_1)
    
    # print(c_mokka_50,c_mokka_poll)
    # Initialize a variable leave to keep track of the player if they want to quit the game.
    global leave 
    leave = 1
    # Initialize a variable money to keep track of the player's earnings
    global money
    # Initialize a variable mokka_50 to keep track of the player's 50-50 life_line.
    global mokka_50,mokka_poll,mokka_swap
    print(mokka_50,mokka_poll,mokka_swap)
    
    def lifeline():
        # global mokka_50,mokka_poll,mokka_swap
        while(True):
            
            if (leave == 1): # if user haven't used the life_life
                print("\n Do  you want to use the life-line or You want to quit the game??")
                if (mokka_50 == 1 and mokka_poll == 1 and mokka_swap == 1):
                    print(" 1. 50-50 \n 2. Poll \n 3. Swap")
                
                elif (mokka_50 == 1 and mokka_poll == 1 and mokka_swap == 0): 
                    print(f" 1. 50-50 \n 2. Poll \n {Colors.red}3. Swap {Colors.reset} ")
                
                elif (mokka_50 == 1 and mokka_poll == 0 and mokka_swap == 1): 
                    print(f" 1. 50-50  \n {Colors.red}2. Poll \n {Colors.reset}3. Swap")
                
                elif (mokka_poll == 1 and mokka_50 == 0 and mokka_swap == 0): 
                    print(f" 1. 50-50 \n {Colors.reset} 2. Poll \n 3. Swap{Colors.reset}")
                
                elif (mokka_poll == 0 and mokka_50 == 1 and mokka_swap == 1):
                    print(f" {Colors.red}1. 50-50 {Colors.reset}\n 2. Poll \n 3. Swap")
                
                elif (mokka_poll == 0 and mokka_50 == 1 and mokka_swap == 0):
                    print(f"{Colors.red} 1. 50-50 {Colors.reset}\n 2. Poll \n {Colors.red}3. Swap{Colors.reset}")
                
                elif (mokka_poll == 0 and mokka_50 == 0 and mokka_swap == 1):
                    print(f"{Colors.red} 1. 50-50 \n 2. Poll {Colors.reset} \n 3. Swap")
                
                elif (mokka_poll == 0 and mokka_50 == 0 and mokka_swap == 0):
                    print(f" {Colors.red}1. 50-50 \n 2. Poll \n 3. Swap {Colors.reset}")
                
            
            li_li = input("\n Enter your Choice:-\t")
            # if li_li in [0,1,2,3]:
            if re.match(r'^[0-3]$',li_li):
                return int(li_li)
            else:
                print("Sorry, you chose wrong options. Please try again")
                time.sleep(2)
                os.system('cls')
    
    
    life_line = lifeline()
    if ( life_line == 1 ):
        if ( mokka_50 == 1 ):
            Answer = ranopt(Question,Options,Correct_Answer,i)
            # Answer
            # user has used the life_line. 
            Answer.append(1)
            # Answer[2]  = 1
            # print(Answer)
            mokka_50 = 0 
            return Answer              
        else:
            print(f"\n {Colors.pink}Aap yeh life-line estmal kar juke hai!!{Colors.reset}")
            return False
            
    elif(life_line == 2):
        if (mokka_poll == 1):
            # print(Options)
            # print(Correct_Answer)
            poll_answer = poll(Question,Options,Correct_Answer,i)
            if(poll_answer[0] == 1):
                poll_answer.append(Options)
                poll_answer.append(2)
            else:
                poll_answer[0] = 0
                
                os.system('cls')
                mon(i)
                ques(Question,Options,i)
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
    elif (life_line == 3):
        if(mokka_swap == 1):
            Swap = swap(i,value) 
            qu,op,ca,des = Swap
            
            os.system('cls')
            
            mon(i)
            ques(qu,op,i)
            answer = int(input("Enter you Answer: "))
            
            Answer = []
            Answer.append(answer)
            Answer.append(op)
            Answer.append(ca)
            Answer.append(3)
            
            mokka_swap = 0
            time.sleep(3)            
            return Answer
        else:
            print("Aap yeh life-line estmal kar juke hai!!")
            return False
            # print(f"Question:-{qu}\nOptions:- {op}\n Correct answers:- {ca}\n Description:- {des}")      
    
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
                   

#Start of the game.... 
os.system('cls') # Clears the terminal screen 
# Display a welcome message
print(f'\n\n{Colors.blue}WELCOME TO \'KON BANEGA CROREPATTI\'\n{Colors.reset}')
intro()

# Seed the random number generator with the current time to make shuffling random
random.seed(time.time())

# Loop through the questions
for i in range(len(Questions)):
    print("Main loop")
    #Prompt the user to contiue playing.
    if (i == 5 or i == 10 or i == 15):
        print("\nKya app ghel jari rakhenge")
        print(f"Dhanrashi apke pass hai {Money_Prices[i]}")
        print(f"{Colors.yellow} 1.Jari rakhenge \n 2.Nahi \n{Colors.reset}")
        choice = int(input("Enter Your Choice:-\t"))
        os.system('cls')
        if (choice == 2): # Game Over!!
                break
    
    value = random.randint(0, 4)
    # Randomly select a question, its options, correct answer, and description
    Question, Options, Correct_Answer, Description = Questions[i][value].values()

    # Shuffle the answer options to present them in a random order
    random.shuffle(Options)

    #Displaying the Current Point/Money values
    mon(i)
    # Display the question and available options
    ques(Question,Options,i)
    
    # Prompt the user for Life line Options.
    if mokka_50 == 0 and mokka_poll ==0 and mokka_swap == 0:
        Answer = int(input('\n Enter your choice (1-4) : '))
    else:
        print("5) Life-line Or Leave the game!!")
        Answer = int(input('\n Enter your choice (1-5) : '))
            
    
    if (Answer == 5):
        
        if counter_for_ll == 1:
            Answer_life = ll(value)
            if Answer_life == False:
                counter_for_ll+=1
        
        while(counter_for_ll > 1):
            os.system('cls')
            Answer_life = ll(value)
            if Answer_life != False:
                break
            
        
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
        elif (Answer_life[len(Answer_life) - 1] == 3):
            if (len(Answer_life) == 4):
                Options = Answer_life[1]
                Answer = Answer_life[0]
                Correct_Answer = Answer_life[2]
        else :
                Answer = 0
                
        
    if (Answer == 0):        
        if (i == 0):
            money = 0
            break
        else:
            money = Money_Prices[i-1]
            break
    
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