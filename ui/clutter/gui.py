#!/usr/bin/python
#
# Clutter version of the Curator GUI
#

import clutter

class GUI:
    """
    Class representing the GUI
    """
    
    verbose = False
    control = None
    basepath = None
    
    def __init__(self, verbose=False, basepath=None, controller=None):
        # House keeping
        self.basepath = basepath
        self.verbose = verbose
        self.control = controller

        # Setup the Stage
        self.stage = clutter.Stage()
        self.stage.set_size(500,400)
        self.stage.set_color(clutter.Color(0,0,0,255))
        self.stage.set_user_resizable(True)

        # Setup something to handle GUI events
        self.stage.connect('destroy', self.shutdown_gui)
        self.stage.connect('key-press-event', self.parse_keys)
        self.stage.connect('allocation-changed', self.on_stage_resize)

        # Define the two panes within one layout
        system_layout = clutter.FlowLayout(clutter.FLOW_VERTICAL)
        system_layout.set_homogeneous(False)
        self.main_pane = clutter.Box(system_layout)
        self.stage.add(self.main_pane)
        
        album_layout = clutter.FlowLayout(clutter.FLOW_VERTICAL)
        album_layout.set_homogeneous(True)
        album_layout.set_column_spacing(10)
        album_layout.set_row_spacing(20)

        self.album_pane = clutter.Box(album_layout)
        self.album_pane.set_color(clutter.Color(20,20,20,200))
        self.album_pane.set_name('albums')
        self.album_pane.set_size(100, -1)
        self.main_pane.add(self.album_pane)

        preview_layout = clutter.FlowLayout(clutter.FLOW_HORIZONTAL)
        preview_layout.set_homogeneous(True)
        preview_layout.set_column_spacing(20)
        preview_layout.set_row_spacing(20)

        self.preview_pane = clutter.Box(preview_layout)
        self.preview_pane.set_color(clutter.Color(0,0,0,200))
        self.preview_pane.set_name('previews')
        self.preview_pane.set_size(-1, -1)
        self.main_pane.add(self.preview_pane)
        

        # Fill the stage with preview icons and display
        self.populate_preview()
        self.stage.show_all()
        
    def populate_preview(self):
        sets = self.control.get_sets()
        for s in sets:
            for p in s.photos:
                tex = clutter.Texture()
                tex.set_from_file(p.get_icon_file_name())
                self.preview_pane.add(tex)


    def parse_keys(self, actor, event):
        #do stuff when the user presses a key
        #it would be awesome if I could find some documentation regarding clutter.keysyms
        if event.keyval == clutter.keysyms.q:
            #if the user pressed "q" quit the test
            clutter.main_quit()

    def on_stage_resize(self, actor, allocation, flags):
        width, height = allocation.size
        self.album_pane.set_width(100)
        self.album_pane.set_height(height)
        self.preview_pane.set_width(width-100)
        self.preview_pane.set_height(height)
            

    def run(self):
        print "entering the GUI run loop"
        clutter.main()
              
    def shutdown_gui(self):
        print "shutdown_gui"
        clutter.main_quit()

def start_gui(verbose=True, basepath=None, controller=None):
    return GUI(verbose, basepath, controller)
        
if __name__=="__main__":
    test = start_gui()
