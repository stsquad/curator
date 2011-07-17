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
        
        
        #create a clutter stage
        self.stage = clutter.Stage()
        #set the stage size in x,y pixels
        self.stage.set_size(500,200)
        #define some clutter colors in rgbo (red,green,blue,opacity)
        color_black =clutter.Color(0,0,0,255) 
        color_green =clutter.Color(0,255,0,255)
        color_blue =clutter.Color(0,0,255,255)
        #set the clutter stages bg color to our black
        self.stage.set_color(color_black)
        #we will need to check on the key presses from the user
        self.stage.connect('key-press-event', self.parseKeyPress)
        #create a clutter label, is there documentation for creating a clutterlabel?
        self.label = clutter.Label()
        #set the labels font
        self.label.set_font_name('Mono 32')
        #add some text to the label
        self.label.set_text("Hello")
        #make the label green
        self.label.set_color(color_green )
        #put the label in the center of the stage
        (label_width, label_height) = self.label.get_size()
        label_x = (self.stage.get_width()/2) - label_width/2
        label_y = (self.stage.get_height()/2) - label_height/2
        self.label.set_position(label_x, label_y)
        #make a second label similar to the first label
        self.label2 = clutter.Label()
        self.label2.set_font_name('Mono 32')
        self.label2.set_text("World!")
        self.label2.set_color(color_blue )
        (label2_width, label2_height) = self.label2.get_size()
        label2_x = (self.stage.get_width()/2) - label2_width/2
        label2_y = (self.stage.get_height()/2) - label2_height/2
        self.label2.set_position(label2_x, label2_y)
        #hide the label2 
        self.label2.set_opacity(0)
        #create a timeline for the animations that are going to happen
        self.timeline = clutter.Timeline(500)
        #how will the animation flow? ease in? ease out? or steady?
        #ramp_inc_func will make the animation steady
#        labelalpha = clutter.Alpha(self.timeline, clutter.ramp_inc_func)
        #make some opacity behaviours that we will apply to the labels
#        self.hideBehaviour = clutter.BehaviourOpacity(255,0x00,labelalpha)
#        self.showBehaviour = clutter.BehaviourOpacity(0x00,255,labelalpha)
        #add the items to the stage
        self.stage.add(self.label2)
        self.stage.add(self.label)
        #show all stage items and enter the clutter main loop
        self.stage.show_all()
        
    def parseKeyPress(self,actor, event):
        #do stuff when the user presses a key
        #it would be awesome if I could find some documentation regarding clutter.keysyms
        if event.keyval == clutter.keysyms.q:
            #if the user pressed "q" quit the test
            clutter.main_quit()
        elif event.keyval == clutter.keysyms.s:
            #if the user pressed "s" swap the labels
            self.swapLabels()
            
    
    def swapLabels(self):   
        #which label is at full opacity?, like the highlander, there can be only one
        if(self.label.get_opacity()>1 ):
            showing = self.label
            hidden = self.label2
        else:
            showing = self.label2
            hidden = self.label
        #detach all objects from the behaviors
        self.hideBehaviour.remove_all()
        self.showBehaviour.remove_all()
        #apply the behaviors to the labels
        self.hideBehaviour.apply(showing)
        self.showBehaviour.apply(hidden)
        #behaviours do nothing if their timelines are not running
        self.timeline.start()

    def populate_preview(self):
        sets = control.get_sets()
        for s in sets:
            for p in s.photos:
                if self.end_event.is_set():
                    print "caught a termination event"
                else:
                    print "do something here"
#                  info = store_photo_info(p)
#                  gobject.idle_add(self.add_preview_icon, info)


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
