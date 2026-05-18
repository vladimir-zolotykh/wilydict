#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class WilyDict(dict):
    _next: int = 0

    def __missing__(self, key):
        if not (key.startswith("__") and key.endswith("__")):
            self[key] = self._next
            self._next += 1


class AutoMeta(type):
    def __prepare__(cls, bases, **kwds):
        # cls: AutoConst
        return WilyDict()


class AutoConst(metaclass=AutoMeta):
    pass


class Color(AutoConst):
    RED
    GREEN
    BLUE


if __name__ == "__main__":
    c = Color()
    print(c.RED, c.GREEN, c.BLUE)
