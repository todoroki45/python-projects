import random
from playsound import playsound
print("gusses the no. between 1 to 100")
randomnumber=random.randint(1,100)
usergusses=None
gusses=0
while (usergusses!=randomnumber):
    usergusses= int(input("enter your gusses :"))
    gusses +=1
    if (usergusses==randomnumber):
        print("you gusses it right")
        # playsound("D:\\To Kasa Ho Ap Log - Remix.mp3")
    else:
        if (usergusses>randomnumber):
            print("you gusses it wrong ! gusses smaller number ")
            # playsound("D:\\Kon Hai Tu - Carryminati Meme.mp3")  
        else:
            print ("you gusses it wrong ! gusses the larger number ")
            # playsound("D:\\Kon Hai Tu - Carryminati Meme.mp3") 
print("you gusses in range gusses",gusses)
