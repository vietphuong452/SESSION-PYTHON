import json
#Mở file json 
with open('example.json',"r+",encoding="utf8") as json_file:  
    #Load file json vào biến data
    data = json.load(json_file)
    person={'name':'Nguyen Thi B', 'age':15}
    # #Thêm thông tin vào biến data
    data.append(person)
    print(data)
    #Xóa toàn bộ file json cũ và ghi đè
    json_file.seek(0)
    #Ghi lại file json mới
    json.dump(data, json_file)