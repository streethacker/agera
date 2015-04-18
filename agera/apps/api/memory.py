# -*- coding: utf-8 -*-

import logging

from agera.apps.api import (
    bp,
    render_json,
)

from agera.utils.koenig import (
    koenig_client,
)

from agera.utils.serializer import (
    serialize_virtual_memory,
    serialize_swap_memory,
)


logger = logging.getLogger(__name__)


@bp.route('/memory/virtual')
@render_json
def get_virtual_memory():

    with koenig_client() as koec:
        virtual_memory = koec.query_virtual_memory()

    return serialize_virtual_memory(virtual_memory)


@bp.route('/memory/swap')
@render_json
def get_swap_memory():

    with koenig_client() as koec:
        swap_memory = koec.query_swap_memory()

    return serialize_swap_memory(swap_memory)
