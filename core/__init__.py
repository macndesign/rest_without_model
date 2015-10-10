# coding: utf-8
from __future__ import unicode_literals, absolute_import


class Task(object):
    def __init__(self, **kwargs):
        for field in ('id', 'name', 'owner', 'status'):
            setattr(self, field, kwargs.get(field, None))
