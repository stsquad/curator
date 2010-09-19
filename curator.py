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
from set_factory import create_set

verbose=0
me=os.path.basename(sys.argv[0])

all_photosets=[]

def usage():
    print "Usage:"
    print "  " + me + " [options] [uri1 [uri2 [uri3...]]]"
    print "  -h, --help:   Display usage test"
    print "  -v, -verbose: Be verbose in output"

# Start of code
if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv", ["help", "verbose"])
    except getopt.GetoptError, err:
        usage()
        
    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
            exit
        if o in ("-v", "--verbose"):
            verbose=1
        # TODO: handle project saving/loading


    # Lets create a set of sets
    if len(args)>0:
        for uri in args:
            pset=create_set(uri)
            if pset:
                if verbose:
                    print "Created: "+str(pset)
                all_photosets.append(pset)

    # We have sets to deal with now
    if verbose:
        print "Project using %d photo sets" % (len(all_photosets))
        

