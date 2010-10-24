#!/usr/bin/python
#
# Handle the GUI for curator
#

import pygtk
import gtk
pygtk.require("2.0") 


def store_set_info(pset):
    """
    From a photo set store stuff in the GUI model
    
    Returns a tupple that will be appeneded to the model

    >>> x=GUI()
    """

    item = []

    # name
    item.append(pset.__str__())

    #icon
    pb = gtk.gdk.pixbuf_new_from_file(pset.get_icon_file())
    item.append(pb)

    print "store_set_info made: " % (item)

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
#      self.set_icons.set_pixbuf_column(1)
#      self.set_icons.set_markup_column(2)

      self.setlist_store = builder.get_object("setlist_store")

      # populate the set icons
      if sets:
          for s in sets:
              print "Adding: %s to model" % (s)
              self.setlist_store.append(store_set_info(s))


              
              

  def on_window1_destroy(self,widget,data=None):
      gtk.main_quit()

  def on_button1_clicked(self,widget,data=None):
      gtk.main_quit()  

def start_gui(basepath=None, sets=None):
    return GUI(basepath, sets)

if __name__ == "__main__":
    start_gui()
    gtk.main()
