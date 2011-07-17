#!/usr/bin/python
#
# Clutter version of the Curator GUI
#

import clutter

class image_previews(clutter.Box):
    """
    A group of image previews
    """
    current_preview = None
    current_index = 0
    total_previews = 0
    
    def __init__(self, sets):

        layout = clutter.FlowLayout(clutter.FLOW_HORIZONTAL)
        layout.set_homogeneous(False)
        layout.set_column_spacing(20)
        layout.set_row_spacing(20)

        clutter.Box.__init__(self, layout)
        self.set_color(clutter.Color(0,0,0,200))
        self.set_name('previews')
        self.set_size(-1, -1)

        for s in sets:
            icon = clutter.Texture()
            icon.set_from_file(s.get_icon_file())
            for p in s.photos:
                tex = clutter.Texture()
                tex.set_from_file(p.get_icon_file_name())
                self.add(tex)
                self.total_previews += 1

    def move_right(self):
        if self.current_preview:
            self.current_preview.set_scale(1.0, 1.0)
        if self.current_index < self.total_previews:
            self.current_index += 1
            self.current_preview = self.get_children()[self.current_index]
            self.current_preview.set_scale(3.0, 3.0)


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

        # Fill the stage with preview icons and display
        if self.control:
            sets = self.control.get_sets()
            self.previews = image_previews(sets)
            self.main_pane.add(self.previews)

        self.stage.show_all()

    def parse_keys(self, actor, event):
        #do stuff when the user presses a key
        #it would be awesome if I could find some documentation regarding clutter.keysyms
        if event.keyval == clutter.keysyms.q:
            #if the user pressed "q" quit the test
            self.shutdown_gui()
        elif event.keyval == clutter.keysyms.Right:
            self.previews.move_right()
        elif event.keyval == clutter.keysyms.Left:
            print "left"
        else:
            print "un-handled key: %d, %s" % (event.keyval, str(hex(event.keyval)))

    def on_stage_resize(self, actor, allocation, flags):
        width, height = allocation.size
        self.album_pane.set_width(100)
        self.previews.set_width(width-100)
            

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
