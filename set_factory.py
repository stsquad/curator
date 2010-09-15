#!/usr/bin/python
#
# Factory to create an set objects
#

import set

def create_set(uri):
    """
    Run through the available set types until one works with the passed URI.

    When adding new set types they will need to be added to the factory
    """
    
