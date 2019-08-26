while True:
    txt = input("YEAR OF YOUR BIRTH")
    print(txt)
    if txt.isdigit():
        print("A number")
        break
    else:
        print("Not a number")

print(2019-int(txt))

