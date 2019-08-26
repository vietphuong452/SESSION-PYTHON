# Thêm tùy chọng default_search với giá trị là ytsearchx (x là số video muốn lấy)
# Ví dụ ytsearch2 lấy top 2 Video khi search
# Thêm quite: True để ẩn thông tin (Downloading webpage)
from youtube_dl import YoutubeDL
options = {
    'default_search': 'ytsearch2',
    'quiet': True
}

ydl = YoutubeDL(options)
search_result = ydl.extract_info('that girl', download=False)

#Thay vì print ra hãy ghi ra file cho dễ đọc
# print(search_result)

import json
with open('search.json', 'w',encoding="utf8") as json_file:
  json.dump(search_result, json_file)

# Json là 1 dicts và bạn hoàn toàn có thể đọc nó show ra kết quả như sau

videos = search_result["entries"]

for video in videos:
  print(f"Tên {video['title']}, Id của Video {video['id']}, upload bởi {video['uploader']}")
  print("Tên", video['title'], "Id của Video ",video['id'],", upload bởi", video['uploader'])