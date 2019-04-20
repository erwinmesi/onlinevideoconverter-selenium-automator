from online_video_converter_downloader import OnlineVideoConverterDownloader
from chrome_downloads import ChromeDownloads
import csv

def get_video_links():
    with open('videos.csv') as file:
        reader = csv.reader(file)
        return [row[0] for row in reader]

for link in get_video_links():
    OnlineVideoConverterDownloader().download(link)