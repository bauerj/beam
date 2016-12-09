# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from os import path

import codecs


def _read_file(name, encoding='utf-8'):
    """
    Read the contents of a file.

    :param name: The name of the file in the current directory.
    :param encoding: The encoding of the file; defaults to utf-8.
    :return: The contents of the file.
    """
    with codecs.open(name, encoding=encoding) as f:
        return f.read()


__version__ = _read_file(path.join(path.dirname(__file__), 'VERSION')).strip()


def _details_from_identifier(identifier):
    pass


def vps(identifier):
    name, key, hash_ = _details_from_identifier(identifier)
