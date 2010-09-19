#!/usr/bin/python
#
# Factory to create an set objects
#

import photo_set
from file_set import file_set
from flickr_set import flickr_set
from facebook_set import facebook_set

def create_set(uri):
    """
    Run through the available set types until one works with the passed URI.

    When adding new set types they will need to be added to the factory
    """
    for set_type in [file_set, flickr_set, facebook_set]:
        pset=set_type(uri)
        if pset:
            return pset

    print "Unable to create a set for URI:"+uri
    

    
