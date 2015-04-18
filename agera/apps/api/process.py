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
    IntField,
    ListField,
)

from agera.utils.serializer import (
    serialize_process,
)


logger = logging.getLogger(__name__)


@bp.route('/process')
@render_json
@validator({
    'pid': IntField,
})
def get_process(pid):

    with koenig_client() as koec:
        process = koec.query_process_by_pid(pid)

    return {'process': serialize_process(process)}


@bp.route('/process/total')
@render_json
@validator({
    'pids': ListField(IntField),
})
def get_total_process(pids=None):

    if not pids:
        return {'total_process': []}

    with koenig_client() as koec:
        process_dict = koec.query_processes_by_pids(pids)

    result = []

    for pid, process in process_dict.iteritems():
        result.append({
            pid: serialize_process(process),
        })

    return {'total_process': result}
