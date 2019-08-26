yob = int(input("Your year of birth : "))
age = 2019 - yob
print("you are :" ,age)

if age<10:
    print("young")
elif age < 18:
    print("teenager")
else:
    print("adult")