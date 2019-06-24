import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os, sys
from soundspider import SoundSpider
from time import sleep
import threading

class Handler:
	def onDestroy(self, *args):
		try:
			download_thread._stop()
		except:
			pass
		Gtk.main_quit()

	def onToggleDownload(self, button):
		status = "Downloading..."
		builder.get_object('label4').set_text(status)
		button.set_sensitive(False)
		builder.get_object("folder_label").set_sensitive(False)
		builder.get_object("url_label").set_sensitive(False)
		## verbose?
		verbose = True
		# verbose = False
		params = (builder.get_object("url_label").get_text(),builder.get_object("folder_label").get_text(),verbose, builder.get_object('label4'), button,builder.get_object("url_label"),builder.get_object("folder_label"))
		download_thread = threading.Thread(target=SoundSpider.convert, args=params)
		download_thread.start()
		return

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
	# """ Get absolute path to resource, works for dev and for PyInstaller """
	# base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
	# return os.path.join(base_path, relative_path)

download_thread = threading.Thread()

builder = Gtk.Builder()
builder.add_from_file(resource_path("ui.glade"))
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()