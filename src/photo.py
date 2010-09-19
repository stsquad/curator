#!/usr/bin/python
#
# Represents an individual photo in a set. 

class photo():
    """
    While the photo class holds paths to cached photos and thumbnails it
    doesn't hold any awareness of where they came from. This is left to the
    various set classes which have knowledge of how to deal with this.

    TODO: decide how unique the id needs to be
    """

    def __init__(self, id):
        """
        Initilise the photo object
        >>> x = photo(1)
        >>> print x.id
        1
        >>> x.photo_path == None
        True
        >>> x.photo_thumb_path == None
        True
        """
        self.id = id
        self.photo_path = None
        self.photo_thumb_path = None

    def __str__(self):
        """
        String representation of ID
        >>> x = photo(123)
        >>> print x
        123
        >>> x = photo("/path/to/photo")
        >>> print x
        /path/to/photo
        """
        return str(self.id)
    


# Unit Tests
if __name__ == "__main__":
    import doctest
    doctest.testmod()    
    
