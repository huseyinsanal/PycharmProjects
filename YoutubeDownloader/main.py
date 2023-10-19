import pytube

url = input("enter video url: ")

path = "D:\YoutubeDownloader Videos"

pytube.YouTube(url).streams.get_highest_resolution().download(path)
