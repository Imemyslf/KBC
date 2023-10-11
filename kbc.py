import time
import random
from KBC_Data import Questions, Money_Prices

# Initialize a variable to keep track of the player's earnings
money = 0

# Display a welcome message
print("WELCOME TO \"KON BANEGA CROREPATTI\"\n")

# Seed the random number generator with the current time to make shuffling random
random.seed(time.time())

# Loop through the questions
for i in range(len(Questions)):
    # Randomly select a question, its options, correct answer, and description
    Question, Options, Correct_Answer, Description = Questions[i][random.randint(0, 4)].values()

    # Shuffle the answer options to present them in a random order
    random.shuffle(Options)

    # Display the question and available options
    print(f"Aapka {i+1} Sawal Hai {Money_Prices[i]} Rupay Ke Liye:- \n")
    print(Question)
    for j in range(len(Options)):
        print(f'{j+1}) {Options[j]}')

    # Prompt the user for their answer
    Answer = int(input('Enter your answer in (1-4) : '))
    time.sleep(3) # for Suspense

    # Check if the user's answer matches the correct answer
    if Correct_Answer in Options[Answer-1]:
        print(f"\nAap Jeeth Juke Hai {Money_Prices[i]} Rupay")
        money = Money_Prices[i]
    else:
        print("Galat Jawaab Aapka khel Yahi Samapt Hota Hai!!")
        break

# Display the total earnings and a thank you message
print(f"Aap apne saath {money} Rupay Lekar Ja Rahe Hai!!")
print("DHANYAWAAD HUMARA KHEL KHELNE KE LIYE")
