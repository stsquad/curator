#!/usr/bin/python
#
# Represents an individual photo in a set. 

import urllib2

# For flickrapi
from xml.etree.ElementTree import ElementTree

from photo import photo

class flickr_photo(photo):
    """
    Represents a photo from the flickr photo site.
    """

    def __init__(self, flickr=None, flickr_entry=None, cache=None):
        """
        """
        self.flickr = flickr
        self.flickr_entry = flickr_entry
        self.cache = cache
        id = int(flickr_entry.get("id", 0))
        super(self.__class__, self).__init__(id)

        # Set on-demmand
        self.sizes = None

    def __str__(self):
        """
        String representation of ID
        >>> xml = '<photo id="2484" secret="123456" server="1" title="my photo" isprimary="0" />'
        >>> x = flickr_photo(123)
        >>> print x.__str__()
        'flickr_123'
        """
        return str("flickr_"+str(self.id))
    
    def _getSizes(self):
        if self.sizes is None:
            try:
                self.sizes = self.flickr.photos_getSizes(photo_id=self.id)
                sizes_tree = ElementTree(self.sizes)
                self.cache.save_xml("getSizes_"+str(self.id), sizes_tree)
            except IOError:
                # most likey can't talk to net, try the cache
                sizes_tree = self.cache.load_xml("getSizes")
                self.sizes = sizes_tree.getroot()

        return self.sizes.find("sizes")
            


    def get_icon_file_name(self):
        file_name = "flickr_icon_"+str(self.id)+".jpg"
        file_path = self.cache.return_file_path(file_name)
        if file_path:
            return file_path
        else:
            print "gifn: Downloading a thumbnail to: %s" % (file_name)
            sizes = self._getSizes()

            for el in sizes:
                label = el.get('label')
                if label == "Thumbnail":
                    source = el.get('source')
                    resp = urllib2.urlopen(source)
                    return self.cache.write_file(file_name, resp.read())
                
        return None


# Unit Tests
if __name__ == "__main__":
    import doctest
    doctest.testmod()    
