# -*- coding: utf-8 -*-
"""References model. It represents a mutable GIT object, like a branch,
tag or remote. It's basically a pointer to a specific commit."""

class Reference(object):
    def __init__(self, pointer, name):
        """
        Builds a Reference instance.
        :param pointer: pointer to a commit. A hash string
        :param name: name for the pointer (the tag, the branch's name, etc)
        """
        self.pointer = pointer
        self.name = name
