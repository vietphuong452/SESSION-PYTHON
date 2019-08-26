# loop_count= 0
# while loop_count < 2:
#     print("How many legs an octopus has:")
#     a = ['one leg','two legs','six legs','eight legs']
#     for i,a in enumerate(a):
#         print(i+1,a,sep = ".")
#     b= int(input("Your answer : "))
#     if b== 4:
#         print("You are correct")
#     else:
#         print("Not a correct answer")
#     loop_count+=1








diem = 0
a=[
    {
            'Question':'How many legs an octopus has',
            '1.' : 'One leg',
            '2.' :  'Two legs',
            '3.' : 'Three leg',
            '4.' : 'Eight legs',
            'answer-right': 4,
    },
{
        'Question':'How many legs a dog has',
        '1.' : 'One leg',
        '2.' :  'Two legs',
        '3.' : 'Four leg',
        '4.' : 'Eight legs',
        'answer-right': 3
}
]
for i in range(len(a)):
    for j in a[i]:
        if j == "answer-right":
            break
        print(j,a[i][j])
    b= int(input("Your answer: "))
    if b== a[i]['answer-right']:
        print("You are correct")
        diem = diem +1
    else:
        print("Not a correct answer")
print("Score:",diem)
a= diem/2*100
print("percentage:",a)


