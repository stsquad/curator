#!/usr/bin/python
#
# Curator
#
# A photo album creator and slurper with an emphasis on maintaining
# decent meta-data for well atributed final output.
#
#

import sys,os
import getopt

from controller import controller

# For verbosity
verbose=False
verbose_level=0

# GUI
gui_mode="clutter"

me=os.path.basename(sys.argv[0])
gui=None


def usage():
    print "Usage:"
    print "  " + me + " [options] [uri1 [uri2 [uri3...]]]"
    print "  -h, --help:   Display usage test"
    print "  -v, -verbose: Be verbose in output"


def start_curator(args):
    # We need a controller
    control = controller(verbose=(verbose_level>1))
    
    # Lets create a set of sets
    if len(args)>0:
        for uri in args:
            control.add_set_by_uri(uri)

    # We have sets to deal with now
    if verbose:
        print "Project using %d photo sets" % (control.get_set_count())

    cwd = os.getcwd()
    if os.path.dirname(sys.argv[0]) == cwd:
        bp=cwd+"/../"
    else:
        bp=cwd

    sys.path.append(bp+"/ui/"+gui_mode)
    from gui import start_gui
    gui = start_gui(verbose=(verbose_level>1), basepath=bp, controller=control)
    gui.run()
    

# Start of code
if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvgc", ["help", "verbose", "gtk", "clutter"])
    except getopt.GetoptError, err:
        usage()
        exit (-1)
        
    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
            exit
        if o in ("-v", "--verbose"):
            verbose=True
            verbose_level += 1
        if o in ("-g", "--gtk"):
            gui_mode="gtk"
        if o in ("-c", "--clutter"):
            gui_mode="clutter"

    start_curator(args)

