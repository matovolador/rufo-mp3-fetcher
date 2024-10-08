import yt_dlp as youtube_dl
import os
import traceback
from datetime import datetime
from pydub import effects, AudioSegment
import glob
import tkinter as tk


class SoundSpider():
    @staticmethod
    def convert(url_entry, extra_path_entry, verbose, label_object, button_object, url_label, folder_label, normalize):
        url = url_entry.get()
        extra_path = extra_path_entry.get()

        # Clean errors.txt
        with open('errors.txt', 'w') as f:
            f.write('')

        sub_path = ''  # folder name. optional. this goes inside downloads/
        if extra_path:
            sub_path = extra_path.replace(
                "/", "").replace('"', "").replace("'", "") + "/"
        download_path = os.path.join(
            os.path.dirname(__file__), "downloads/" + sub_path)
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Progress hook to update the label
        def progress_hook(d):
            if d['status'] == 'downloading':
                label_object['text'] = f"Downloading: {d['_percent_str']} - {d['_eta_str']} remaining"
            elif d['status'] == 'finished':
                label_object['text'] = "Download finished, processing..."

        options = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'audioquality': '0',
            'ignoreerrors': True,
            # name the file the ID of the video
            'outtmpl': 'downloads/' + sub_path + u'%(playlist_index)s - %(title)s.%(ext)s',
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
            "minsleepinterval": "5",
            "maxsleepinterval": "10",
            'progress_hooks': [progress_hook],  # Add the progress hook here
        }

        try:
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([url])

            if normalize:
                label_object["text"] = "Normalizing audio. Please wait..."
                files = glob.glob("./downloads/" + sub_path + "*.mp3")
                print(f"Normalizing {len(files)} audio files...")

                for idx, f in enumerate(files):
                    print(f"Normalizing file {idx+1}/{len(files)}: {f}")
                    _sound = AudioSegment.from_file(f, "mp3")
                    sound = effects.normalize(_sound)
                    sound.export(f, format="mp3")
                    print(
                        f"Finished normalizing file {idx+1}/{len(files)}: {f}")

            print("Normalization process completed.")

            # Update UI
            label_object["text"] = "Done!"
            button_object['state'] = "normal"
            folder_label['state'] = "normal"
            url_label['state'] = "normal"
            # url_entry.delete(0, tk.END)
            # extra_path_entry.delete(0, tk.END)
            return True
        except Exception as e:
            with open('errors.txt', 'w') as f:
                f.write(str(datetime.now()) + ": " +
                        str(e) + "\n" + traceback.format_exc())

            # Update UI
            label_object['text'] = "Error downloading file(s).\nPlease check errors.txt file for more information."
            button_object["state"] = "normal"
            folder_label['state'] = "normal"
            url_label['state'] = "normal"
            # url_entry.delete(0, tk.END)
            # extra_path_entry.delete(0, tk.END)
            return False
