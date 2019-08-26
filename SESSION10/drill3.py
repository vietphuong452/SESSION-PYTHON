loop_count = 0
while loop_count<2:
    c={
    "Age": "25",
    "Born": "Canada",
    "Status": "Married"
    }
    b={
    "Age":'25',
    "Born": 'Thai Binh',
    "Status": 'Single',
    }
    a= input("Choose a single : Son Tung or Justin Bieber: ").upper()
    if a == "ST":
        for i in b:
            print(i,":",b[i])
    if a == "JB":
        for i in c:
            print(i,":",c[i])
    loop_count +=1

