#!/usr/bin/python
#
# Represents a set of photos as stored on the file-system

from os import path,listdir
from photo_set import photo_set
from photo import photo


class file_set(photo_set):
    """
    A photoset that lives on the file system in a directory structure
    """

    def __new__(cls, uri):
        """
        Creates a set object for a given URI file source. If the directory
        does not exist then the class will not instantiate.

        Appologies for hardwired paths in the test, this could be neater
        >>> x=file_set("/usr/share/images/desktop-base/")
        >>> x==None
        False
        >>> x=file_set("/dev/null")
        >>> x==None
        True
        """
        abs_path = path.abspath(uri)
        if path.exists(abs_path) and path.isdir(abs_path):
            obj = super(file_set, cls).__new__(cls)
            return obj
        else:
            return None

    def __init__(self, uri, recurse=False):
        """
        Initialise the object with number of files

        >>> fs=file_set("./tests/test_album1")
        >>> fs==None
        False
        >>> print fs
        File based Photoset: ./tests/test_album1 (3 photos)
        """
        super(file_set, self).__init__(uri)
        self.absolute_path = path.abspath(uri)
        for f in listdir(self.absolute_path):
            photo_path = self.absolute_path+"/"+f
            if self._file_is_image(photo_path):
                p = photo(photo_path)
                self.add_photo(p)

    def _file_is_image(self, path):
        """
        Check if a given file is a valid image
        >>> import os
        >>> p = os.getcwd()
        >>> ta = p+"/tests/test_album1"
        >>> fs = file_set(ta)
        >>> fs == None
        False
        >>> fs = file_set(ta)
        >>> ok = ta+"/new_context.jpg"
        >>> fs._file_is_image(ok)
        True
        >>> bad = p+"/file_set.py"
        >>> fs._file_is_image(bad)
        False
        """
        if path.endswith("jpg"):
            return True

        # fall-through
        return False
        
    def __str__(self):
        """
        Print a string representation of the set
        """
        return "File based Photoset: %s (%d photos)" % (self.uri, len(self.photos))




# Unit Tests
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1 and not sys.argv[1].startswith("-v"):
        for a in sys.argv[1:]:
            print "Creating file_set: "+a
            pset = file_set(a)
            if pset:
                print "  created:"+str(pset)
            else:
                print "  nothing created"
    else:
        import doctest
        doctest.testmod()    

