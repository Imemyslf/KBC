import random
import Colors
import threading
import os
import time
from KBC_Data import Questions,Money_Prices


space = " "
# Introduction and Rules
def intro():
    print(f"\n{Colors.cyan} Rules:-{Colors.reset}")
    print(f"\n 1. There are total{Colors.blue} 15 {Colors.reset} question in Kon Banega Crorepati")
    print(f"\n 2. Price Money(aka Points System) are from {Colors.green}1000 - 7000000{Colors.reset}")
    print(f"\n 3. You will have Life Line\n {space * 3}a. 50-50\n {space * 3}b. Poll")
    print(f"\n 4. You can leave the game whenever you want{Colors.red} *Just Press 0 when the option pop's up to you!! *{Colors.reset}")
    print("\n 5. Money Price(aka Points System) rule")
    print(f"\n   a. If you have correctly answered Questions till 5 then your base money will be '10000' \n {space * 5}Else your base money will be '0' if you get any one Question wrong between 1 to 5. ")
    print(f"\n   b. If you have correctly answered Questions till 10 then your base money will be '320000' \n {space * 5}Else your base money will be '10000' if you get any one Question wrong between 6 to 10. ")
    print(f"\n   c. If you have correctly answered Questions till 14 then your base money will be '5000000' \n {space * 5}Else your base money will be '320000' if you get any one Question wrong between 11 to 14. ")
    print(f"\n   d. The FInal Question will have '7000000' Price Money. It's Totally On The Player If They Want To Attempt The Final Round Or Not \n {space * 5}Note:- If the Answer Given Is Wrong Then The Price Money Will Drop To '320000'")
    response = input(f"\n{space * 3}Press enter to continue{space * 2}")
    
    os.system('cls')
    
def ques(Question,Options,i):
    print(f'Aapka {i+1} Sawal Hai {Money_Prices[i]} Rupay Ke Liye:- \n')
    
    print(Question)
    
    for j in range(len(Options)):
        print(f'{j+1}) {Options[j]}')
    pass   


stop_event = threading.Event()
def get_user_input_with_timeout(timeout):
    user_input = None

    def input_thread():
        nonlocal user_input
        user_input = int(input("\nEnter your choice:-  "))
        stop_event.set()  # Stop the countdown thread when input is received

    def countdown_thread():
        print("\n")
        for remaining in range(timeout, 0, -1):
            if stop_event.is_set():
                break  # Exit the loop if stop_event is set
            print(f"\rTime remaining: {remaining} seconds ", end="")
            time.sleep(1)
        if not stop_event.is_set():
            print("\rTime remaining: 0 seconds")

    stop_event.clear()  # Clear the event before starting new threads

    input_thread_obj = threading.Thread(target=input_thread)
    input_thread_obj.daemon = True
    input_thread_obj.start()

    countdown_thread_obj = threading.Thread(target=countdown_thread)
    countdown_thread_obj.daemon = True
    countdown_thread_obj.start()

    input_thread_obj.join(timeout)

    if input_thread_obj.is_alive():
        print("\nTimeout! You didn't provide input within the specified time.")

    return user_input

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
    mon(i)
    ques(Question,Options,i)
    # print(f'Aapka {i+1} Sawal Hai {Money_Prices[i]} Rupay Ke Liye:- \n')
    # print(Question)
    # for j in range(len(Options)):
    #     print(f'{j+1}) {Options[j]}')
    
    Answer = int(input("Enter the answer:- "))
    answer = [Answer,Options]
    return answer


# Life_line_2  
def poll(Question,Options,Correct_Answer,i):
    os.system('cls')
    choice = []
    space = " "
    large = 0

    #Assigning The correct answer in the variable answer
    answer = Correct_Answer
    
    #Choosing Percentage for the Correct Answer
    choice_1_answer = random.randint(33,38)
    
    #Choosing Percentage for the random options
    choice_0 = random.randint(20,35)
    
    #removal of the correct answer from the Options List
    Options.remove(answer)
    
    # Randomly Selecting any 1 option from The Options list
    random_option = random.sample(range(len(Options)), 1)
    i_rand = random_option[0] # assigning the index value of the randomly selected option
    print(i_rand)
    
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
    choice_3 = random.randint(10,20)
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
    
    
    for i in range (len(choice)):
        if (choice[i] > large):
            large = choice[i]
            inti  = i
    
    final_answer = Options[inti]
    print(f"\n Audience vote:- {final_answer}")
    poll_answer= input(f"\n Do you want to continue with the poll?(Y?N){space*2}")
    if (poll_answer.upper() == "Y" or poll_answer.upper() == "YES"):
        final_answer = inti
        fa = [1,final_answer,Options[final_answer]]
        return fa
    else:
        fa = [0]
        return fa



def mon(i):
    print(" Current Status of Player:- ",end= " ")
    if (i == 0):
        print(f"\n Levels Cleared = {i} \t Prize Money = {Colors.green}0{Colors.reset}\n")
    else:
        print(f"\n Levels Cleared = {i} \t Prize Money = {Colors.green}{Money_Prices[i -1]}{Colors.reset}\n")



def swap(i,value):

        # Create two separate arrays using slicing
        current_question = Questions[i][value]
        remaining_questions = Questions[i][:value] + Questions[i][value + 1:]
        Question, Options, Correct_Answer, Description = remaining_questions[random.randint(0,3)].values()
        quest = Question, Options, Correct_Answer, Description
        
        return quest
    
def game():
    
    random.seed(time.time())
    for i in range(len(Questions)):
        random_int = random.randint(0, 3)
        print(random_int)
        Qu,Op,Co_A,Des = Questions[i][random_int].values()
        random.shuffle(Op)

        print(Qu)
        
        for j in range(len(Op)):
            print(f"{j+1} {Op[j]}")
        
        answer = input("")
        if answer == "s":
            Swap = list(swap(i,random_int))
            qu,op,ca,des = Swap
            print(Swap)
            print(f"Question:-{qu}\nOptions:- {op}\n Correct answers:- {ca}\n Description:- {des}")            
            
            
            
        
if __name__ == "__main__":
    # intro()
    # ranopt()
    # poll()
    # mon(5)
    # swap()
    game()
    pass