import yt_dlp as youtube_dl
import os
import traceback
from datetime import datetime
from pydub import effects, AudioSegment
import glob
import argparse


class SoundSpider():
    @staticmethod
    def convert(url, extra_path, verbose, normalize):
        # Clean errors.txt
        with open('errors.txt', 'w') as f:
            f.write('')

        sub_path = ''
        if extra_path:
            sub_path = extra_path.replace("/", "").replace('"', "").replace("'", "") + "/"

        download_path = os.path.join(os.path.dirname(__file__), "downloads", sub_path)
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        def progress_hook(d):
            if d['status'] == 'downloading':
                print(f"Downloading: {d['_percent_str']} - {d['_eta_str']} remaining")
            elif d['status'] == 'finished':
                print("Download finished, processing...")

        options = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'audioquality': '0',
            'ignoreerrors': True,
            'outtmpl': os.path.join("downloads", sub_path, '%(playlist_index)s - %(title)s.%(ext)s'),
            'noplaylist': False,
            'verbose': verbose,
            'nocheckcertificate': True,
            'output': download_path,
            'geobypass': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '0'
            }],
            "minsleepinterval": 5,
            "maxsleepinterval": 10,
            'progress_hooks': [progress_hook],
        }

        try:
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([url])

            if normalize:
                print("Normalizing audio. Please wait...")
                files = glob.glob(os.path.join("downloads", sub_path, "*.mp3"))
                print(f"Normalizing {len(files)} audio files...")

                for idx, f in enumerate(files):
                    print(f"Normalizing file {idx+1}/{len(files)}: {f}")
                    _sound = AudioSegment.from_file(f, "mp3")
                    sound = effects.normalize(_sound)
                    sound.export(f, format="mp3")
                    print(f"Finished normalizing file {idx+1}/{len(files)}: {f}")

            print("All done!")
            return True
        except Exception as e:
            with open('errors.txt', 'w') as f:
                f.write(str(datetime.now()) + ": " +
                        str(e) + "\n" + traceback.format_exc())
            print("Error downloading file(s). Check errors.txt for details.")
            return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and optionally normalize audio from a YouTube URL.")
    parser.add_argument("url", help="YouTube video or playlist URL")
    parser.add_argument("-p", "--path", default="", help="Optional subfolder path under downloads/")
    parser.add_argument("-n", "--normalize", action="store_true", help="Normalize audio volume")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()

    SoundSpider.convert(
        url=args.url,
        extra_path=args.path,
        verbose=args.verbose,
        normalize=args.normalize
    )