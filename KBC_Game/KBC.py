import time
import re
import os
import random
import Colors
from Function import intro, mon, question, get_user_input_with_timeout, user_data, play
from lifeline import ran_50_50, poll, swap 
from KBC_Data import Questions, Money_Prices

money = 0
mokka_50 = 1
mokka_poll = 1
mokka_swap = 1
counter_for_ll = 1
timeout_duration = 40

# Lifeline options
def life_line(Question, Options, Correct_Answer, Description, i, value=0):
    global leave, money, mokka_50, mokka_poll, mokka_swap
    leave = 1
    global money
    # Initialize a variable mokka_50 to keep track of the player's 50-50 life_line.
    global mokka_50, mokka_poll, mokka_swap
    def lifeline_selection():
        lifelines = {
            "1. 50-50": mokka_50,
            "2. Poll": mokka_poll,
            "3. Swap": mokka_swap
        }
        
        while leave == 1:  # if user hasn't used the lifeline
            print("\nDo you want to use a lifeline or quit the game?")
            for lifeline, available in lifelines.items():
                if available:
                    print(lifeline)
                else:
                    print(f"{Colors.red}{lifeline}{Colors.reset}")
                    
            lifeline_selected = input("\nEnter your choice: ")
            if re.match(r'^[0-3]$', lifeline_selected):
                return int(lifeline_selected)
            else:
                print("Sorry, you chose the wrong option. Please try again.")
                time.sleep(2)
                os.system('cls')

    
    life_line = lifeline_selection()
    if life_line == 1:
        if mokka_50 == 1:
            Answer = ran_50_50(Question, Options, Correct_Answer, i)
            # Which line user had selected. 
            if Answer[0] != None:
                Answer.append(1)
            # User has used the lifeline
            mokka_50 = 0
            return Answer
        else:
            input(f"\n{Colors.pink}You have already used this lifeline!!{Colors.reset}\nPress enter to continue")
            return False
    
    elif life_line == 2:
        if mokka_poll == 1:
            poll_answer = poll(Question, Options, Correct_Answer, i)
            if poll_answer[0] == 1:
                poll_answer.extend([Options,2])
            else:
                poll_answer[0] = 0
                os.system('cls')
                mon(i)
                question(Question, Options, i)
                timeout_duration = 15
                print(f"You have {timeout_duration} seconds to provide input.")
                Check = get_user_input_with_timeout(timeout_duration)
                Correct_Answer_poll = Check if Check else None
                
                if Correct_Answer_poll != None:
                    poll_answer.extend([Correct_Answer_poll, Options, 2])
                    
            mokka_poll = 0
            time.sleep(3)
            return poll_answer
        else:
            input(f"\n{Colors.pink}You have already used this lifeline!!{Colors.reset}\nPress enter to continue")
            return False
    
    elif life_line == 3:
        if mokka_swap == 1:
            Swap = swap(i, value)
            qu, op, ca, des = Swap
            os.system('cls')
            mon(i)
            question(qu, op, i)
            timeout_duration = 15
            print(f"\n\nYou have {timeout_duration} seconds to provide input.")
            Check = get_user_input_with_timeout(timeout_duration)
            answer = Check if Check else None
            if answer != None:
                Answer = [answer,op,ca,des,3]
            mokka_swap = 0
            time.sleep(3)
            return Answer
        else:
            input(f"\n{Colors.pink}You have already used this lifeline!!{Colors.reset}\nPress enter to continue")
            return False     

    elif life_line == 0:
        if i == 0:
            money = 0
            leave_game = [money, 0]
            return leave_game
        else:
            money = Money_Prices[i - 1]
            leave_game = [money, 0]
            return leave_game
    else:
        return False


# Game logic
def game(user_name):
    global money, mokka_50, mokka_poll, mokka_swap, timeout_duration, counter_for_ll
    os.system('cls')  # Clears the terminal screen
    intro()
    start_time = time.time()
    random.seed(time.time())

    for i in range(len(Questions)):
        # Prompt the user to continue playing.
        if i == 5 or i == 10 or i == 15:
            print("\nDo you want to continue playing?")
            print(f"\nYou currently have {Colors.green}{Money_Prices[i - 1]}{Colors.reset}")
            print(f"{Colors.yellow}1. Continue \n2. No \n{Colors.reset}")
            choice = int(input("Enter your choice: "))
            os.system('cls')
            if choice == 2: # Game Over!!
                break
            else:
                timeout_duration = timeout_duration - 10 if i != 15 else  200
                input(f"\n{Colors.green}You will have {Colors.yellow}{timeout_duration}{Colors.reset} {Colors.green}seconds to answer your question.{Colors.reset}\n\nPress enter to continue")
                os.system("cls")
                
        value = random.randint(0, 4)
        Question, Options, Correct_Answer, Description = Questions[i][value].values()
        # Shuffle the answer options to present them in a random order
        random.shuffle(Options)
        mon(i)
        # Display the question and available options
        question(Question, Options, i) 
        
        if mokka_50 == 0 and mokka_poll == 0 and mokka_swap == 0:
            print(f"\nYou have {timeout_duration} seconds to provide input.")
        else:
            print("5) Use Lifeline Or Leave the game!!")
            print(f"\nYou have {timeout_duration} seconds to provide input.")

        Check = get_user_input_with_timeout(timeout_duration)
        Answer = Check if Check else 0

        if Answer == 5:
            if counter_for_ll == 1:
                Answer_life = life_line(Question,Options,Correct_Answer,Description,i,value)
                if Answer_life == False:
                    counter_for_ll += 1

            while counter_for_ll > 1:
                os.system('cls')
                Answer_life = life_line(Question,Options,Correct_Answer,Description,i,value)
                if Answer_life != False:
                    break
                
            if Answer_life[len(Answer_life) - 1] == 1:
                Answer = Answer_life[1]
                if len(Answer_life) == 4:
                        Options = Answer_life[2]
            
            elif Answer_life[len(Answer_life) - 1] == 2:            
                Options = Answer_life[3] if len(Answer_life) == 5 else Answer_life[2]
                Answer = Answer_life[1] + 1 if len(Answer_life) == 5 else Answer_life[1]
            
            elif Answer_life[len(Answer_life) - 1] == 3:            
                if len(Answer_life) == 5:
                    Options,Answer,Correct_Answer,Description = Answer_life[1],Answer_life[0],Answer_life[2],Answer_life[3]
            
            else:
                Answer = 0

        if Answer == 0:
            money = 0 if i == 0 else Money_Prices[i - 1]
            break
        else:
            if Correct_Answer in Options[Answer - 1]:
                time.sleep(3)
                print(f'\n{Colors.green}Congratulations! You have won {Money_Prices[i]} Rupees\n{Colors.reset}')
                input(f"\nDescription:- {Colors.cyan}{Description}{Colors.reset}\nPress any key to continue")
                money = Money_Prices[i]
                os.system('cls')
            else:
                print(f'\nSorry!! {Colors.red}Wrong Answer! Your game ends here!!\n{Colors.reset}')
                print(f"\nCorrect Answer:- {Correct_Answer}")
                if 0 <= i < 5:
                    money = 0
                elif 5 <= i < 10:
                    money = 10000
                elif 10 <= i < 15:
                    money = 320000
                else:
                    money = Money_Prices[i]
                break

    # Display the total earnings and a thank you message
    print(f'\n You are taking {Colors.blue}{money}{Colors.reset} Rupees with you!!')

    end_time = time.time()
    total_time = end_time - start_time

    user_data(user_name, money, total_time)

    print(f'\n {Colors.blue}Thank You {user_name} for playing our game{Colors.reset}')
    time.sleep(6)
    os.system('exit')

# Start of the game....
def start_game():
    os.system('cls')
    player_choice = play()

    if player_choice == 1:
        os.system('cls')
        while True:
            user_name = input("\nEnter your username:- ").strip()
            if user_name:
                
                break
            else:
                input("Please enter a valid username\n Press enter to continue")
                os.system('cls')
        
        os.system('cls')
        game(user_name)
    else:
        print(f"\n{Colors.pink}Thank you!! See you again later{Colors.reset}")
        time.sleep(2)
        os.system('exit')
    pass
if __name__ == '__main__':
    start_game()