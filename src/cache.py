#!/usr/bin/python
#
# Simple Cached Object manager for Curator
#

import os

from xml.etree.ElementTree import ElementTree

# Basepath
cache_root=os.path.expanduser("~/.cache/curator/")

class cache():
    """
    The cache object is used as a simple cache manager for thumbnail,
    preview pictures and XML/JSON outputs from web services. One manager
    exists per set.

    The cache id is usually something simple like a concatination of type
    and set id although more complex hashing can be used
    """

    def __init__(self, cache_id):
        self.path = cache_root+cache_id
        if os.path.exists(self.path):
            if not os.path.isdir(self.path):
                raise IOError, self.path
        else:
            os.makedirs(self.path)

    def save_xml(self, name, xml_tree):
        file_path=self.path+"/"+name
        if os.path.exists(file_path):
            print "Overwritting: "+file_path
        xml_tree.write(file_path)
        
        return

    def load_xml(self, name):
        file_path=self.path+"/"+name
        if not os.path.exists(file_path):
            print "Couldn't find cached: "+file_path
            return None
        else:
            xml_tree=ElementTree(file=file_path)
            return xml_tree
    
