import random
import Colors
import os
from KBC_Data import Questions,Money_Prices

# Introduction and Rules
def intro():
    print(f"\n{Colors.cyan} Rules:-{Colors.reset}")
    print(f"\n 1. There are total{Colors.blue} 15 {Colors.reset} question in Kon Banega Crorepati")
    print(f"\n 2. Money price(aka Points) are from {Colors.green}1000 - 7cr{Colors.reset}")
    print("\n 3. You will have Life Line\n a. 50-50\n b. Poll")
    print(f"\n 4. You can leave the game whenever you want{Colors.red} *Just Press 0 when the option pop's up to you!! *{Colors.reset}")
    response = input(" Press enter to continue\t")
    
    os.system('cls')
    
    

#Life_line_1
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

# Life_line_2 
def poll(Options,Correct_Answer):
    os.system('cls')
    choice = []
    space = " "
    large = 0

    # for i in range(len(Questions)):
    #     Question, Options, Correct_Answer, Description = Questions[i][random.randint(0, 4)].values()

    #Assigning The correct answer in the variable answer
    answer = Correct_Answer
    
    #Choosing Percentage for the Correct Answer
    choice_1_answer = random.randint(35,37)
    
    #Choosing Percentage for the random options
    choice_0 = random.randint(35,38)
    
    #removal of the correct answer from the Options List
    Options.remove(answer)
    
    # Randomly Selecting any 1 option from The Options list
    random_option = random.sample(range(len(Options)), 1)
    i_rand = random_option[0] # assigning the index value of the randomly selected option
    
    # Assigning the string of randomly selected option to i_rand_remove
    for i in range(len(Questions)):
        if (i_rand == i):
            i_rand_remove = Options[i]
    
    # Removal of randomly selected option       
    Options.remove(i_rand_remove)
    #Appending the randomly selected option into the Options at index value 0
    Options.insert(0,i_rand_remove)
    #Appending the Correct Answer into the Options at index value 1
    Options.insert(1,answer)
    
    #Appending the percentage generated for the random option at index 0
    choice.insert(0,choice_0)
    
    #Appending the percentage generated for the correct answer at index 1
    choice.insert(1,choice_1_answer)
    
    # Genrating a random number for third option in the choice list 
    choice_3 = random.randint(10,15)
    #Appending the percentage generated for the third option at index 2
    choice.insert(2,choice_3)
    
    # Subtracting all the values from the choice list and getting the reaming value 
    remaining_value = 100 - (choice_1_answer + choice_0 + choice_3) 
    
    # Append the remaining values to the choice list
    choice.insert(3,remaining_value)
    
    # Finding the largest string in the Option's list and assigning it to the large
    for i in range(len(Options)):
        # Assigning the value as per thier index number(i)
        op = Options[i]
        
        # finding the length of the individual string present in the option list
        op_name = len(op)
        
        if (op_name > large): 
            # if length of the string present in the option list is greater than assign large = length of the string
            large = op_name

    # Generating a new Options1 list to append the remaining spaces to be printed in the output screen
    Options1 = []
    for i in range(len(Options)):
        opt = Options[i]
        # Generating remaing spaces by sbutracting the largest length of the string to the actul string present in the option list
        # Example: remaining_spaces(6) = KonBanega (length of the string is 9) - KBC (length of the string is 3)
        remaining_spaces= (large - len(opt))
        Options1.append(remaining_spaces)
    
    # Displaying Poll
    for i in range (len(choice)):
        cho = choice[i]
        opt = Options[i]
        opt1 = Options1[i]
        
        str1 = opt + (space * opt1) 
        print(f"{str1} ",end="")
        
        for i in range(cho):
            if (i == 0 ):
                print("",end="")
            elif (i >= 0 and i < (cho -1)):
                print(f"{Colors.white_highlight} {Colors.reset}",end="")
        
        for i in range(cho):
            if (i == 9):    
                print(f" {cho} %")

        print(f" {space * (large + 1)}",end="")
        
        print("\n")
    
    

if __name__ == "__main__":
    intro()
    ranopt()
    poll()