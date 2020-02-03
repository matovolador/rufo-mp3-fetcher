import os, sys
from soundspider import SoundSpider
from time import sleep
import threading
import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.label_title = tk.Label(self,text="Download Youtube Urls to MP3.\nYou can also download playlists!")
		self.label_title.pack(side="top")
		self.downloadBtn = tk.Button(self,text="Download",command=self.onToggleDownload)
		self.downloadBtn.pack(side="bottom")
		self.url_label = tk.Label(self,text="Enter Youtube URL:")
		self.url_label.pack(side="top")
		self.url_entry = tk.Entry(self)
		self.url_entry.pack(side="top")
		self.dir_label = tk.Label(self,text="Enter download subfolder:")
		self.dir_label.pack(side="top")
		self.dir_entry = tk.Entry(self)
		self.dir_entry.pack(side="top")
		self.status_label = tk.Label(self,text="")
		self.status_label.pack(side="bottom")


	def onToggleDownload(self):
		status = "Downloading..."
		self.status_label['text'] = status
		self.downloadBtn['state'] = "disabled"
		self.dir_entry['state'] = "disabled"
		self.url_entry['state'] = "disabled"
		## verbose?
		verbose = True
		# verbose = False
		params = (self.url_entry,self.dir_entry,verbose, self.status_label, self.downloadBtn,self.url_entry,self.dir_entry,True)
		download_thread = threading.Thread(target=SoundSpider.convert, args=params)
		download_thread.start()
		return

root = tk.Tk()
app = Application(master=root)
app.master.title("RUFO MP3 FETCHER")
app.master.maxsize(400, 200)
app.master.geometry("400x200")
app.mainloop()