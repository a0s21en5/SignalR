from pytube import YouTube

link = input("Enter Here What You Download: ")
youtube_1 = YouTube(link)

print(youtube_1.title)
