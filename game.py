import threading
import time
from findertools import sleep
default_ans = ["to melt", "for melting", "melt"]
sys_code = [7, 5, 6, 3, 9]
    
def gameOver():
    print('''\nYou died...''')
    time.sleep(2)
    print('''GAME OVER!''')
    time.sleep(2)
    print("Do you want to play again? (y/n) : "),
    d8 = raw_input()
    if d8 == "y":
        displayIntro()
    elif d8 == "n":
         quit()   
def safeHouse():
    print("Good! You are in the safe zone now")
    time.sleep(4)
    print("The Bomb Explodes!!!!")
    time.sleep(3)
    print("Everyone dies except you and some others who took precaution")
    time.sleep(3)
    print('''In search of some foods and medicines you go back to your demolished house
and you find a wild dog''')
    time.sleep(4)
    print("Will you fight it or tame it? (f/t)")
    d3 = raw_input()
    if d3 == "f":
        print("The dog bit you")
        gameOver()
    elif d3 == "t":
        print("To tame this wild dog you have to solve a riddle")
        print("Let's Start")
        time.sleep(3)
        print("You have 30 seconds...STARTING...")
        time.sleep(2)
        print("3 ") , 
        time.sleep(1),  
        print("2 "),  
        time.sleep(1), 
        print("1 ")
        #set timer
        print('''The dog loves to be called by its own name which is set after a vehicle which is often used in wars''')
        time.sleep(4)
        print('''He is a bit bulky too''')
        time.sleep(3)
        print("So what would you call him? : ")
        timer2 = threading.Timer(25.0,gameOver)
        timer2.start()
        d_name = raw_input()
        timer2.cancel()
        if d_name == "Tank" or d_name == "tank" or d_name == "TANK":
            print("Yes...you called him tank and he loves it")
            time.sleep(3)
            print("You tamed the dog")
            continuation()
        else:
            print("You are wrong....The dog bit you")
            gameOver()                  
def sysHack():    
    print("Ok...So you have to get the password to get access to their system")
    time.sleep(3)
    print('''You have 30 seconds...STARTING...'''),
    time.sleep(2)
    print("3 ") , 
    time.sleep(1),  
    print("2 "),  
    time.sleep(1), 
    print("1 ")
        
    #set timer
    print('''In the range of 1-9, Write the possible values that are divisible by any odd number greater than 1 (Without any space) ''')
    timer = threading.Timer(30.0,gameOver)
    timer.start()
    ans = raw_input()
    timer.cancel()
    if ans == "35679":
        print("You have neutralized the system's first level of defense")
        time.sleep(3)
        print("Now organize it in ascending order replacing the greatest prime number with the smallest one. Insert one value at a time:")
        time.sleep(3)
        test_code = []
        for i in range(0, 5):
            print ("Slot %d: " %(i+1)),
            ele = int(input())
            test_code.append(ele)
                
        if test_code==sys_code:
            print("LOADING"),
            for i in range(7):
                print("."),
                time.sleep(1),
                
            print("\nYes...You have gained access to their system and made you and your wife's profile")
            safeHouse()
        else:
            print("You are not a good programmer and wasn't able to hack")
            gameOver()
    else:
        print("You are not a good programmer and wasn't able to hack")
        gameOver()
def continuation():
    print("You trained the dog and now it helps you to find things to survive")
    time.sleep(3)
    print("You found a precious medicine that helps to survive for a long time without foods")
    time.sleep(3)
    print("Suddenly the terrorist group called The Order attacked the safe zone and killed everyone in search of the medicine except your wife")
    time.sleep(5) 
    print("You found a radio  informing that your wife has been kidnapped and will be killed if you don't hand over them that medicine")
    time.sleep(5)
    print("Do you accept their offer? (y/n)")
    d4 = raw_input()
    if d4=="y":
        final_round()
    elif d4 == "n":
        gameOver()  
def final_round():
    print("Finally you went there and you have two ways in your mind:")
    time.sleep(5)
    print("1. "),
    time.sleep(2),
    print("You face them and hand over the medicine")
    time.sleep(4)
    print("2. "),
    time.sleep(2),
    print("Blend in, Get your wife and run away")
    time.sleep(3)
    print("Which one will you prefer? (1/2): ")
    d5 = raw_input()
    if d5 == "1":
        print("Alas!"),
        time.sleep(3)
        print("Your wife is killed")
        gameOver()
    elif d5== "2":
        print("You blended into their area, found your wife in the basement locked in a cage that has a small window with grills")
        time.sleep(4)
        options()
def options():
    print("So you have 3 options:")
    time.sleep(3)
    print("1. "),
    time.sleep(2),
    print("Use your hammer to break the lock")
    time.sleep(4)
    print("2. "),
    time.sleep(2),
    print("Use your dog to fetch the key from the security guard")
    time.sleep(4)
    print("3. "),
    time.sleep(2),
    print("Search for the bag that's kept beside the cage")
    time.sleep(4)
        
    print("So which option you choose? (1/2/3) : ")
    d6 = raw_input()
    if d6=="1":
        print("You created too much noise and got their attention")
        time.sleep(3)
        gameOver()
    elif d6 == "2":
        print("The security killed the dog and you are spotted")
        time.sleep(3)
        gameOver()
    elif d6 == "3":
        print("You found a high temperature torch which burns at 3000C")
        time.sleep(3)
        print("Is it useful to you? (y/n) : ")
        d7 = raw_input()
        if d7=="y":
            print("How does it help you?")
            time.sleep(2)
            print("Your Answer (in small letters): "),
            f_ans = raw_input()
            if f_ans.find(default_ans[0]) != -1 or f_ans.find(default_ans[1]) != -1 or f_ans.find(default_ans[2]) != -1:
                print("Good job! Your answer is correct")
                time.sleep(2)
                print("You have melted the grills of the window and managed to run away with your wife")
                time.sleep(3)
                win()
            else:
                print("You failed to answer...You loose")
                time.sleep(2)
                gameOver()  
        elif d7=="n":
            options()
def win():
    print("You Win!!!")
    time.sleep(2)
    print("Congratulations...")
    time.sleep(2)
    print("Do you want to play again? (y/n) : "),
    d9 = raw_input()
    if d9 == "y":
        displayIntro()
    elif d9 == "n":
        quit()
def displayIntro():
    print('''Suppose that you and your wife are sitting in your living room when someone knocks on your door.''')
    time.sleep(4)
    print("Do you want to open the door? (y/n): "),
    d0=raw_input()
    if d0=="n":
        print("There's been an announcement that there will be a nuclear attack in 24 hours")
        time.sleep(2)
        print("Now you cannot register for shelter from the private underground protection representative because you did not accept their offer by not opening the door")
        time.sleep(7)
        print("So the only way is to hack their system and make your and your wife's profile to get access to the safe zone")
        time.sleep(4)
        print("Do you want to hack the system or leave it? (h/l)")
        d2 = raw_input()
        if d2 == "h":
            sysHack()
        elif d2 == "l":
            gameOver()
    elif d0 == "y":
        print('''There is a private underground protection representative who offers you to reserve a bunker underground, just in case there is a war break out .''') 
        time.sleep(4)
        print("Will you accept their proposal? (y/n)")
    
        d1 = raw_input();

        if d1=="y":
            print("Alas!")
            time.sleep(2)
            print("It costs 10,000$ and you don't have enough money to register")
            time.sleep(4)
            print("Now you can hack their system and make your and your wife's profile to get access to the safe zone")
            time.sleep(4)
            print("Do you want to hack the system or leave it? (h/l)")
            d2 = raw_input()
            if d2 == "h":
                sysHack()
            elif d2 == "l":
                gameOver()
    
        elif d1=="n":
            print("There's been an announcement that there will be a nuclear attack in 24 hours and now you cannot register to seek shelter")
            time.sleep(2)
            print("Now the only way is to hack their system and make your and your wife's profile to get access to the safe zone")
            time.sleep(2)
            print("Do you want to hack the system or leave it? (h/l)")
            d2 = raw_input()
            if d2 == "h":
                sysHack()
            elif d2 == "l":
                gameOver()
        
displayIntro()
