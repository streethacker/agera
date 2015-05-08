## Agera接口文档 ##

<br />

#### 1. 查询系统CPU时间(GET: /api/times) ####

查询系统CPU时间，结果中的每个属性代表了CPU在各自模式下工作的秒数

**请求地址**

```
http://localhost:7300/api/cpu/times
```

**签名生成**

**系统级参数**

**应用级参数**

 参数名称       | 类型 | 是否必须 | 示例值 | 描述 
----------------|------|----------|--------|--------------------------------
percpu          | int  | 否       | 1      | 是否显示每个cpu的详细信息(多核) 


**示例url**

```
http://localhost:7300/api/cpu/times?percpu=1
```

**返回结果**

```
{
    code: 200,
    data: {
        cpu_times: [
            {
                guest: null,
                guest_nice: null,
                idle: 29706.15,
                iowait: null,
                irq: null,
                nice: 0,
                softirq: null,
                steal: null,
                system: 1425.08,
                user: 2142.05
            },
            {
                guest: null,
                guest_nice: null,
                idle: 32213.23,
                iowait: null,
                irq: null,
                nice: 0,
                softirq: null,
                steal: null,
                system: 284.9,
                user: 774.42
            },
            {
                guest: null,
                guest_nice: null,
                idle: 30340.16,
                iowait: null,
                irq: null,
                nice: 0,
                softirq: null,
                steal: null,
                system: 920.3,
                user: 2012.09
            },
            {
                guest: null,
                guest_nice: null,
                idle: 32132.7,
                iowait: null,
                irq: null,
                nice: 0,
                softirq: null,
                steal: null,
                system: 308.65,
                user: 831.2
            }
        ]
    },
    message: "ok"
}
```

**错误码**

错误码  |  代表含义
--------|-----------------------
1000    | Koenig 服务错误
601     | 缺少必要的请求参数
602     | 参数格式错误

<br />

#### 2. 查询CPU占用率信息(GET: /api/cpu/percent) ####

查询系统全局范围内CPU占用率信息

**请求地址**

```
http://localhost:7300/api/cpu/percent
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
---------| -----| ---------| -------| --------------------------------
percpu   | int  | 否       |  1     | 是否显示每个CPU的详细信息(多核) 

**示例url**

```
http://localhost:7300/api/cpu/percent?percpu=1
```

**返回结果**

```
{
    code: 200,
    data: {
        cpu_percent: [
            18.8,
            3.7,
            15.8,
            4.1
        ]
    },
    message: "ok"
}
```

**错误码**

错误码  |  代表含义
--------|-----------------------
1000    | Koenig 服务错误
601     | 缺少必要的请求参数
602     | 参数格式错误

<br />

#### 3. 查询CPU工作于各模式下的时间占用率(GET: /api/cpu/times/percent) ####

查询CPU工作于不同模式下的占用率信息

**请求地址**

```
http://localhost:7300/api/cpu/times/percent
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型  | 是否必须 | 示例值 | 描述
---------| ------| ---------| -------| -------------
percpu   | int   | 否       | 1      | 是否查询所有CPU核心的信息(多核) 
interval | float | 否       | 1.0    | 计算占用率的时间间隔 

**示例url**

```
http://localhost:7300/api/cpu/times/percent?percpu=1&interval=0.1
```

**返回结果**

```
{
    code: 200,
    data: {
        cpu_times_percent: [
            {
                guest: null,
                guest_nice: null,
                idle: 81.2,
                iowait: null,
                irq: null,
                nice: 0,
                softirq: null,
                steal: null,
                system: 7.6,
                user: 11.3
            },
            {
                guest: null,
                guest_nice: null,
                idle: 96.3,
                iowait: null,
                irq: null,
                nice: 0,
                softirq: null,
                steal: null,
                system: 1.1,
                user: 2.6
            },
            {
                guest: null,
                guest_nice: null,
                idle: 84,
                iowait: null,
                irq: null,
                nice: 0,
                softirq: null,
                steal: null,
                system: 4.6,
                user: 11.4
            },
            {
                guest: null,
                guest_nice: null,
                idle: 95.9,
                iowait: null,
                irq: null,
                nice: 0,
                softirq: null,
                steal: null,
                system: 1.3,
                user: 2.8
            }
        ]
    },
    message: "ok"
}
``` 

**错误码**

错误码  |  代表含义
--------|-----------------------
1000    | Koenig 服务错误
601     | 缺少必要的请求参数
602     | 参数格式错误

<br />

#### 4. 查询系统内存的使用情况(GET: /api/memory/virtual) ####

查询系统内存的使用情况

**请求地址**

```
http://localhost:7300/api/memory/virtual
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
---------| -----| ---------|--------| --------------------

**示例url**

```
http://localhost:7300/api/memory/virtual
```

**返回结果**

```
{
    code: 200,
    data: {
        active: "3.9 G",
        available: "3.0 G",
        buffers: null,
        cached: null,
        free: "163.9 M",
        inactive: "2.8 G",
        percent: "63.00",
        shared: null,
        total: "8.0 G",
        used: "7.7 G",
        wired: "1001.9 M"
    },
    message: "ok"
}
```

**错误码**

错误码  |  代表含义
--------|-----------------------
1000    | Koenig 服务错误
601     | 缺少必要的请求参数
602     | 参数格式错误

<br />

#### 5. 查询内存置换(swap memory)的数据(GET: /api/memory/swap) ####

查询内存交换的相关数据

**请求地址**

```
http://localhost:7300/api/memory/swap
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
-------| -----| --------|------| --------------------

**示例url**

```
http://localhost:7300/api/memory/swap
```

**返回结果**

```
{
    code: 200,
    data: {
        free: "0.0 B",
        percent: "0.00",
        sin: "15.1 G",
        sout: "147.0 M",
        total: "0.0 B",
        used: "0.0 B"
    },
    message: "ok"
}
```

**错误码**

错误码  |  代表含义
--------|-----------------------
1000    | Koenig 服务错误
601     | 缺少必要的请求参数
602     | 参数格式错误

<br />

#### 6. 查询所有已挂在分区的信息(GET: /api/disk/partitions) ####

查询已挂在分区的信息：设备名、挂载点、文件系统类型等

**请求地址**

```
http://localhost:7300/api/disk/partitions
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
---------| -----| ---------|--------| --------------------

**示例url**

```
http://localhost:7300/api/disk/partitions
```

**返回结果**

```
{
    code: 200,
    data: {
        disk_partitions: [
            {
                device: "/dev/disk1",
                fstype: "hfs",
                mountpoint: "/",
                opts: "rw,local,rootfs,dovolfs,journaled,multilabel"
            }
        ]
    },
    message: "ok"
}
```

**错误码**

错误码  |  代表含义
--------|-----------------------
1000    | Koenig 服务错误
601     | 缺少必要的请求参数
602     | 参数格式错误

<br />

#### 7. 查询磁盘的IO数据(GET: /api/disk/io/counters) ####

查询系统全局范围内磁盘IO的相关统计数据

**请求地址**

```
http://localhost:7300/api/disk/io/counters
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
---------| -----| ---------|--------| --------------------
perdisk  | int  | 否       | 1      | 是否获取每个磁盘的具体信息 

**示例url**

```
http://localhost:7300/api/disk/io/counters?perdisk=1
```

**返回结果**

```
{
    code: 200,
    data: {
        disk_io_counters: [
            {
                disk0: {
                    read_bytes: "8.03 G/s",
                    read_count: 246008,
                    read_time: 235040,
                    write_bytes: "8.43 G/s",
                    write_count: 251839,
                    write_time: 139457
                }
            }
        ]
    },
    message: "ok"
}
```

**错误码**

错误码  |  代表含义
--------|-----------------------
1000    | Koenig 服务错误
601     | 缺少必要的请求参数
602     | 参数格式错误

<br />

#### 8. 查询磁盘空间的使用情况(GET: /api/disk/usage) ####

查询指定分区磁盘空间的使用情况(默认为根分区)

**请求地址**

```
http://localhost:7300/api/disk/usage
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
---------| -----| ---------|--------| --------------------
path     | str  | 否       | '/'    | 磁盘分区

**示例url**

```
http://localhost:7300/api/disk/usage?path=/dev/sda3
```

**返回结果**

```
{
    code: 200,
    data: {
        free: "56.2 G",
        percent: "49.60",
        total: "111.9 G",
        used: "55.5 G"
    },
    message: "ok"
}
```

**错误码**

错误码  |  代表含义
--------|-----------------------
1000    | Koenig 服务错误
601     | 缺少必要的请求参数
602     | 参数格式错误

<br />

#### 9. 查询网络IO数据(GET: /api/network/io/counters) ####

查询系统全局范围内网络IO的相关统计数据

**请求地址**

```
http://localhost:7300/api/network/io/counters
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
---------| -----| ---------|--------| --------------------
pernic  | int  | 否       | 1      | 是否获取每个磁盘的具体信息 

**示例url**

```
http://localhost:7300/api/network/io/counters?pernic=1
```

**返回结果**

```
{
    code: 200,
    data: {
        net_io_counters: [
            {
                gif0: {
                    bytes_recv: "0.00 B",
                    bytes_sent: "0.00 B",
                    dropin: 0,
                    dropout: 0,
                    errin: 0,
                    errout: 0,
                    packets_recv: 0,
                    packets_sent: 0
                }
            },
            {
                en2: {
                    bytes_recv: "0.00 B",
                    bytes_sent: "0.00 B",
                    dropin: 0,
                    dropout: 0,
                    errin: 0,
                    errout: 0,
                    packets_recv: 0,
                    packets_sent: 0
                }
            },
            {
                en0: {
                    bytes_recv: "1.01 G",
                    bytes_sent: "60.45 M",
                    dropin: 0,
                    dropout: 0,
                    errin: 0,
                    errout: 0,
                    packets_recv: 860639,
                    packets_sent: 692864
                }
            },
            {
                en1: {
                    bytes_recv: "0.00 B",
                    bytes_sent: "0.00 B",
                    dropin: 0,
                    dropout: 0,
                    errin: 0,
                    errout: 0,
                    packets_recv: 0,
                    packets_sent: 0
                }
            },
            {
                lo0: {
                    bytes_recv: "14.31 M",
                    bytes_sent: "14.31 M",
                    dropin: 0,
                    dropout: 0,
                    errin: 0,
                    errout: 0,
                    packets_recv: 25381,
                    packets_sent: 25381
                }
            },
            {
                bridge0: {
                    bytes_recv: "0.00 B",
                    bytes_sent: "2.00 K",
                    dropin: 0,
                    dropout: 0,
                    errin: 0,
                    errout: 0,
                    packets_recv: 0,
                    packets_sent: 6
                }
            },
            {
                p2p0: {
                    bytes_recv: "0.00 B",
                    bytes_sent: "0.00 B",
                    dropin: 0,
                    dropout: 0,
                    errin: 0,
                    errout: 0,
                    packets_recv: 0,
                    packets_sent: 0
                }
            },
            {
                stf0: {
                    bytes_recv: "0.00 B",
                    bytes_sent: "0.00 B",
                    dropin: 0,
                    dropout: 0,
                    errin: 0,
                    errout: 0,
                    packets_recv: 0,
                    packets_sent: 0
                }
            },
            {
                awdl0: {
                    bytes_recv: "0.00 B",
                    bytes_sent: "107.36 K",
                    dropin: 0,
                    dropout: 0,
                    errin: 0,
                    errout: 0,
                    packets_recv: 0,
                    packets_sent: 482
                }
            }
        ]
    },
    message: "ok"
}
```

**错误码**

错误码  |  代表含义
--------|-----------------------
1000    | Koenig 服务错误
601     | 缺少必要的请求参数
602     | 参数格式错误

<br />

#### 10. 查询网络连接信息(GET: /api/disk/io/counters) ####

查询系统全局范围内Socket连接的相关信息

**请求地址**

```
http://localhost:7300/api/network/connections
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
---------| -----| ---------|--------| --------------------

**示例url**

```
http://localhost:7300/api/network/connections
```

**返回结果**

```
{
    code: 200,
    data: {
        net_connections: [
            {
                family: 2,
                fd: 6,
                laddr: null,
                pid: 18235,
                proto: "tcp",
                raddr: null,
                status: "ESTABLISHED",
                type: 1
            },
            {
                family: 30,
                fd: 7,
                laddr: null,
                pid: 18235,
                proto: "tcp6",
                raddr: null,
                status: "ESTABLISHED",
                type: 1
            },
            {
                family: 2,
                fd: 81,
                laddr: null,
                pid: 17442,
                proto: "tcp",
                raddr: null,
                status: "ESTABLISHED",
                type: 1
            },
            {
                family: 2,
                fd: 82,
                laddr: null,
                pid: 17442,
                proto: "tcp",
                raddr: null,
                status: "ESTABLISHED",
                type: 1
            },
            {
                family: 30,
                fd: 24,
                laddr: null,
                pid: 158,
                proto: "udp6",
                raddr: null,
                status: "NONE",
                type: 2
            },
            {
                family: 30,
                fd: 25,
                laddr: null,
                pid: 158,
                proto: "udp6",
                raddr: null,
                status: "NONE",
                type: 2
            },
            {
                family: 2,
                fd: 27,
                laddr: null,
                pid: 158,
                proto: "udp",
                raddr: null,
                status: "NONE",
                type: 2
            },
            {
                family: 30,
                fd: 36,
                laddr: null,
                pid: 49,
                proto: "udp6",
                raddr: null,
                status: "NONE",
                type: 2
            },
            {
                family: 2,
                fd: 58,
                laddr: null,
                pid: 49,
                proto: "udp",
                raddr: null,
                status: "NONE",
                type: 2
            },
            {
                family: 30,
                fd: 59,
                laddr: null,
                pid: 49,
                proto: "udp6",
                raddr: null,
                status: "NONE",
                type: 2
            },
            {
                family: 30,
                fd: 10,
                laddr: null,
                pid: 30,
                proto: "udp6",
                raddr: null,
                status: "NONE",
                type: 2
            },
            {
                family: 2,
                fd: 20,
                laddr: null,
                pid: 1,
                proto: "udp",
                raddr: null,
                status: "NONE",
                type: 2
            },
            {
                family: 2,
                fd: 29,
                laddr: null,
                pid: 1,
                proto: "udp",
                raddr: null,
                status: "NONE",
                type: 2
            }
        ]
    },
    message: "ok"
}
```

**错误码**

错误码  |  代表含义
--------|-----------------------
1000    | Koenig 服务错误
601     | 缺少必要的请求参数
602     | 参数格式错误

<br />

#### 11. 查询指定pid的进程信息(GET: /api/process) ####

查询指定pid的进程信息

**请求地址**

```
http://localhost:7300/api/process
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
---------| -----| ---------|--------| --------------------
pid      | int  | 是       | 17442  | 进程pid 

**示例url**

```
http://localhost:7300/api/process?pid=17442
```

**返回结果**

```
{
    code: 200,
    data: {
        process: {
            cpu_percent: "17.60",
            create_time: "2015-05-08 20:47:48",
            cwd: "/",
            exe: null,
            gids: null,
            memory_percent: "1.89",
            name: "Google Chrome",
            pid: 17442,
            ppid: 1,
            status: "running",
            uids: null,
            username: "YUCHI"
        }
    },
    message: "ok"
}
```

**错误码**

错误码  |  代表含义
--------|-----------------------
1000    | Koenig 服务错误
601     | 缺少必要的请求参数
602     | 参数格式错误

<br />

#### 12. 查询当前系统中所有进程的信息(GET: /api/process/total) ####

查询当前系统中所有进程的信息

**请求地址**

```
http://localhost:7300/api/process/total
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
---------| -----| ---------|--------| --------------------

**示例url**

```
http://localhost:7300/api/process/total
```

**返回结果**

```
{
    code: 200,
    data: {
        total_process: [
            {
                0: {
                    cpu_percent: "8.50",
                    create_time: "2015-05-08 09:40:36",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "10.34",
                    name: "kernel_task",
                    pid: 0,
                    ppid: 0,
                    status: "running",
                    uids: null,
                    username: "root"
                }
            },
            {
                1: {
                    cpu_percent: "0.00",
                    create_time: "2015-05-08 09:40:36",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "0.15",
                    name: "launchd",
                    pid: 1,
                    ppid: 0,
                    status: "running",
                    uids: null,
                    username: "root"
                }
            },
            {
                20: {
                    cpu_percent: "0.10",
                    create_time: "2015-05-08 09:40:37",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "0.08",
                    name: "fseventsd",
                    pid: 20,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "root"
                }
            },
            {
                17437: {
                    cpu_percent: "2.30",
                    create_time: "2015-05-08 20:47:15",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "0.68",
                    name: "VLC",
                    pid: 17437,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                33: {
                    cpu_percent: "0.20",
                    create_time: "2015-05-08 09:40:37",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "0.57",
                    name: "mds",
                    pid: 33,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "root"
                }
            },
            {
                17442: {
                    cpu_percent: "9.10",
                    create_time: "2015-05-08 20:47:48",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "1.88",
                    name: "Google Chrome",
                    pid: 17442,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                17444: {
                    cpu_percent: "6.80",
                    create_time: "2015-05-08 20:47:48",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "2.37",
                    name: "Google Chrome Helper",
                    pid: 17444,
                    ppid: 17442,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                17448: {
                    cpu_percent: "0.00",
                    create_time: "2015-05-08 20:47:49",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "0.59",
                    name: "Google Chrome Helper",
                    pid: 17448,
                    ppid: 17442,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                17449: {
                    cpu_percent: "2.20",
                    create_time: "2015-05-08 20:47:49",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "0.64",
                    name: "Google Chrome Helper",
                    pid: 17449,
                    ppid: 17442,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                17450: {
                    cpu_percent: "0.00",
                    create_time: "2015-05-08 20:47:49",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "0.52",
                    name: "Google Chrome Helper",
                    pid: 17450,
                    ppid: 17442,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                140: {
                    cpu_percent: "0.00",
                    create_time: "2015-05-08 09:40:39",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "0.07",
                    name: "com.apple.AmbientDisplayAgent",
                    pid: 140,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "root"
                }
            },
            {
                17591: {
                    cpu_percent: "0.00",
                    create_time: "2015-05-08 20:49:05",
                    cwd: "/Users/chiyu",
                    exe: null,
                    gids: null,
                    memory_percent: "0.01",
                    name: "tmux",
                    pid: 17591,
                    ppid: 17555,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                17593: {
                    cpu_percent: "0.00",
                    create_time: "2015-05-08 20:49:05",
                    cwd: "/Users/chiyu",
                    exe: null,
                    gids: null,
                    memory_percent: "0.02",
                    name: "tmux",
                    pid: 17593,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                17594: {
                    cpu_percent: "0.00",
                    create_time: "2015-05-08 20:49:05",
                    cwd: "/Users/chiyu/workspace/agera/agera",
                    exe: null,
                    gids: null,
                    memory_percent: "0.02",
                    name: "bash",
                    pid: 17594,
                    ppid: 17593,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                190: {
                    cpu_percent: "0.00",
                    create_time: "2015-05-08 09:41:07",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "0.03",
                    name: "CrashReporterSupportHelper",
                    pid: 190,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "root"
                }
            },
            {
                193: {
                    cpu_percent: "0.00",
                    create_time: "2015-05-08 09:41:08",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "0.05",
                    name: "filecoordinationd",
                    pid: 193,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "root"
                }
            },
            {
                204: {
                    cpu_percent: "0.00",
                    create_time: "2015-05-08 09:41:08",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "2.07",
                    name: "Dock",
                    pid: 204,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                206: {
                    cpu_percent: "0.00",
                    create_time: "2015-05-08 09:41:08",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "0.30",
                    name: "SystemUIServer",
                    pid: 206,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                207: {
                    cpu_percent: "0.00",
                    create_time: "2015-05-08 09:41:08",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "1.90",
                    name: "Finder",
                    pid: 207,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                208: {
                    cpu_percent: "2.90",
                    create_time: "2015-05-08 09:41:08",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "0.12",
                    name: "coreaudiod",
                    pid: 208,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "_coreaudiod"
                }
            },
            {
                310: {
                    cpu_percent: "1.70",
                    create_time: "2015-05-08 09:41:32",
                    cwd: "/Users/chiyu/Library/Containers/com.tencent.qq/Data",
                    exe: null,
                    gids: null,
                    memory_percent: "1.98",
                    name: "QQ",
                    pid: 310,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                18235: {
                    cpu_percent: "3.90",
                    create_time: "2015-05-08 21:05:42",
                    cwd: "/Users/chiyu/workspace/agera/agera",
                    exe: null,
                    gids: null,
                    memory_percent: "0.26",
                    name: "python",
                    pid: 18235,
                    ppid: 18234,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                94: {
                    cpu_percent: "7.70",
                    create_time: "2015-05-08 09:40:38",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "2.28",
                    name: "WindowServer",
                    pid: 94,
                    ppid: 1,
                    status: "running",
                    uids: null,
                    username: "root"
                }
            },
            {
                4976: {
                    cpu_percent: "0.30",
                    create_time: "2015-05-08 11:59:20",
                    cwd: "/Users/chiyu/workspace/draenor",
                    exe: null,
                    gids: null,
                    memory_percent: "0.69",
                    name: "python",
                    pid: 4976,
                    ppid: 4966,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                4975: {
                    cpu_percent: "0.30",
                    create_time: "2015-05-08 11:59:20",
                    cwd: "/Users/chiyu/workspace/draenor",
                    exe: null,
                    gids: null,
                    memory_percent: "0.66",
                    name: "python",
                    pid: 4975,
                    ppid: 4967,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
            {
                17893: {
                    cpu_percent: "1.70",
                    create_time: "2015-05-08 20:50:37",
                    cwd: "/",
                    exe: null,
                    gids: null,
                    memory_percent: "1.92",
                    name: "Google Chrome Helper",
                    pid: 17893,
                    ppid: 17442,
                    status: "running",
                    uids: null,
                    username: "YUCHI"
                }
            },
        ]
    },
    message: "ok"
}
```

**错误码**

错误码  |  代表含义
--------|-----------------------
1000    | Koenig 服务错误
601     | 缺少必要的请求参数
602     | 参数格式错误
