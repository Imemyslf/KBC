import random
import Colors
import os
from KBC_Data import Questions,Money_Prices

def intro():
    print(f"\n{Colors.cyan} Rules:-{Colors.reset}")
    print(f"\n 1. There are total{Colors.blue} 15 {Colors.reset} question in Kon Banega Crorepati")
    print(f"\n 2. Money price(aka Points) are from {Colors.green}1000 - 7cr{Colors.reset}")
    print("\n 3. You will have Life Line\n a. 50-50\n b. Poll")
    print(f"\n 4. You can leave the game whenever you want{Colors.red} *Just Press 0 when the option pop's up to you!! *{Colors.reset}")
    response = input(" Press enter to continue\t")
    
    os.system('cls')

#Randome Options Functions for deleting any two randome options but keeping the Correct_Answer in it.
def ranopt(Question,Options,Correct_Answer,i):
    #Passing the Correct_Answer into the variable answer
    answer = Correct_Answer

    #Removing the Correct_Answer from the Options list.
    Options.remove(answer)

    #Selecting any two random options from the new Options list.
    indices_to_delete = random.sample(range(len(Options)), 2)

        # Deleting the two randome options that were choosen from the above list
    for index in range(len(indices_to_delete)):
        del Options[index]

    #Adding the answer Back into the Options List.
    Options.insert(0,answer)

    os.system('cls') # Clears the terminal screen
    
    # Re-appearing the question with 50-50 life_life.
    print(f'Aapka {i+1} Sawal Hai {Money_Prices[i]} Rupay Ke Liye:- \n')
    print(Question)
    for j in range(len(Options)):
        print(f'{j+1}) {Options[j]}')

# 
def poll(Options,Correct_Answer):
    os.system('cls')
    choice = []
    space = " "
    large = 0

    # for i in range(len(Questions)):
    #     Question, Options, Correct_Answer, Description = Questions[i][random.randint(0, 4)].values()

    answer = Correct_Answer
    choice_1_answer = random.randint(35,37)
    
    choice_0 = random.randint(35,38)
    
    Options.remove(answer)
    
    random_option = random.sample(range(len(Options)), 1)
    i_rand = random_option[0]
    
    for i in range(len(Questions)):
        if (i_rand == i):
            i_rand_remove = Options[i]
            
    Options.remove(i_rand_remove)
    Options.insert(0,i_rand_remove)
    Options.insert(1,answer)
    
    choice.insert(0,choice_0)
    choice.insert(1,choice_1_answer)
    nos = choice[0]  + choice[1]
    # print(f"Choice 0,1:- {nos}")
    
    total = 100 - (choice[0] + choice[1])
    
    choice_3 = random.randint(10,15)
    choice.insert(2,choice_3)
    
    final_value = 100 - (choice_1_answer + choice_0 + choice_3)
    choice.insert(3,final_value)
    
    for i in range(len(Options)):
        op = Options[i]
        op_name = len(op)
        if (op_name > large):
            large = op_name
            large_name = Options[i]

    num = large
    name = large_name
    Options1 = []
    for i in range(len(Options)):
        opt = Options[i]
        n1 = (num - len(opt))
        Options1.append(n1)

    for i in range (len(choice)):
        cho = choice[i]
        opt = Options[i]
        opt1 = Options1[i]
        
        print(f" {space * (num + 1)}",end="")
        for i in range (cho):
            if (i < (cho -1)):
                print("-",end="")
            else:
                print("")
        str1 = opt + (space * opt1) 
        print(f"{str1} ",end="")
        
        for i in range(cho):
            if (i == 0 ):
                print("|",end="")
            elif (i >= 0 and i < (cho -1)):
                print(" ",end="")
        
        for i in range(cho):
            if (i == 9):    
                print(f" | {cho} %")

        print(f" {space * (num + 1)}",end="")
        for i in range(cho):
            if (i < (cho -1)):
                print("-",end="")
        print("\n")

if __name__ == "__main__":
    intro()
    ranopt()
    poll()