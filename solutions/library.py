from pathlib import Path
import yt_dlp
import csv

def download_video(url):
    ydl_options = {
        "outtmpl": "videos/%(title)s.%(ext)s",
        "socket_timeout": 30,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            ydl.download([url])

        return {
            "url": url,
            "status": "success",
            "error": "",
        }

    except Exception as error:
        return {
            "url": url,
            "status": "failed",
            "error": str(error),
        }
        
def download_video_semaphore(url, semaphore):
    ydl_options = {
        "outtmpl": "videos/%(title)s.%(ext)s",
        "socket_timeout": 30,
    }

    with semaphore:
        try:
            with yt_dlp.YoutubeDL(ydl_options) as ydl:
                ydl.download([url])

            return {
                "url": url,
                "status": "success",
                "error": "",
            }

        except Exception as error:
            return {
                "url": url,
                "status": "failed",
                "error": str(error),
            }

def read_video_urls(csv_path):
    urls = []
    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            urls.append(row["url"])
    return urls

def get_video_metadata(url):

    metadata = {}
    ydl_options = {
    "quiet": True,
    "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        info = ydl.extract_info(url, download=False)

        metadata["title"] = info.get("title")
        metadata["duration"] = info.get("duration")
        metadata["uploader"] = info.get("uploader")
        metadata["view_count"] = info.get("view_count")
        metadata["ext"] = info.get("ext")
        metadata["url"] = url

    return metadata