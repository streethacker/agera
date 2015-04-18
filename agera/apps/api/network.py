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
)

from agera.utils.serializer import (
    serialize_network_io_counters,
    serialize_network_connections,
)


logger = logging.getLogger(__name__)


@bp.route('/network/io/counters')
@render_json
@validator({
    'pernic': BoolField,
})
def get_network_io_counters(pernic=False):

    with koenig_client() as koec:
        if pernic:
            net_io_counters_dict = koec.query_net_io_counters_pernic()

            result = []
            for interface, io_counters in net_io_counters_dict.iteritems():
                result.append({
                    interface: serialize_network_io_counters(io_counters),
                })

            return {'net_io_counters': result}

        net_io_counters = koec.query_net_io_counters()
        return {
            'net_io_counters': serialize_network_io_counters(net_io_counters)
        }


@bp.route('/network/connections')
@render_json
def get_network_connections():

    with koenig_client() as koec:
        net_connections = koec.query_net_connections()

    return {
        'net_connections': serialize_network_connections(net_connections)
    }
