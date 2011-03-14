#!/usr/bin/python
#
# Handle the GUI for curator
#

from threading import Thread, Event
import pygtk
import gtk,gobject
pygtk.require("2.0") 


def store_set_info(pset):
    """
    From a photo set store stuff in the GUI model
    
    Returns a tupple that will be appeneded to the model

    >>> x=GUI()
    """

    item = []

    # name
    item.append(pset.get_album_name())

    #icon
    pb = gtk.gdk.pixbuf_new_from_file(pset.get_icon_file())
    item.append(pb)

    print "store_set_info made: " + str(item)
    return item

def store_photo_info(photo):
    item = []
    fn = photo.get_icon_file_name()
    print "  adding photo: %s" % (fn)
 #   item.append(fn)

    pb = gtk.gdk.pixbuf_new_from_file(fn)
    item.append(pb)

    print "store_photo_info made: " + str(item)
    return item


class GUI(object):
  def __init__(self, basepath=None, sets=None):
      builder = gtk.Builder()

      glade_file = "ui/gtk/gtk_interface.glade"
      if basepath:
          glade_file = basepath+"/"+glade_file

      builder.add_from_file(glade_file)
      
      builder.connect_signals(self)
      self.window1 = builder.get_object("window1")
      self.window1.show()

      self.set_icons = builder.get_object("set_icons")
      self.set_icons.set_text_column(0)
      self.set_icons.set_pixbuf_column(1)

      # populate the set icons
      self.setlist_store = builder.get_object("setlist_store")
      if sets:
          for s in sets:
              print "Adding: %s to model" % (s)
              self.setlist_store.append(store_set_info(s))

      # And now the main display
      self.photo_icons = builder.get_object("photo_icons")
      self.photo_icons.set_pixbuf_column(0)
      self.photolist_store = builder.get_object("photolist_store")

      # Spawn some background threads
      self.end_event = Event()
      self.end_event.clear()
      self.preview_thread = Thread(target=self.populate_preview, args=(sets,)).start()

  def populate_preview(self, sets):
      for s in sets:
          for p in s.photos:
              if self.end_event.is_set():
                  print "caught a termination event"
              else:
                  info = store_photo_info(p)
                  gobject.idle_add(self.add_preview_icon, info)

  # Run in the GTK context
  def add_preview_icon(self, info):
      print "add_preview_icon: tick"
      self.photolist_store.append(info)
              
          
              
  def shutdown_gui(self):
      print "shutdown_gui"
      self.end_event.set()
      print "current threads: "+str(Threading.enumerate())
      

  def on_window1_destroy(self,widget,data=None):
      shutdown_gui()
      
  def on_button1_clicked(self,widget,data=None):
      shutdown_gui()

  def on_quit_clicked(self,widget,data=None):
      print "quit!"
      shutdown_gui()

  def on_open_clicked(self,widget,data=None):
      print "file open"

def start_gui(basepath=None, sets=None):
    gtk.gdk.threads_init()
    
    return GUI(basepath, sets)

if __name__ == "__main__":
    start_gui()
    gtk.main()
