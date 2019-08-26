print("Press enter a number")
a=['Show all songs','Show detail of the song','Play a song','Search and download song','Exit']
for i, a in enumerate(a):
    print(i+1,a,sep=".")
b= int(input("==> "))

if b == 4:
    c= input("Which Song: ")
    from youtube_dl import YoutubeDL
    options = {
    'default_search': 'ytsearch2',
    'quiet': True
    }
    ydl = YoutubeDL(options)
    search_result = ydl.extract_info(c, download=False)
    
    for k, videos in enumerate(search_result['entries']):
        print(k+1,"Tên", videos['title'], ", id của Video ",videos['id'],", upload bởi", videos['uploader'])
    d= input("Do you want to download ?(Y/N) ").upper()
    e= int(input("The number of the song: ")) - 1
    if d == "Y":
        options = {}
        ydl = YoutubeDL(options)
        print(search_result["entries"][e]['webpage_url'])
        ydl.download([search_result["entries"][e]['webpage_url']])
        print()
    if d=="N":
        print("")
    