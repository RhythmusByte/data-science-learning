from yt_dlp import YoutubeDL

URL = input('Enter the url: ').strip()

ydl_opts = {
    'outtmpl': '/data/data/com.termux/files/home/storage/shared/Download/%(title)s.%(ext)s'
}

with YoutubeDL(ydl_opts) as ydl:
    try:
        ydl.download([URL])
    except Exception as e:
        print(f"Download failed: {e}")
