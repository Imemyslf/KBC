import random
import os
from KBC_Data import Money_Prices


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

def poll(Options,Correct_Answer,i):
    os.system('cls')
    choice = []
    number = 0
    for i in range (4):
        number = random.randint(40,80)
        choice.append(number)
    space = " "
    
    # for i in range(len(Questions)):
    #         Question, Options, Correct_Answer, Description = Questions[i][random.randint(0, 4)].values()

    answer = Correct_Answer
    # Options.remove(answer)
    large = 0

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

    # print(f"{Question}\n")
    for i in range (len(choice)):
        cho = choice[i]
        opt = Options[i]
        opt1 = Options1[i]
        print(f"{space * (num + 1)}",end="")
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
            elif (i > 0 and i < (cho -1)):
                print(" ",end="")
        for i in range(cho):
            if (i == 9):    
                print(f"| {cho} %")
        # print("\n")
        print(f"{space * (num + 1)}",end="")
        for i in range(cho):
            if (i < (cho -1)):
                print("-",end="")
        print("\n")
        
        # Options.insert(0,answer)
        # print(Options)
        
    # Options.insert(0,answer)

        # Clears the terminal screen
        
        # Re-appearing the question with 50-50 life_life.
    # print(f'Aapka {i+1} Sawal Hai {Money_Prices[i]} Rupay Ke Liye:- \n')
    # print(Question)
    # for j in range(len(Options)):
    #     print(f'{j+1}) {Options[j]}')