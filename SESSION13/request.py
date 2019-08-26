import json

import requests
r = requests.get('https://jsonplaceholder.typicode.com/users')
r1 = r.json()
print(len(r1))
ask = input("Nhap vao ten:").upper()
for i in range(len(r1)):
        if r1[i]["username"].upper() == ask:
        print(r1[i])
