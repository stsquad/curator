#!/usr/bin/python
#
# Represents a set of photos as stored on the Flickr photo sharing site

import sys
import re

from photo_set import photo_set
from photo import photo

# For flickrapi
import xml.etree.ElementTree
import flickrapi

#Secret: e377d23130b29828
flickr_api_app_id="aveh_wzV34EyLrQovnSYnRxAUZPisqj30BJGWhoLfqSDIQ75nW4VvspQm1cbGaoelwE-"
flickr_api_keys="2e99f9f42e759029f540360a36647abd"
#flickr_api_keys=0x2e99f9f42e759029f540360a36647abd
flickr = flickrapi.FlickrAPI(flickr_api_keys)


class flickr_set(photo_set):
    """
    A photoset that lives on the Flickr photo sharing site
    """

    def __new__(cls, uri):
        """
        Creates a set object for a Flickr URI.

        Object creation does not care if it can contact Flickr, just that
        the URI is a valid Flickr one.
        >>> x=flickr_set("/usr/share/images/desktop-base/")
        >>> x==None
        True
        >>> x=flickr_set("http://www.flickr.com/photos/someone/sets/12345678/with/10111213")
        >>> x==None
        False
        """
        if re.match("http://www.flickr.com", uri):
            obj = super(flickr_set, cls).__new__(cls)
            return obj
        else:
            return None

    def __init__(self, uri, recurse=False):
        """
        Initialise the photo set from the flickr web-site

        As we may not be connected to the web we might work directly from
        cached thumbnails/images.

        >>> x=flickr_set("http://www.flickr.com/photos/someone/sets/12345678/with/10111213")
        >>> x.flickr_setid
        12345678
        >>> print x
        Flickr based Photoset: http://www.flickr.com/photos/someone/sets/12345678/with/10111213 (0 photos)
        """
        super(self.__class__, self).__init__(uri)

        m = re.search("(set-|sets\/)([0-9]{1,})", uri);
        pset = int(m.group(2))
        if pset:
            self.flickr_setid=pset
            self.fetched=False
            try:
                sets = flickr.photosets_getInfo(photoset_id=pset)
                self.fetched=True
            except IOError:
                # most likey can't talk to net
                pass
            except:
                print "Unhandled exception caught:", sys.exc_type

    def __str__(self):
        """
        Print a string representation of the set
        """
        return "Flickr based Photoset: %s (%d photos)" % (self.uri, len(self.photos))

# Unit Tests
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1 and not sys.argv[1].startswith("-v"):
        for a in sys.argv[1:]:
            print "Creating flickr_set: "+a
            pset = file_set(a)
            if pset:
                print "  created:"+str(pset)
            else:
                print "  nothing created"
    else:
        import doctest
        doctest.testmod()    

