#!/usr/bin/python
#
# Represents a set of photos as stored on the Facebooks photo pages

import sys
import re

from photo_set import photo_set
from photo import photo

# For Facebook API
from facebook import Facebook

# TODO: get some proper keys
fb_api_key = "e1e9cfeb5e0d7a52e4fbd5d09e1b873e"
fb_secret_key = "1bebae7283f5b79aaf9b851addd55b90"

facebook = Facebook(fb_api_key, fb_secret_key)

# We only want to authenticate once, but only if actually are importing
# a Facebook album
authenticated=False

def do_facebook_login():
    if not authenticated:
        print "TODO...."

class facebook_set(photo_set):
    """
    A photoset that lives on Facebook
    """

    def __new__(cls, uri):
        """
        Creates a set object for a Facebook URI.

        Object creation does not care if it can contact Facebook, just that
        the URI is a valid one.
        >>> x=facebook_set("/usr/share/images/desktop-base/")
        >>> x==None
        True
        >>> x=facebook_set("http://www.facebook.com/album.php?aid=259915&id=699881489")
        >>> x==None
        False
        """
        if re.match("http://www.facebook.com", uri):
            obj = super(facebook_set, cls).__new__(cls)
            return obj
        else:
            return None

    def __init__(self, uri, recurse=False):
        """
        Initialise the photo set from the Facebook web-site

        As we may not be connected to the web we might work directly from
        cached thumbnails/images.

        >>> x=facebook_set("http://www.facebook.com/album.php?aid=259915&id=699881489")
        >>> x.fb_aid
        259915
        >>> print x
        Facebook based Photoset: http://www.facebook.com/album.php?aid=259915&id=699881489 (0 photos)
        """
        super(self.__class__, self).__init__(uri)

        m = re.search("(aid=)([0-9]{1,})", uri);
        pset = int(m.group(2))
        if pset:
            self.fb_aid=pset
            self.fetched=False
            try:
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
        return "Facebook based Photoset: %s (%d photos)" % (self.uri, len(self.photos))

# Unit Tests
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1 and not sys.argv[1].startswith("-v"):
        for a in sys.argv[1:]:
            print "Creating facebook_set: "+a
            pset = file_set(a)
            if pset:
                print "  created:"+str(pset)
            else:
                print "  nothing created"
    else:
        import doctest
        doctest.testmod()    
