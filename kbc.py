
money = 0
ques = [ 
        ["Highest mountain the world?","Mt.Everest","Mt.Fugi","Mt.Kilimanjaro","Mt.Denali",1],
        ["Fastets animal in the world?","Tiger","Girrafe","Chetah","Lion",3],
        ["Longest river in the world?","Amazon","Nile","Godavri","Kaveri",2],
        ["Heighest Architecture Building in the world?","Sydney Opera House","Eiffel Tower","Leaning Tower of Pis","Burj Khalifa",4],
        ["Tallest human made Statue in the world?","Spring Temple Buddha"," Laykyun Sekkya","Statue of Unity","Statue of Belief",3]
        ["Which of the following is a root vegetable?","Carrot","Cassava","Onion","All the above ",4],
        ["Which of the following diseases is caused by the deficiency of Vitamin C?","Scurvy","Chronic Inflammation and Oxidative Stress","Bleeding Gums","All the above",4],
        ["Which animal is Yama's vehicle?","Crocodile","Buffalo","Tiger","None of the above",2],
        ["In which of the following state of India Valmiki Tiger Reserve is located?","Chattisgarh","Jharkhand","Bihar","Madhya Pradesh",3],
        ["Full of RAC related to Railways are?","Retail Asset Centre","Reservation Against Cancellation","Rajasthan Armed Constabulary","Refregeration & Air Conditioning",2],
        ["The first non-congress PM who completed a full term as PM in India?","Atal Bihari Vajpayee","H. D. Deve Gowda","Narendra Modi","Inder Kumar Gujra",1],
        ["Whic one of thr first avatar of Lord Vishnu from his Dashavatar?","Matsya","Kurma","Varah","None of the above",1],
]

monpri = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000]
print(monpri[-1])
print("\n WELCOME TO \"KON BANEGA CROREPATTI\" ")
for i in range(0,len(ques)):
    if (i>= 5 and i<10):
        money = 10000
    elif (i>=10 and i < 17):
        money = 320000
    else:
        money = monpri[-1]
    que = ques[i]
    print(f"Aapka {i+1} Sawal Hai {monpri[i]} Rupay Ke Liye: \n")
    print(que[0])
    print(f"1.{que[1]}\n2.{que[2]}")
    print(f"3.{que[3]}\n4.{que[4]}")
    ans = int (input("Enter your ans in (1-4): "))
    if (ans == que[5]):
        print(f"Aap Jeeth Juke Hai {monpri[i]} Rupay\n ")
        money += monpri[i]
    else:
        print("\nGalat Jawaab Aapka khel Yahi Samapt Hota Hai!!")
        break

print(f"\n Aap apne saath {money} Rupay Lekar Ja Rahe Hai!!")
print("\n DHANYAWAAD HUMARA KHEL KHELNE KE LIYE")