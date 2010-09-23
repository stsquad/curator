#!/usr/bin/python
#
# Represents a set of photos as stored on the Flickr photo sharing site

import sys
import re

from photo_set import photo_set
from photo import photo
from cache import cache

# For flickrapi
from xml.etree.ElementTree import ElementTree
import flickrapi

verbose=True

#Secret: e377d23130b29828
flickr_api_app_id="aveh_wzV34EyLrQovnSYnRxAUZPisqj30BJGWhoLfqSDIQ75nW4VvspQm1cbGaoelwE-"
flickr_api_keys="2e99f9f42e759029f540360a36647abd"
flickr = flickrapi.FlickrAPI(flickr_api_keys)


class flickr_set(photo_set):
    """
    A photoset that lives on the Flickr photo sharing site
    """

    # set from flickr queries
    info=None
    title=None
    set_size=0

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
        '12345678'
        >>> print x
        Flickr based Photoset: http://www.flickr.com/photos/someone/sets/12345678/with/10111213 (0 photos)
        """
        super(self.__class__, self).__init__(uri)

        m = re.search("(set-|sets\/)([0-9]{1,})", uri);
        pset=m.group(2)
        if pset:
            self.flickr_setid=pset
            self.cache = cache("flickr_"+str(self.flickr_setid))
            ps_info=self._getInfo()
            if ps_info:
                # extract info from Photo Set
                ps=ps_info.find("photoset")
                self.set_size=ps.attrib['photos']
                self.title=ps.find("title").text
                self.desc=ps.find("description").text
        else:
            print "flickr_set: unable to extract set ID from URI:"+uri

    def _getInfo(self):
        """
        Get basic information about the Flickr Set
        """
        self.info=None
        try:
            info=flickr.photosets_getInfo(photoset_id=self.flickr_setid)
            self.info=ElementTree(info)
            self.cache.save_xml("getInfo", etree)
        except IOError:
            # most likey can't talk to net, try the cache
            self.info = self.cache.load_xml("getInfo")
        except:
            print "flickr_set: Unhandled exception ", sys.exc_type
            raise sys.exc_type

        return self.info
        

    def __str__(self):
        """
        Print a string representation of the set
        """
        string="Flickr based Photoset"
        if self.title:
            string=string+" '"+self.title+"'"
        string=string+": "+self.uri+" ("
        if self.set_size:
            string=string+self.set_size+"/"
        string=string+str(len(self.photos))+" photos)"
        return string

# Unit Tests
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1 and not sys.argv[1].startswith("-v"):
        for a in sys.argv[1:]:
            print "Creating flickr_set: "+a
            pset = flickr_set(a)
            if pset:
                print "  created:"+str(pset)
            else:
                print "  nothing created"
    else:
        import doctest
        doctest.testmod()    

