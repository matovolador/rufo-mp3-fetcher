from __future__ import unicode_literals
import youtube_dl
import sys,os
from datetime import datetime
class SoundSpider():

    @staticmethod
    def convert(url,extra_path,verbose, label_object, button_object,url_label,folder_label):
        # Clean errors.txt
        with open('errors.txt','w') as f:
                f.write('')
                f.close()

        sub_path = ''  # folder name. optional. this goes inside downoads/
        if extra_path:
            sub_path = extra_path.replace("/","").replace('"',"").replace("'","")+"/"
        download_path = os.path.join(os.path.dirname(__file__),"downloads/"+sub_path)
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        options = {
            'format':'bestaudio/best',
            'extractaudio':True,
            'audioformat':'mp3',
            "audioquality":"0",
            'ignoreerrors':True,
            'outtmpl': 'downloads/'+sub_path+u'%(title)s.%(ext)s',     #name the file the ID of the video
            'noplaylist':False,
            'verbose': verbose,
            'nocheckcertificate':True,
            'output': download_path,
            'geobypass': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '0'
            }],
            "minsleepinterval":"5",
            "maxsleepinterval": "10"
        }
        try:
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([url])
                
            if normalize:
                # get files again since they have new names:
                files = glob.glob("./downloads/"+sub_path+"*.mp3")
                print("Normalizing audio...")
                for f in files:
                    _sound = AudioSegment.from_file(f, "mp3")  
                    sound = effects.normalize(_sound)  
                    sound.export(f, format="mp3")
            print("Done")

            # do this crap while i implement a callback to Threading (cant be arsed to be honest)
            label_object.set_text("Done!")
            button_object.set_sensitive(True)
            folder_label.set_sensitive(True)
            url_label.set_sensitive(True)
            folder_label.set_text('')
            url_label.set_text('')
            return True
        except Exception as e:
            with open('errors.txt','w') as f:
                f.write(str(datetime.now())+ ": " +str(e))
                f.close()

            # do this crap while i implement a callback to Threading (cant be arsed to be honest)
            label_object.set_text("Error downloading file(s).\nPlease check errors.txt file for more information.")
            button_object.set_sensitive(True)
            folder_label.set_sensitive(True)
            url_label.set_sensitive(True)
            folder_label.set_text('')
            url_label.set_text('')
            return False
