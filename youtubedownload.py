import os
import subprocess
import sys


def run_script():
    output_dir = input("Enter location to save file [~/storage/downloads/]: ")

    if not output_dir:
        output_dir = "~/storage/downloads/"

    savepath = os.path.expanduser(output_dir)
    if not os.path.isdir(savepath):
        print("Path doesn't exist!\nExiting...")
        sys.exit()

    videourl = input("Enter video link: ")
    if not videourl:
        print("You did not enter link!\nExiting...")
        sys.exit()

    subprocess.run(
        f'yt-dlp --list-formats {videourl} | grep -E "video only|RESOLUTION"',
        shell=True,
        stdout=sys.stdout,
        stderr=sys.stderr,
        check=False,
    )

    print("Enter desired video id from above result")
    video_id = input("Enter video id: ")
    if not video_id:
        print("You did not video id!\nExiting...")
        sys.exit()

    output_filename = "%(title)s.mp4"

    outputfile_fullpath = str(os.path.join(savepath, output_filename))
    vid_format = f"{video_id}+ba"
    subprocess.run(
        [
            "yt-dlp",
            "-f",
            vid_format,
            "--merge-output-format",
            "mp4",
            "-o",
            outputfile_fullpath,
            videourl,
        ],
        stdout=sys.stdout,
        stderr=sys.stderr,
        check=False,
    )


if __name__ == "__main__":
    run_script()
