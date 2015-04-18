# -*- coding: utf-8 -*-

import time
import datetime


def datetime2utc(x):
    return time.mktime(x.timetuple()) if x else 0


def utc2datetime(x):
    return datetime.datetime.fromtimestamp(x)
