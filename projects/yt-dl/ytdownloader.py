from yt_dlp import YoutubeDL

BASE_OPTS = {
    'quiet': True,
    'no_warnings': True,
    'noprogress': True,
}

# https://youtu.be/xy3AcmW0lrQ

def get_url():
    return input("Enter the url: ")

def get_metadata(url):
    with YoutubeDL(BASE_OPTS) as ydl:
        info = ydl.extract_info(url, download=False)
        return info

def format_choice():
    choice = input('Type (v) for video and (a) for audio: ').lower()
    return 'video' if choice == 'v' else 'audio'

def show_formats(info, media_type):
    print("\nAvailable formats:")
    for f in info['formats']:
        if media_type == 'video' and f.get('vcodec') != 'none':
            print(f"- {f.get('format_id')} | {f.get('ext')} | {f.get('resolution')}")
        if media_type == 'audio' and f.get('vcodec') == 'none':
            print(f"- {f.get('format_id')} | {f.get('ext')} | audio only")

def build_opts(info, media_type):
    if media_type == 'video':
        return {
            **BASE_OPTS,
            'format': 'bestvideo*[height<=480]+bestaudio/best[height<=480]',
            'outtmpl': '%(title)s.%(ext)s',
            'merge_output_format': 'mp4',   
        }
    else:
        return {
            **BASE_OPTS,
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

def downloader(url, opts):
    with YoutubeDL(opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    print('\n\tYoutube Downloader\n')
    url = get_url()
    info = get_metadata(url)

    title = info.get('title', 'Unknown title')
    channel = info.get('uploader', 'Unknown channel')

    print(f'\nTitle: {title}')
    print(f'Channel: {channel}')

    print('\nPlease select the format you want.')
    media_type = format_choice()

    print()
    show_formats(info, media_type)

    opts = build_opts(info, media_type)
    downloader(url, opts)
    print('Download Completed..')

