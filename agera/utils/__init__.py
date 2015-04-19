# -*- coding: utf-8 -*-

import time
import datetime


def datetime2utc(x):
    return time.mktime(x.timetuple()) if x else 0


def utc2datetime(x):
    return datetime.datetime.fromtimestamp(x)


def bytes2human(n, scale=0, unit=''):

    if n is None:
        return

    result = '%.{}f %s{}'.format(scale, unit)
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')

    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            val = float(n) / prefix[s]
            return result % (val, s)

    return result % (n, 'B')
