#!/usr/bin/python
#
# Represents an individual photo in a set. 

import urllib2
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

        try:
            print "getting id..."
            print "entry is: %s" % flickr_entry.dump()
            id = flickr_entry.find("photo/id")
            print "id is : %d" % (id)
        except:
            print "defaulting: flickr_entry = %s " % (dir(flickr_entry))
            id = int(0)

        print "flickr_photo: id is %s" % (id)
        super(self.__class__, self).__init__(id)

        if self.flickr:
            print "Getting sizes...."
            self.sizes = self.flickr.photos_getSizes(photo_id=id)

    def __str__(self):
        """
        String representation of ID
        >>> xml = '<photo id="2484" secret="123456" server="1" title="my photo" isprimary="0" />'
        >>> x = flickr_photo(123)
        >>> print x.__str__()
        'flickr_123'
        """
        return str("flickr_"+str(self.id))

    def get_icon_file_name(self):
        file_name = "flickr_icon_"+self.id
        file_path = self.cache.return_file_path(file_name)
        if file_path:
            return file_path
        else:
            print "Downloading a thumbnail to: %s" % file_path
            thumb = self.sizes.get("Thumbnail")
            resp = urllib2.urlopen(thumb.get("source"))
            self.cache.write_to_file(file_path)
            return file_path


# Unit Tests
if __name__ == "__main__":
    import doctest
    doctest.testmod()    
