import random
import os
from KBC_Data import Questions,Money_Prices

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

    os.system('cls') # Cleaing the terminal screen
    
    # Re-appearing the question with 50-50 life_life.
    print(f'Aapka {i+1} Sawal Hai {Money_Prices[i]} Rupay Ke Liye:- \n')
    print(Question)
    for j in range(len(Options)):
        print(f'{j+1}) {Options[j]}')

