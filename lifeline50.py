import random
from KBC_Data import Questions,Money_Prices

def ranopt(Question,Options,Correct_Answer,i):
    
    answer = Correct_Answer

    Options.remove(answer)

    indices_to_delete = random.sample(range(len(Options)), 2)

    for index in range(len(indices_to_delete)):
        del Options[index]

    Options.insert(0,answer)

    print(f'Aapka {i+1} Sawal Hai {Money_Prices[i]} Rupay Ke Liye:- \n')
    print(Question)
    for j in range(len(Options)):
        print(f'{j+1}) {Options[j]}')
