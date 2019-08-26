# while True:
#     name = input( "Your name is :")
#     print(name)
#     if name.isalpha():
#         print("Done") 
#         break
#     else:
#         print("Rewrite your name")







# while True:
#     passw = input("Enter your password : ")
#     if passw.isdigit():
#         print("Done")
#         break
#     else:
#         print("Incorrect password")







# while True:
#     passw = input("Enter your password : ")
#     if len(passw) > 8:
#         print("Only 8 characters")
#         while True:
#             passw = input("Enter your password :") 
#             if len(passw) < 8:
#                 break
#     if passw.isdigit():
#         print("DONE")
#         break
#     else:
#         print("Only number")





# num1 = 42859
# num2 = 10
# a = num1 // num2
# print(a)






# number = input("Pick a random number: ")
# d={"DIGITS":0}
# for c in number:
#     if c.isdigit():
#         d["DIGITS"]+=1    
# print("The number you entered has",d["DIGITS"] )






# s = input("Nhập câu của bạn: ")
# # Bài tập Python 16, Code by Quantrimang.com
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print ("Số chữ cái là:", d["LETTERS"])
# print ("Số chữ số là:", d["DIGITS"])





# import pyglet

# music = pyglet.resource.media('sample.wav.mp3')
# music.play()

# pyglet.app.run()



# import datetime

# datetime_object = datetime.datetime.now()
# print(datetime_object)





