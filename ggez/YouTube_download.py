from pytube import YouTube
DOWNLOAD_FOLDER = "/Users/EL HUDA"
video_url ="https://www.youtube.com/watch?v=Cd8jlnmuMnI&list=PLny0NV_uoNSbYLSdaLRUOxA4yiC9cyeQa&index=16"
video_obj = YouTube (video_url)
stream = video_obj.streams.get_highest_resolution()
stream.download (DOWNLOAD_FOLDER)