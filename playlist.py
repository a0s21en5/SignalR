from pytube import Playlist

py = Playlist("Enter Here What You Download: ")

print(f'Downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()
