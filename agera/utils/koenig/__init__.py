# -*- coding: utf-8 -*-

import os
import thriftpy

from thriftpy.rpc import client_context

from agera.settings import (
    KOENIG_THRIFT_SETTINGS,
)


koenig_thrift = thriftpy.load(
    os.path.join(os.path.dirname(__file__), 'koenig.thrift'), 'koenig_thrift'
)


def make_client(service, name):
    host = KOENIG_THRIFT_SETTINGS[name]['host']
    port = KOENIG_THRIFT_SETTINGS[name]['port']
    return client_context(service, host, port)


def koenig_client():
    return make_client(koenig_thrift.KoenigService, 'koenig')
