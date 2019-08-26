skills=[
    {
        '1': 'kick',
        '2': 'slap',
        '3': 'shoot',
        '4': 'jump',
        'hi-rate': 0.3
    }
]
from random import*
for i in range(len(skills)):
    for j in skills[i]:
        if j =='hi-rate':
            break
        print(j,skills[i][j],sep=":")
            
a=int(input("Choose a skill: "))
b=randint(0,10)*0.1
if b<0.8:
    print("Miss")
else:
    if a == 1:
        print("-1000")
    elif a == 2:
        print("-2000")
    elif a == 3:
        print("-3000")
    elif a == 4:
        print("-4000")
