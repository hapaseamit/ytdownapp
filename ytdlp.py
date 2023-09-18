"""
Youtube video downloader program.
"""
import os

import yt_dlp


def get_video_formats(url):
    """Getting video formats"""
    ydl = yt_dlp.YoutubeDL()

    info = ydl.extract_info(url, download=False)

    formats = info["formats"]

    for index, video_format in enumerate(formats):
        format_note = video_format.get("format_note", "Unknown")
        ext = video_format.get("ext", "Unknown")
        if format_note != "Unknown" and ext == "mp4":
            print(f"{index + 1}. {format_note} - {ext}")

    # Ask user to select a format
    format_choice = input("Enter the number corresponding to the desired format: ")

    # Validate and return the chosen format
    if format_choice.isnumeric() and 1 <= int(format_choice) <= len(formats):
        chosen_format = formats[int(format_choice) - 1]
        return chosen_format
    print("Invalid format choice.")
    return None


def download_youtube_video(url):
    """Downloading video."""
    chosen_format = get_video_formats(url)

    if chosen_format is not None:
        # Create YT-DLP downloader object
        ydl = yt_dlp.YoutubeDL()

        # Set download options
        video_options = {
            "format": chosen_format["format_id"],
            "keepvideo": True,
            # Output filename template
            "outtmpl": "~/storage/download/%(title)s.%(ext)s",
        }

        # Download the YouTube video
        with yt_dlp.YoutubeDL(video_options) as ydl:
            video_info = ydl.extract_info(url, download=True)
            video_filename = ydl.prepare_filename(video_info)

        # Set download options for audio
        audio_options = {
            "format": "bestaudio/best",
            # Output audio filename template
            "outtmpl": "~/storage/download/%(title)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

        # Download the YouTube audio
        with yt_dlp.YoutubeDL(audio_options) as ydl:
            audio_info = ydl.extract_info(url, download=True)
            audio_filename = ydl.prepare_filename(audio_info)

        # Merge video and audio using FFmpeg
        merged_filename = f"{video_filename[:-4]}_merged.mp4"
        video_bitrate = "2000k"
        merge_command = f'ffmpeg -i "{video_filename}" -i "{audio_filename}" -c:v copy -b:v {video_bitrate} -c:a copy "{merged_filename}"'
        os.system(merge_command)

        print("Video and audio merged successfully!")


if __name__ == "__main__":
    video_url = input("Enter video link: ")
    download_youtube_video(video_url)
