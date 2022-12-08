from pytube import YouTube

link = input("Enter Here What You Download: ")
data = YouTube(link)

# All Format
videos = data.streams.all()

vid = list(enumerate(videos))

for i in vid:
    print(i)

print()
strm = int(input("Enter :"))
videos[strm].download()
print("Successfully Downloaded Video")
