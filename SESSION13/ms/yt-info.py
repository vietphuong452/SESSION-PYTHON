# Từ nay trở đi các bạn chỉ cần from youtube_dl import YoutubeDL thay vì copy code dài dòng từ document
from youtube_dl import YoutubeDL
# Option là 1 dicts mở rộng giúp thêm tính năng cho ydl, khi không sử dụng tính năng hãy đễ dicts trống như dưới
options = {}

ydl = YoutubeDL(options)

# extract_info() truyền vào 1 str và trả về kq là 1 json, có thể thêm 1 tham số là download=False để không cần down(mặc định là True)
info = ydl.extract_info("https://www.youtube.com/watch?v=2Vv-BfVoq4g", download=False)

#Thay vì print ra hãy ghi ra file cho dễ đọc
# print(info)

# Để dễ nhìn bạn có thể ghi json ra file theo hướng dẫn https://appdividend.com/2019/04/15/how-to-convert-python-dictionary-to-json-tutorial-with-example/ phần "Writing JSON to a file"
import json
with open('info.json', 'w',encoding="utf8") as json_file:
  json.dump(info, json_file)
