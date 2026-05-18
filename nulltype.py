#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class NullMeta(type):
    def __repr__(cls):
        if hasattr(cls, "repr"):
            return cls.repr
        else:
            return cls.__name__


class Null(metaclass=NullMeta):
    def __new__(cls, *args, **kwds):
        raise TypeError("Cannot instantiate Null")


if __name__ == "__main__":
    n1 = Null
    n2 = Null
    assert n1 is n2
    print(n1, n2)
