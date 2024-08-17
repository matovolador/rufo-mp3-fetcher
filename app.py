import os, sys
from soundspider import SoundSpider
from time import sleep
import threading
import tkinter as tk

the_menu = False

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def destroy(self):
			try:
				download_thread.quit()
			except:
				pass
			self.destroy()

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

		self.url_entry.bind_class("Entry", "<Button-3><ButtonRelease-3>", self.show_menu)
		self.dir_entry.bind_class("Entry", "<Button-3><ButtonRelease-3>", self.show_menu)

        self.download_thread = threading.Thread(
            target=SoundSpider.convert, args=params)
        self.download_thread.start()

	def make_menu(self,w):
		global the_menu
		the_menu = tk.Menu(w, tearoff=0)
		the_menu.add_command(label="Cut")
		the_menu.add_command(label="Copy")
		the_menu.add_command(label="Paste")

	def show_menu(self,e):
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
app.master.maxsize(400, 200)
app.master.geometry("400x200")
app.mainloop()