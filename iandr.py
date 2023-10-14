
import Colors
import os
def intro():
    print(f"\n{Colors.cyan} Rules:-{Colors.reset}")
    print(f"\n 1. There are total{Colors.blue} 15 {Colors.reset} question in Kon Banega Crorepati")
    print(f"\n 2. Money price(aka Points) are from {Colors.green}1000 - 7cr{Colors.reset}")
    print("\n 3. You will have Life Line\n a. 50-50")
    print(f"\n 4. You can leave the game whenever you want{Colors.red} *Just Press 0 when the option pop's up to you!! *{Colors.reset}")
    response = input(" Press any key to continue")
    
    os.system('cls')