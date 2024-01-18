#for __pytube__ library you have to use this command on your teminal
#$ pip install pytube
#The you should close the editor and reopen for the script to work

from pytube import YouTube

#This method creates on the terminal a text that shows the progres of the download
def on_progress(stream, chunk, remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - remaining

    percent = (bytes_downloaded / total_size) * 100
    print(f"Downloading... {percent:.2f}% completed", end='\r', flush=True)

#This is the main method. This method downloads the video form yotube  in 720p .mp4
def download_video(url, destination_path):
    try:
        video = YouTube(url, on_progress_callback=on_progress)
        stream = video.streams.filter(file_extension="mp4").first()

        if stream:
            stream.download(output_path=destination_path)
            print("\nDownload completed at:", destination_path)
        else:
            print("No available video stream found for", url)

    except Exception as e:
        print("\nError:", str(e))

#This takes the url of the video that is writen on the .txt file so you can download
#more than 1 video erevy time you need to download something
def download_videos_from_file(file_path, destination_path):
    with open(file_path, 'r') as file:
        for line in file:
            url = line.strip()
            if url:
                download_video(url, destination_path)

if __name__ == "__main__":
    #Change the route of your folder where you want the files to download
    #It is important that you use this character " / " instead of " \ "
    #Just replace them
    url_file_path = "route/of/the/txt"
    destination_path = "route/of/the/folder"

    download_videos_from_file(url_file_path, destination_path)
