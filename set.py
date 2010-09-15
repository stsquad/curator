#!/usr/bin/python
#
# Set, represents a set of photos
#

#import object

class set(object):
    """
    The set class represents a set of 'photos' from any photo source
    """

    def __init__(self, uri):
        """
        Initialise the Set object
        >>> x=set("test")
        >>> print x.uri
        test
        """
        self.uri = uri

    def __str__(self):
        """
        Print a string representation of the set
        >>> x=set("test")
        >>> print x
        Generic Photoset: test
        """
        return "Generic Photoset: "+self.uri


# Unit Tests
if __name__ == "__main__":
    import doctest
    doctest.testmod()    

