import Colors
import threading
import os
import time
import re
import json
from KBC_Data import Money_Prices

space = " "

def play():
    def reset_progress():
        def open_json_info(filepath):
            with open(filepath,'r') as f:
                data = json.load(f)
                return data
        
        def save_player_progress(filepath,player):
            with open(filepath,'w') as f:
                json.dump({'player': player},f)
                   
        data = open_json_info("_internal\Player_info.json")
        data['player'] = []
        save_player_progress("_internal\Player_info.json",data['player'])
    
    def display_player_info():
        def get_player_info(filepath):
            with open(filepath,'r') as f:
                data = json.load(f)
                return data
            
        data = get_player_info("_internal\Player_info.json")
        headers = ["UserName", "Points", "Total Time"]

        # Display as table
        print("=" * (len(headers[0]) + len(headers[1]) + len(headers[2]) + 15))  # Adjusted length for formatting
        print(f"| {headers[0]:^10} | {headers[1]:^10} | {headers[2]:^10} |")  # Center-aligned headers
        print("=" * (len(headers[0]) + len(headers[1]) + len(headers[2]) + 15))  # Adjusted length for formatting

        for player in data['player']:
            print(f"| {player['Username']:^10} | {player['Points']:^10} | {player['Total Time']:^10} |")

        print("=" * (len(headers[0]) + len(headers[1]) + len(headers[2]) + 15))  # Adjusted length for formatting
        
    
    def get_user_choice():
        while True:    
            print(f'\n\n{Colors.blue}WELCOME TO \'KON BANEGA CROREPATTI\'\n{Colors.reset}')
            print(f"\n1. Play the game\n2. Reset the Progress\n3. Display Player info\n0. Exit")
            input_user = input("\nEnter your choice:- ")
            
            if int(input_user) == 2:
                reset_progress()
                input("\n Progress reset successfully\n\nPress enter to continue")
                os.system('cls')
            elif int(input_user) == 3:
                display_player_info()
                input("\n\nPress enter to continue")
                os.system('cls') 
            elif re.match(r'^[01]$',input_user):
                return input_user
            else:
                input("Sorry, you have selected wrong option.Please try again\nPress enter to continue")
                os.system('cls')
    
    user_choice = int(get_user_choice())
    return user_choice if user_choice in [0,1,3] else None

# Introduction and Rules
def intro():
    print(f"\n{Colors.cyan} Rules:-{Colors.reset}")
    print(f"\n 1. There are total{Colors.blue} 15 {Colors.reset} questions in Kon Banega Crorepati")
    print(f"\n 2. Price Money (aka Points System) ranges from {Colors.green}1000 - 7000000{Colors.reset}")
    print(f"\n 3. You will have 3 Lifelines:-")
    print(f'\n{Colors.blue}{space * 3}a. 50-50:-{Colors.reset}\n{space*6}"50-50" lifeline removes two incorrect options from the provided list of options \n{space*6}for a given question{Colors.reset}')
    print(f'\n{Colors.green}{space * 3}b. Poll:-{Colors.reset}\n{space*6}"Poll" lifeline presents the question with randomized percentages representing \n{space*6}audience votes for each option{Colors.reset}')
    print(f'\n{Colors.pink}{space * 3}c. Swap:-{Colors.reset}\n{space*6}"Swap" lifeline in a quiz game by replacing the current question with a randomly \n{space*6}selected question from the remaining set of questions.')
    print(f"\n 4. You can leave the game whenever you want{Colors.red} *Just Press 0 when the option pops up to you!! *{Colors.reset}")
    print(f"\n 5. Money Price (aka Points System) rules:")
    print(f"\n   {Colors.blue}a. If you have correctly answered Questions till 5 then your base money will be '10000'\n{space * 6}Else your base money will be '0' if you get any one Question wrong between 1 to 5.{Colors.reset}")
    print(f"\n   {Colors.pink}b. If you have correctly answered Questions till 10 then your base money will be '320000'\n{space * 6}Else your base money will be '10000' if you get any one Question wrong between 6 to 10.{Colors.reset}")
    print(f"\n   {Colors.green}c. If you have correctly answered Questions till 14 then your base money will be '5000000'\n{space * 6}Else your base money will be '320000' if you get any one Question wrong between 11 to 14.{Colors.reset}")
    print(f"\n   {Colors.yellow}d. The Final Question will have '7000000' Price Money. It's Totally On The Player If They \n{space*6}Want To Attempt The Final Round Or Not{Colors.reset}")
    print(f"\n{space * 5}Note:- If the Answer Given Is Wrong Then The Price Money Will Drop To '320000'")
    print(f"\n\n  {Colors.red}IF YOU HAVE USED ALL THE LIFELINES AND PRESSED THE 5TH OPTION AGAIN THEN BY DEFAULT YOU \n{space*3}HAVE TO QUIT THE GAME BY PRESSING '0'{Colors.reset}")

    input(f"\n{space * 3}Press enter to continue{space * 2}")
    
    os.system('cls')

#Displaying the levels cleared and points earned by the user
def mon(i):
    print(" Current Status of Player:- ",end= " ")
    if (i == 0):
        print(f"\n Levels Cleared = {i} \t Prize Money = {Colors.green}0{Colors.reset}\n")
    else:
        print(f"\n Levels Cleared = {i} \t Prize Money = {Colors.green}{Money_Prices[i -1]}{Colors.reset}\n")

# Questions function
def question(Question,Options,i):
    print(f'Aapka {i+1} Sawal Hai {Money_Prices[i]} Rupay Ke Liye:- \n')
    print(Question)
    for j in range(len(Options)):
        print(f'{j+1}) {Options[j]}')

#User info function 
def user_data(user_name,money,to_ti):
    def get_player_info(filepath):
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                return data.get('player',[])
            
        except FileNotFoundError:
            return []
    
    def save_player_info(filepath,player):
        with open(filepath, 'w') as f:
            json.dump({'player': player},f,indent=3)
                        
    def add_player_info(filepath,username,points,to_ti):
        player = get_player_info(filepath)
        
        to_ti = f"{to_ti:.3f} mins"
        
        new_player = {
            'Username': username,
            'Points': points,
            'Total Time': to_ti
        }
        
        player.append(new_player)
        save_player_info(filepath,player)
    
    add_player_info('_internal\Player_info.json',user_name,money,to_ti/60)

#Timer function
def get_user_input_with_timeout(timeout):
    stop_event = threading.Event()
    user_input = None

    def input_thread():
        nonlocal user_input
        try:
            input_value = input("Enter your choice: ")
            if input_value.strip():  # Check if input is not an empty string
                user_input = int(input_value)
            stop_event.set()  # Stop the countdown thread when input is received or invalid input is handled
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            stop_event.set()  # Stop the countdown thread when invalid input is handled
        except Exception as e:
            print(f"Exception in input_thread: {e}")
            stop_event.set()  # Stop the countdown thread when any other exception occurs

    def countdown_thread():
        for remaining in range(timeout, 0, -1):
            if stop_event.is_set():
                break  # Exit the loop if stop_event is set
            print(f"\rTime remaining:{Colors.red} {remaining} {Colors.reset}seconds{space*2}Enter your Choice:- ", end="")
            time.sleep(1)
        stop_event.set()  # Ensure the countdown thread stops

    stop_event.clear()  # Clear the event before starting new threads

    input_thread_obj = threading.Thread(target=input_thread)
    input_thread_obj.daemon = True
    input_thread_obj.start()

    countdown_thread_obj = threading.Thread(target=countdown_thread)
    countdown_thread_obj.daemon = True
    countdown_thread_obj.start()

    input_thread_obj.join(timeout)

    if input_thread_obj.is_alive():
        print(f"\n\n{Colors.red}Timeout! You didn't provide input within the specified time{Colors.reset}.\n\nPress enter to continue")
        input_thread_obj.join()  # Ensure input_thread stops

    stop_event.set()  # Ensure the countdown thread stops

    return user_input

if __name__ == "__main__":
    intro()
    # play()
    pass
    