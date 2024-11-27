# pip install pytubefix
from pytubefix import YouTube
from datetime import datetime
source_url = input("URL:")

extractYB = YouTube(source_url)
video_stream = extractYB.streams.get_highest_resolution()
destination_path = 'videos' # Destination
currtime = datetime.today()
filename = str(currtime.hour) + str(currtime.minute) + str(currtime.second) + '.mp4'
video_stream.download(output_path=destination_path, filename=filename)
video_size_bytes = video_stream.filesize
video_duration_seconds = extractYB.length