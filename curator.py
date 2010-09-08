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
import re
import xml.etree.ElementTree

import flickrapi

me=os.path.basename(sys.argv[0])

#Secret: e377d23130b29828
flickr_api_app_id="aveh_wzV34EyLrQovnSYnRxAUZPisqj30BJGWhoLfqSDIQ75nW4VvspQm1cbGaoelwE-"
flickr_api_keys="2e99f9f42e759029f540360a36647abd"
#flickr_api_keys=0x2e99f9f42e759029f540360a36647abd
flickr = flickrapi.FlickrAPI(flickr_api_keys)

def usage():
    print "Usage:"
    print "  " + me + " [options] filename"
    print "  -h, --help:   Display usage test"
    print "  -v, -verbose: Be verbose in output"

# Start of code
if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:", ["help", "verbose", "flickr="])
    except getopt.GetoptError, err:
        usage()
        

    create_log=None

    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
            exit
        if o in ("-v", "--verbose"):
            verbose=1
        if o in ("-f", "--flickr"):
            m = re.search("(set-|sets\/)([0-9]{1,})", a);
            pset = m.group(2)
            if pset:
                print "Fetching set:"+pset
                sets = flickr.photosets_getInfo(photoset_id=pset)
                xml.etree.ElementTree.dump(sets)
        

