#issues:
#need to keep the number of names that are printed 
#using the names that are left over and putting them in team2 or left over team

import random


plrs=[]
team1=[]
team2=[]


plr_num=int(input("how many players do you have "))
team=int(input("how many teams do you want? "))
plr_team=int(plr_num/team)


y=0
while y < plr_num:
    name=input("enter a players name ")
    plrs.append(name)
    y=y+1




x=0
while x<team:
    random.shuffle(plrs)
    for i in range(0, len(plrs), plr_team):
        chunk=plrs[i:i+plr_team]
        if chunk==plrs:
            plrs.remove(chunk)
        else:
            print(chunk)
    x=x+2
    
    

