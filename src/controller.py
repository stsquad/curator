#!/usr/bin/python
#
# Some sort of controller for everything else to reference
#

from set_factory import create_set


class controller(object):
    """
    The controller object is the principle interaction point with the system
    """
    verbose = False
    # a set of photo sets
    photo_sets = []

    def __init__(self, verbose=False):
        self.verbose = verbose
        return

    def add_set_by_uri(self, set_uri):
        """
        Add a set
        """
        pset=create_set(set_uri)
        if pset:
            if self.verbose: print "Added: "+str(pset)
            self.photo_sets.append(pset)

    def get_set_count(self):
        return len(self.photo_sets)

    def get_sets(self):
        return self.photo_sets
