# YouTube Downloader
# Downloads the highest resolution video from a YouTube link
# Usage: python ytDownloader.py <link>
# Make sure you are in the virtual environment and have pytube installed

from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()
print("Downloading...")

yd.download("./videos")
print("Done")