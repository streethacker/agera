# -*- coding: utf-8 -*-

import logging

from agera.apps.api import(
    bp,
    render_json,
)

from agera.utils.koenig import (
    koenig_client,
)

from agera.utils.validate import (
    validator,
    FloatField,
    BoolField,
)


from agera.utils.serializer import (
    serialize_cpu_times,
    serialize_cpu_times_percpu,
    serialize_cpu_times_percent,
    serialize_cpu_times_percent_percpu,
)


logger = logging.getLogger(__name__)


@bp.route('/cpu/times')
@render_json
@validator({
    'percpu': BoolField,
})
def get_cpu_times(percpu=False):

    with koenig_client() as koec:
        if percpu:
            cpu_times_percpu = koec.query_cpu_times_percpu()
            return {'cpu_times': serialize_cpu_times_percpu(cpu_times_percpu)}

        cpu_times = koec.query_cpu_times()
        return {'cpu_times': serialize_cpu_times(cpu_times)}


@bp.route('/cpu/percent')
@render_json
@validator({
    'interval': FloatField,
    'percpu': BoolField,
})
def get_cpu_percent(interval=0, percpu=False):

    with koenig_client() as koec:
        if percpu:
            cpu_percent_percpu = koec.query_cpu_percent_percpu(interval)
            return {'cpu_percent': cpu_percent_percpu}

        cpu_percent = koec.query_cpu_percent(interval)
        return {'cpu_percent': cpu_percent}


@bp.route('/cpu/times/percent')
@render_json
@validator({
    'interval': FloatField,
    'percpu': BoolField,
})
def get_cpu_times_percent(interval=0, percpu=False):

    with koenig_client() as koec:
        if percpu:
            cpu_times_percent_percpu = koec.query_cpu_times_percent_percpu(
                interval
            )
            result = serialize_cpu_times_percent_percpu(
                cpu_times_percent_percpu
            )
            return {'cpu_times_percent': result}

        cpu_times_percent = koec.query_cpu_times_percent(interval)
        return {
            'cpu_times_percent': serialize_cpu_times_percent(cpu_times_percent)
        }
