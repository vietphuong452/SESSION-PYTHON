# Từ nay trở đi các bạn chỉ cần from youtube_dl import YoutubeDL thay vì copy code dài dòng từ document
from youtube_dl import YoutubeDL
# Option là 1 dicts mở rộng giúp thêm tính năng cho ydl, khi không sử dụng tính năng hãy đễ dicts trống như dưới
options = {
    'outtmpl': '%(id)s', # lấy tên file down về là id của video, lấy id làm tên file để tiện quản lí
'postprocessors': [{
    'key': 'FFmpegExtractAudio', # Tách lấy audio
    'preferredcodec': 'mp3', # Format ưu tiên là mp3
    'preferredquality': '192', # Chất lượng bitrate

}]}

ydl = YoutubeDL(options)

# download() có thể truyền vào 1 str hoặc 1 list
ydl.download(["https://www.youtube.com/watch?v=2Vv-BfVoq4g"])