# -*- coding: utf-8 -*-
"""Document model. It represents an object committed to GIT"""

import jsonpickle

class Document(object):
    def __init__(self, key, value, max_depth=None):
        """
        Build an instance of Document model
        :param key: the document key. Must be unique (a hash, normally)
        :param value: the value to store as document. It will serialized to
        json using jsonpickle
        :param max_depth: max number of step to recurse into value.  If set to a
        non-negative integer then jsonpickle will not recurse deeper than
        ‘max_depth’ steps into the object. Anything deeper than ‘max_depth’ is
        represented using a Python repr() of the object.
        """
        self.key = key
        self.value = jsonpickle.encode(value, max_depth=max_depth)
