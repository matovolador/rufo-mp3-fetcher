import os
import sys
from soundspider import SoundSpider
from time import sleep
import threading
import signal
import sys
import tkinter as tk


def signal_handler(sig, frame):
    print('Exiting application...')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

the_menu = False


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.download_thread = None
        self.create_widgets()

    def custom_destroy(self):
        try:
            self.download_thread.quit()  # This might cause issues if not properly defined
        except:
            pass
        self.master.destroy()  # Properly destroy the Tkinter window

    def create_widgets(self):
        self.label_title = tk.Label(
            self, text="Download Youtube Urls to MP3.\nYou can also download playlists!")
        self.label_title.pack(side="top")
        self.downloadBtn = tk.Button(
            self, text="Download", command=self.onToggleDownload)
        self.downloadBtn.pack(side="bottom")
        self.url_label = tk.Label(self, text="Enter Youtube URL:")
        self.url_label.pack(side="top")
        self.url_entry = tk.Entry(self)
        self.url_entry.pack(side="top")
        self.dir_label = tk.Label(self, text="Enter download subfolder:")
        self.dir_label.pack(side="top")
        self.dir_entry = tk.Entry(self)
        self.dir_entry.pack(side="top")
        self.status_label = tk.Label(self, text="")
        self.status_label.pack(side="bottom")

        self.url_entry.bind_class(
            "Entry", "<Button-3><ButtonRelease-3>", self.show_menu)
        self.dir_entry.bind_class(
            "Entry", "<Button-3><ButtonRelease-3>", self.show_menu)

    def onToggleDownload(self):
        status = "Downloading..."
        self.status_label['text'] = status
        self.downloadBtn['state'] = "disabled"
        self.dir_entry['state'] = "disabled"
        self.url_entry['state'] = "disabled"
        # verbose?
        # verbose = True
        verbose = False
        params = (self.url_entry, self.dir_entry, verbose, self.status_label,
                  self.downloadBtn, self.url_entry, self.dir_entry, True)
        self.download_thread = threading.Thread(
            target=SoundSpider.convert, args=params)
        self.download_thread.start()
        return

    def make_menu(self, w):
        global the_menu
        the_menu = tk.Menu(w, tearoff=0)
        the_menu.add_command(label="Cut")
        the_menu.add_command(label="Copy")
        the_menu.add_command(label="Paste")

    def show_menu(self, e):
        w = e.widget
        the_menu.entryconfigure("Cut",
                                command=lambda: w.event_generate("<<Cut>>"))
        the_menu.entryconfigure("Copy",
                                command=lambda: w.event_generate("<<Copy>>"))
        the_menu.entryconfigure("Paste",
                                command=lambda: w.event_generate("<<Paste>>"))
        the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)


root = tk.Tk()
app = Application(master=root)
app.make_menu(root)
app.master.title("RUFO MP3 FETCHER")
app.master.maxsize(800, 200)
app.master.geometry("800x200")

# Bind the custom destroy method to the window close button
app.master.protocol("WM_DELETE_WINDOW", app.custom_destroy)

app.mainloop()
