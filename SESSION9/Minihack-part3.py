# a = ['5', '1', '8', '92','-1', '30']
# num = input("Number : ")
# if num in a:
    # for i in range(len(a)):
    #     if num == a[i]:
    #         print("Found,Position:",i + 1)
    # for i,item in enumerate(a):
    #     if num == item:
    #         print("Found",num,"Position:",i + 1)








# a = [4234,23,423,4,234,24,234,24,234,32]
# sum = 0
# for i in a:
#     sum = sum + i
#     print(sum)







# a = [1,23,45]
# b=0
# for i in a:
#     b = i + b
#     print(b)









a = (input("Enter Your Number : ").split(" "))
a = list(a)
sum = 0 
for i in a:
    sum = sum + int(i) 
print(sum)
