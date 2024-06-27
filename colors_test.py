# global money
# money1 = 1
# def deduct():
#     money = money1 
#     # print(money)
#     if (money == 1):
#         print("Money:- ", money)
#         money1 = 0
#     else:
#         print("Money: ", money)

# deduct()
# deduct()

money1 = 1  # Define money1 as a global variable

def deduct():
    global money1  # Declare money1 as a global variable
    money = money1
    if money == 1:
        print("Money:", money)
        money1 = 0  # Modify the global variable money1
    else:
        print("Money:", money)

deduct()
deduct()
