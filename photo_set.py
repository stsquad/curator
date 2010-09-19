#!/usr/bin/python
#
# Photo Set, represents a set of photos
#

class photo_set(object):
    """
    The photo set class represents a set of 'photos' from any photo source
    """

    def __init__(self, uri):
        """
        Initialise the Set object
        >>> x=photo_set("test")
        >>> print x.uri
        test
        """
        super(photo_set, self).__init__()
        self.uri = uri
        self.photos = []

    def __str__(self):
        """
        Print a string representation of the set
        >>> x=photo_set("test")
        >>> print str(x)
        Generic Photoset: test (0 photos)
        """
        return "Generic Photoset: %s (%d photos)" % (self.uri, len(self.photos))

    def __repr__(self):
        return "photo_set(%s) (uri:%s, photos:%d)" % (self.__name__, self.uri, len(self.photos))
    
    def add_photo(self, photo):
        """
        Add a photo to the internal photos list
        >>> from photo import photo
        >>> x=photo_set("test")
        >>> p=photo(1)
        >>> x.add_photo(p)
        >>> print str(x)
        Generic Photoset: test (1 photos)
        """
        self.photos.append(photo)
        

# Unit Tests
if __name__ == "__main__":
    import doctest
    doctest.testmod()    

