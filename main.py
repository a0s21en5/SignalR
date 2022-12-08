from pytube import YouTube

link = input("Enter Here What You Download: ")
data = YouTube(link)

# Title
# print(data.title)
# Thumbnail
# print(data.thumbnail_url)

videos = data.streams.all()

vid = list(enumerate(videos))

for i in vid:
    print(i)

print()
strm = int(input("Enter :"))
videos[strm].download()
print("Successfully Downloaded Video")
