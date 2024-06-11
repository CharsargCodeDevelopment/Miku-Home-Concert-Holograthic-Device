from pytube import YouTube

def download_youtube_video(url, download_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f'Downloading: {yt.title}')
        stream.download(output_path=download_path)
        print(f'Download completed: {yt.title}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    # URL of the YouTube video to be downloaded
    youtube_url = input("Enter the URL of the YouTube video: ")
    
    # Path where the video will be saved
    download_path = input("Enter the download path (leave empty for current directory): ")
    if not download_path:
        download_path = '.'

    # Download the video
    download_youtube_video(youtube_url, download_path)
