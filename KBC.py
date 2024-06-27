import time
import re
import os
import random
import Colors
from lifeline import ranopt, poll, intro, mon, swap, ques
from KBC_Data import Questions, Money_Prices

money = 0
space = " "
mokka_50 = 1
mokka_poll = 1
mokka_swap = 1

def ll(value=0):
    global leave
    leave = 1
    global money
    global mokka_50, mokka_poll, mokka_swap

    def lifeline():
        while True:
            if leave == 1:
                print("\nDo you want to use the life-line or you want to quit the game?")
                if mokka_50 == 1 and mokka_poll == 1 and mokka_swap == 1:
                    print("1. 50-50 \n2. Poll \n3. Swap")
                elif mokka_50 == 1 and mokka_poll == 1 and mokka_swap == 0:
                    print(f"1. 50-50 \n2. Poll \n{Colors.red}3. Swap {Colors.reset}")
                elif mokka_50 == 1 and mokka_poll == 0 and mokka_swap == 1:
                    print(f"1. 50-50 \n{Colors.red}2. Poll {Colors.reset}\n3. Swap")
                elif mokka_50 == 1 and mokka_poll == 0 and mokka_swap == 0:
                    print(f"1. 50-50 \n{Colors.red}2. Poll \n3. Swap{Colors.reset}")
                elif mokka_50 == 0 and mokka_poll == 1 and mokka_swap == 1:
                    print(f"{Colors.red}1. 50-50 {Colors.reset}\n2. Poll \n3. Swap")
                elif mokka_50 == 0 and mokka_poll == 1 and mokka_swap == 0:
                    print(f"{Colors.red}1. 50-50 {Colors.reset}\n2. Poll \n{Colors.red}3. Swap{Colors.reset}")
                elif mokka_50 == 0 and mokka_poll == 0 and mokka_swap == 1:
                    print(f"{Colors.red}1. 50-50 \n2. Poll {Colors.reset}\n3. Swap")
                elif mokka_50 == 0 and mokka_poll == 0 and mokka_swap == 0:
                    print(f"{Colors.red}1. 50-50 \n2. Poll \n3. Swap {Colors.reset}")

            li_li = input("\nEnter your choice: ")
            if re.match(r'^[0-3]$', li_li):
                return int(li_li)
            else:
                print("Sorry, you chose the wrong option. Please try again.")
                time.sleep(2)
                os.system('cls')

    life_line = lifeline()
    if life_line == 1:
        if mokka_50 == 1:
            Answer = ranopt(Question, Options, Correct_Answer, i)
            Answer.append(1)
            mokka_50 = 0
            return Answer
        else:
            print(f"\n{Colors.pink}Aap yeh life-line estmal kar juke hai!!{Colors.reset}")
            return False
    elif life_line == 2:
        if mokka_poll == 1:
            poll_answer = poll(Question, Options, Correct_Answer, i)
            if poll_answer[0] == 1:
                poll_answer.append(Options)
                poll_answer.append(2)
            else:
                poll_answer[0] = 0
                os.system('cls')
                mon(i)
                ques(Question, Options, i)
                Correct_Answer_poll = int(input("Enter your answer: "))
                poll_answer.append(Correct_Answer_poll)
                poll_answer.append(Options)
                poll_answer.append(2)
            mokka_poll = 0
            time.sleep(3)
            return poll_answer
        else:
            print(f"\n{Colors.pink}Aap yeh life-line estmal kar juke hai!!{Colors.reset}")
            return False
    elif life_line == 3:
        if mokka_swap == 1:
            Swap = swap(i, value)
            qu, op, ca, des = Swap
            os.system('cls')
            mon(i)
            ques(qu, op, i)
            answer = int(input("Enter your answer: "))
            Answer = []
            Answer.append(answer)
            Answer.append(op)
            Answer.append(ca)
            Answer.append(3)
            mokka_swap = 0
            time.sleep(3)
            return Answer
        else:
            print(f"\n{Colors.pink}Aap yeh life-line estmal kar juke hai!!{Colors.reset}")
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

# Start of the game....
os.system('cls')
print(f'\n\n{Colors.blue}WELCOME TO \'KON BANEGA CROREPATTI\'\n{Colors.reset}')
intro()
random.seed(time.time())

for i in range(len(Questions)):
    print("Main loop")
    if i == 5 or i == 10 or i == 15:
        print("\nKya aap khel jari rakhenge?")
        print(f"Dhanrashi apke pass hai {Money_Prices[i]}")
        print(f"{Colors.yellow}1. Jari rakhenge \n2. Nahi \n{Colors.reset}")
        choice = int(input("Enter your choice: "))
        os.system('cls')
        if choice == 2:
            break

    value = random.randint(0, 4)
    Question, Options, Correct_Answer, Description = Questions[i][value].values()
    random.shuffle(Options)
    mon(i)
    ques(Question, Options, i)

    if mokka_50 == 0 and mokka_poll == 0 and mokka_swap == 0:
        Answer = int(input('\nEnter your choice (1-4): '))
    else:
        print("5) Life-line or leave the game!")
        Answer = int(input('\nEnter your choice (1-5): '))

    if Answer == 5:
        Answer_life = ll(value)
        if Answer_life == False:
            continue

        if Answer_life[len(Answer_life) - 1] == 1:
            if len(Answer_life) == 2:
                Options = Answer_life[1]
                Answer = Answer_life[0]
            else:
                Answer = Answer_life[0]
        elif Answer_life[len(Answer_life) - 1] == 2:
            if len(Answer_life) == 5:
                Options = Answer_life[3]
                Answer = Answer_life[1] + 1
            else:
                Options = Answer_life[2]
                Answer = Answer_life[1]
        elif Answer_life[len(Answer_life) - 1] == 3:
            if len(Answer_life) == 4:
                Options = Answer_life[1]
                Answer = Answer_life[0]
                Correct_Answer = Answer_life[2]
        else:
            Answer = 0

    if Answer == 0:
        if i == 0:
            money = 0
            break
        else:
            money = Money_Prices[i - 1]
            break
    else:
        if Correct_Answer in Options[Answer - 1]:
            print(f'\n{Colors.green}Aap Jeet Chuke Hai {Money_Prices[i]} Rupay\n{Colors.reset}')
            money = Money_Prices[i]
            time.sleep(3)
            os.system('cls')
        else:
            print(f'\n{Colors.red}Galat Jawaab! Aapka khel yahi samapt hota hai!!\n{Colors.reset}')
            if i >= 0 and i < 5:
                money = 0
            elif i >= 5 and i < 10:
                money = 10000
            elif i >= 10 and i < 15:
                money = 320000
            else:
                money = Money_Prices[i]
            break

# Display the total earnings and a thank you message
print(f'\n Aap apne saath {Colors.blue}{money}{Colors.reset} Rupay Lekar Ja Rahe Hai!!')
print(f'\n {Colors.pink}DHANYAWAAD HUMARA KHEL KHELNE KE LIYE{Colors.reset}')
print("\n\n")