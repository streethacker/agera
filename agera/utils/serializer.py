# -*- coding: utf-8 -*-

from agera.utils import (
    utc2datetime,
    bytes2human,
)

from marshmallow import (
    Schema,
    fields,
)

from socket import (
    AF_INET,
    AF_INET6,
    SOCK_STREAM,
    SOCK_DGRAM,
)


class CPUTimesSchema(Schema):

    class Meta:
        fields = ('user', 'system', 'idle', 'nice', 'iowait', 'irq',
                  'softirq', 'steal', 'guest', 'guest_nice')


def serialize_cpu_times(cpu_times):
    return CPUTimesSchema().dump(cpu_times).data


def serialize_cpu_times_percpu(cpu_times_percpu):
    return CPUTimesSchema(many=True).dump(cpu_times_percpu).data


class CPUTimesPercentSchema(Schema):

    class Meta:
        fields = ('user', 'system', 'idle', 'nice', 'iowait', 'irq',
                  'softirq', 'steal', 'guest', 'guest_nice')


def serialize_cpu_times_percent(cpu_times_percent):
    return CPUTimesPercentSchema().dump(cpu_times_percent).data


def serialize_cpu_times_percent_percpu(cpu_times_percent_percpu):
    return CPUTimesPercentSchema(many=True).dump(cpu_times_percent_percpu).data


class VirtualMemory(Schema):

    percent = fields.Method('_percent')

    def _percent(self, memory):
        return '%.2f' % memory.percent

    total = fields.Method('_total')

    def _total(self, memory):
        return bytes2human(memory.total, 1)

    available = fields.Method('_available')

    def _available(self, memory):
        return bytes2human(memory.available, 1)

    used = fields.Method('_used')

    def _used(self, memory):
        return bytes2human(memory.used, 1)

    free = fields.Method('_free')

    def _free(self, memory):
        return bytes2human(memory.free, 1)

    active = fields.Method('_active')

    def _active(self, memory):
        return bytes2human(memory.active, 1)

    inactive = fields.Method('_inactive')

    def _inactive(self, memory):
        return bytes2human(memory.inactive, 1)

    buffers = fields.Method('_buffers')

    def _buffers(self, memory):
        return bytes2human(memory.buffers, 1)

    cached = fields.Method('_cached')

    def _cached(self, memory):
        return bytes2human(memory.cached, 1)

    wired = fields.Method('_wired')

    def _wired(self, memory):
        return bytes2human(memory.wired, 1)

    shared = fields.Method('_shared')

    def _shared(self, memory):
        return bytes2human(memory.shared, 1)

    class Meta:
        fields = ('total', 'available', 'percent', 'used', 'free',
                  'active', 'inactive', 'buffers', 'cached', 'wired',
                  'shared')


def serialize_virtual_memory(virtual_memory):
    return VirtualMemory().dump(virtual_memory).data


class SwapMemory(Schema):

    percent = fields.Method('_percent')

    def _percent(self, memory):
        return '%.2f' % memory.percent

    total = fields.Method('_total')

    def _total(self, memory):
        return bytes2human(memory.total, 1)

    used = fields.Method('_used')

    def _used(self, memory):
        return bytes2human(memory.used, 1)

    free = fields.Method('_free')

    def _free(self, memory):
        return bytes2human(memory.free, 1)

    sin = fields.Method('_sin')

    def _sin(self, memory):
        return bytes2human(memory.sin, 1)

    sout = fields.Method('_sout')

    def _sout(self, memory):
        return bytes2human(memory.sout, 1)

    class Meta:
        fields = ('total', 'used', 'free', 'percent', 'sin', 'sout')


def serialize_swap_memory(swap_memory):
    return SwapMemory().dump(swap_memory).data


class DiskPartitionSchema(Schema):

    class Meta:
        fields = ('device', 'mountpoint', 'fstype', 'opts')


def serialize_disk_partitions(partition):
    return DiskPartitionSchema(many=True).dump(partition).data


class DiskUsageSchema(Schema):

    percent = fields.Method('_percent')

    def _percent(self, disk_usage):
        return '%.2f' % disk_usage.percent

    class Meta:
        fields = ('total', 'used', 'free', 'percent')


def serialize_disk_usage(usage):
    return DiskUsageSchema().dump(usage).data


class DiskIOCountersSchema(Schema):

    read_bytes = fields.Method('_read_bytes')

    def _read_bytes(self, io_counters):
        return bytes2human(io_counters.read_bytes, 2, '/s')

    write_bytes = fields.Method('_write_bytes')

    def _write_bytes(self, io_counters):
        return bytes2human(io_counters.write_bytes, 2, '/s')

    class Meta:
        fields = ('read_count', 'write_count', 'read_bytes', 'write_bytes',
                  'read_time', 'write_time')


def serialize_disk_io_counters(io_counters):
    return DiskIOCountersSchema().dump(io_counters).data


class NetworkIOCountersSchema(Schema):

    bytes_sent = fields.Method('_bytes_sent')

    def _bytes_sent(self, net_io_counters):
        return bytes2human(net_io_counters.bytes_sent, 2)

    bytes_recv = fields.Method('_bytes_recv')

    def _bytes_recv(self, net_io_counters):
        return bytes2human(net_io_counters.bytes_recv, 2)

    class Meta:
        fields = ('bytes_sent', 'bytes_recv', 'packets_sent', 'packets_recv',
                  'errin', 'errout', 'dropin', 'dropout')


def serialize_network_io_counters(io_counters):
    return NetworkIOCountersSchema().dump(io_counters).data


class NetworkConnectionSchema(Schema):

    proto_map = {
        (AF_INET, SOCK_STREAM): 'tcp',
        (AF_INET6, SOCK_STREAM): 'tcp6',
        (AF_INET, SOCK_DGRAM): 'udp',
        (AF_INET6, SOCK_DGRAM): 'udp6',
    }

    proto = fields.Method('_proto')

    def _proto(self, connection):
        return self.proto_map.get(
            (connection.family, connection.type)
        )

    laddr = fields.Method('_laddr')

    def _laddr(self, connection):
        return fields.OrderedDict({
            'ip': connection.laddr.ip,
            'port': connection.laddr.port,
        })

    raddr = fields.Method('_raddr')

    def _raddr(self, connection):
        return fields.OrderedDict({
            'ip': connection.raddr.ip,
            'port': connection.raddr.port,
        })

    class Meta:
        fields = ('proto', 'fd', 'family', 'type', 'laddr', 'raddr',
                  'status', 'pid')


def serialize_network_connections(connections):
    return NetworkConnectionSchema(many=True).dump(connections).data


class UserSchema(Schema):

    class Meta:
        fields = ('name', 'terminal', 'host', 'started')


def serialize_users(users):
    return UserSchema(many=True).dump(users).data


class ProcessSchema(Schema):

    create_time = fields.Method('_create_time')

    def _create_time(self, process):
        return utc2datetime(process.create_time).strftime('%Y-%m-%d %H:%M:%S')

    cpu_percent = fields.Method('_cpu_percent')

    def _cpu_percent(self, process):
        return '%.2f' % process.cpu_percent

    memory_percent = fields.Method('_memory_percent')

    def _memory_percent(self, process):
        return '%.2f' % process.memory_percent

    uids = fields.Method('_get_uids')

    def _get_uids(self, process):
        return fields.OrderedDict({
            'real': process.uids.real,
            'effective': process.uids.effective,
            'saved': process.uids.saved,
        })

    gids = fields.Method('_get_gids')

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
