map={
    'x':4,
    'y':4,

}
P={
    'x':2,
    'y':1,

}
K={
    'x':1,
    'y':2,

}
E={
    'x':3,
    'y':2,

}
flag = True
a = True
while True:
    for y in range(map["y"]):
        for x in range(map["x"]):
            if P['x']==x and P['y']==y:
                print('P',end=" ")
            elif  K['x']==x and K['y']==y:
                if flag == True:
                    print('K',end=" ")
                else:
                    print("-",end=" ")
            elif E['x']==x and E['y']==y:
                print('E',end=" ")
            else:
                print("-",end= " ")
        print()
    if  P['x']== E['x'] and P['y']== E["y"]:
        if flag == False:
            print("EXIT")
            break
        else:
            print("You need a key to exit")
    a= input("Move: ").upper()
    if a=="W":
        P['y']-=1
    elif a=="S":
        P['y']+=1
    elif a=="D":
        P['x']+=1
    elif a=="A":
        P['x']-=1
    else:
        break
    if P['x']== K['x'] and P['y']== K["y"]:
        flag = False
        print("You have the key")
    

        


    