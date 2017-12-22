# -*- coding: utf-8 -*-

"""Author model. It represents the author of a GIT commit"""
class Author(object):
    def __init__(self, name, email):
        """
        Builds an instance of Author model
        :param name: the author's name
        :param email: the author's email
        """
        self.name = name
        self.email = email
