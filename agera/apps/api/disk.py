# -*- coding: utf-8 -*-

import logging

from agera.apps.api import (
    bp,
    render_json,
)

from agera.utils.koenig import (
    koenig_client,
)

from agera.utils.validate import (
    validator,
    BoolField,
    StringField,
)

from agera.utils.serializer import (
    serialize_disk_partitions,
    serialize_disk_io_counters,
    serialize_disk_usage,
)


logger = logging.getLogger(__name__)


@bp.route('/disk/partitions')
@render_json
def get_disk_partitions():

    with koenig_client() as koec:
        disk_partitions = koec.query_disk_partitions()

    return {'disk_partitions': serialize_disk_partitions(disk_partitions)}


@bp.route('/disk/io/counters')
@render_json
@validator({
    'perdisk': BoolField,
})
def get_disk_io_counters(perdisk=False):

    with koenig_client() as koec:
        if perdisk:
            result = []

            io_counters_dict = koec.query_disk_io_counters_perdisk()
            for name, counter in io_counters_dict.iteritems():
                result.append({
                    name: serialize_disk_io_counters(counter),
                })

            return {'disk_io_counters': result}

        io_counters = koec.query_disk_io_counters()
        return {'disk_io_counters': serialize_disk_io_counters(io_counters)}


@bp.route('/disk/usage')
@render_json
@validator({
    'path': StringField,
})
def get_disk_usage(path='/'):

    with koenig_client() as koec:
        disk_usage = koec.query_disk_usage(path)

    return serialize_disk_usage(disk_usage)
