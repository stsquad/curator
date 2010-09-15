#!/usr/bin/python
#
# Set, Testing variant
#

from set import set

class test_set(set):
    """
    A virtual test set for unit testing, no real world uses
    >>> x = test_set("test")
    >>> print x.uri
    test
    """
    
    def __new__(cls, uri):
        """
        Creates a set object for a given URI source. If the class is capable of
        handling the URI it will return an instantied object, otherwise None
        >>> x=test_set("test")
        >>> x
        False
        >>> x=test_set("flibble")
        >>> x==None
        True
        """
        if uri.startswith("test"):
            obj = set.__new__(cls)
            return obj
        else:
            return None




# Unit Tests
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1:
        for a in sys.argv[1:]:
            print "Creating test_set: "+a
            pset = test_set(a)
            if pset:
                print "  created:"+pset
            else:
                print "  nothing created"
    else:
        import doctest
        doctest.testmod()    
