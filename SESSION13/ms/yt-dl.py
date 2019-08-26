# Từ nay trở đi các bạn chỉ cần from youtube_dl import YoutubeDL thay vì copy code dài dòng từ document
from youtube_dl import YoutubeDL
# Option là 1 dicts mở rộng giúp thêm tính năng cho ydl, khi không sử dụng tính năng hãy đễ dicts trống như dưới
options = {}

ydl = YoutubeDL(options)

# download() có thể truyền vào 1 str hoặc 1 list
ydl.download(["https://www.youtube.com/watch?v=2Vv-BfVoq4g"])