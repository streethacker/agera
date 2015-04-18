# -*- coding: utf-8 -*-

from agera.utils import (
    utc2datetime,
)

from marshmallow import (
    Schema,
    fields,
)


class CpuTimesSchema(Schema):

    class Meta:
        fields = ('user', 'system', 'idle', 'nice', 'iowait', 'irq',
                  'softirq', 'steal', 'guest', 'guest_nice')


def serialize_cpu_times(cpu_times):
    return CpuTimesSchema().dump(cpu_times).data


def serialize_cpu_times_percpu(cpu_times_percpu):
    return CpuTimesSchema(many=True).dump(cpu_times_percpu).data


class CpuTimesPercentSchema(Schema):

    class Meta:
        fields = ('user', 'system', 'idle', 'nice', 'iowait', 'irq',
                  'softirq', 'steal', 'guest', 'guest_nice')


def serialize_cpu_times_percent(cpu_times_percent):
    return CpuTimesPercentSchema().dump(cpu_times_percent).data


def serialize_cpu_times_percent_percpu(cpu_times_percent_percpu):
    return CpuTimesPercentSchema(many=True).dump(cpu_times_percent_percpu).data


class VirtualMemory(Schema):

    class Meta:
        fields = ('total', 'available', 'percent', 'used', 'free',
                  'active', 'inactive', 'buffers', 'cached', 'wired',
                  'shared')


def serialize_virtual_memory(virtual_memory):
    return VirtualMemory().dump(virtual_memory).data


class SwapMemory(Schema):

    class Meta:
        fields = ('total', 'used', 'free', 'percent', 'sin', 'sout')


def serialize_swap_memory(swap_memory):
    return SwapMemory().dump(swap_memory).data


class DiskPartitionSchema(Schema):

    class Meta:
        fields = ('device', 'mountpoint', 'fstype', 'opts')


def serialize_disk_partition(partition):
    return DiskPartitionSchema().dump(partition).data


class DiskUsageSchema(Schema):

    class Meta:
        fields = ('total', 'used', 'free', 'percent')


def serialize_disk_usage(usage):
    return DiskUsageSchema().dump(usage).data


class DiskIOCountersSchema(Schema):

    class Meta:
        fields = ('read_count', 'write_count', 'read_bytes', 'write_bytes',
                  'read_time', 'write_time')


def serialize_disk_io_counters(io_counters):
    return DiskIOCountersSchema().dump(io_counters).data


class NetworkIOCountersSchema(Schema):

    class Meta:
        fields = ('bytes_sent', 'bytes_recv', 'packets_sent', 'packets_recv',
                  'errin', 'errout', 'dropin', 'dropout')


def serialize_network_io_counters(io_counters):
    return NetworkIOCountersSchema().dump(io_counters).data


class NetworkConnectionSchema(Schema):

    laddr = fields.Method('_laddr')
    raddr = fields.Method('_raddr')

    def _laddr(self, connection):
        return fields.OrderedDict({
            'ip': connection.laddr.ip,
            'port': connection.laddr.port,
        })

    def _raddr(self, connection):
        return fields.OrderedDict({
            'ip': connection.raddr.ip,
            'port': connection.raddr.port,
        })

    class Meta:
        fields = ('fd', 'family', 'type', 'laddr', 'raddr', 'status', 'pid')


def serialize_network_connections(connections):
    return NetworkConnectionSchema(many=True).dump(connections).data


class UserSchema(Schema):

    class Meta:
        fields = ('name', 'terminal', 'host', 'started')


def serialize_users(users):
    return UserSchema(many=True).dump(users).data


class ProcessSchema(Schema):

    create_time = fields.Method('_create_time')
    uids = fields.Method('_get_uids')
    gids = fields.Method('_get_gids')

    def _create_time(self, process):
        return utc2datetime(process.create_time).strftime('%Y-%m-%d %H:%M:%S')

    def _get_uids(self, process):
        return fields.OrderedDict({
            'real': process.uids.real,
            'effective': process.uids.effective,
            'saved': process.uids.saved,
        })

    def _get_gids(self, process):
        return fields.OrderedDict({
            'real': process.gids.real,
            'effective': process.gids.effective,
            'saved': process.gids.saved,
        })

    class Meta:
        fields = ('pid', 'ppid', 'name', 'username', 'create_time',
                  'cpu_percent', 'memory_percent', 'cwd', 'status',
                  'exe', 'uids', 'gids')


def serialize_process(process):
    return ProcessSchema().dump(process).data
