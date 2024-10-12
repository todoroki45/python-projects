import random                   #step 1st import function
from playsound import playsound
def gamewin(com, you):  #make function step 2nd
    if com==you:
        return None

    elif com=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
    
    elif com=="w":
        if you=="s":
            return True
        elif you=="g":
            return False
        
    elif com=="g":
        if you=="w":
            return True
        elif you=="s":
            return False
    
print("com tern :gun(g) snake(s) water(w)")
randomno=random.randint(1,3)     #step 3 computer enter ramdomly so we used randint function
if randomno ==1:
    com="g"
elif randomno==2:
    com="s"
elif randomno==3:
    com="w"
    
you=input("your turn: gun(g) snake(s) water(w) :") #step 4 you enter you step

a=gamewin(com,you)   #function call

print("computer choose",com)  #print what computer choose
print("you choose ",you)      #print what you choose

if a==None:                       #step 5 "output"
    print("the game is tie 😒")
    playsound("D:\\sound\\Kon Hai Tu - Carryminati Meme.mp3")
elif a:    #a==true
    print("you win 🤩")
    playsound("D:\\sound\\Carryminati Mene - Shabash.mp3")
else:      #a==false
    print("you lose 🤣")
    playsound("D:\\sound\\Indian Guy Laughing Meme.mp3")
    
