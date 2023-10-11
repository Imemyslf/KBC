import random
from KBC_Data import Questions, Money_Prices

money = 0

print("WELCOME TO \"KON BANEGA CROREPATTI\"\n")

for i in range(len(Questions)):
    Question, Options, Correct_Answer, Description = Questions[i][random.randint(0, 4)].values()
    random.shuffle(Options)

    print(f"Aapka {i+1} Sawal Hai {Money_Prices[i]} Rupay Ke Liye:- \n")
    
    print(Question)
    
    for j in range(len(Options)):
        print(f'{j+1}) {Options[j]}')

    Answer = int(input('Enter your answer in (1-4) : '))

    if(Correct_Answer in Options[Answer-1]):
        print(f"\nAap Jeeth Juke Hai {Money_Prices[i]} Rupay")
        money = Money_Prices[i]
    else:
        print("Galat Jawaab Aapka khel Yahi Samapt Hota Hai!!")
        break

print(f"Aap apne saath {money} Rupay Lekar Ja Rahe Hai!!")
print("DHANYAWAAD HUMARA KHEL KHELNE KE LIYE")