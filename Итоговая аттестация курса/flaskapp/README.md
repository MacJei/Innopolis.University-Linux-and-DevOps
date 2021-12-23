## Промежуточная аттестация

* Создайте Docker образ nginx или вашего flask приложения

* Выложите в реестр docker hub (https://hub.docker.com/) созданный образ

  * Создайте аккаунт (docker id) в докер хабе

  * Имя образа должно соответствовать формату <ваш docker id>/<имя репозитория>:<тег> Если тег не определять, то будет присвоен тег latest.  Такое имя образа можно задать сразу при сборке либо переименовать командой docker tag

  * docker push <имя образа>

* Запустите контейнер из образа

  * docker run -d -p <host port>:<container port> --name mycontainer <имя образа> (это если нужно прокидывать порты на хост. Если не нужно, то параметр -p можно не указывать)

* Приложите вывод команды docker inspect <имя контейнера>
 
 ## Запуск
 ```
$ cd flask
$ ./run.sh
$ docker login
$ docker tag flaskapp macjei/flaskapp
$ docker push macjei/flaskapp
 ```
 https://hub.docker.com/r/macjei/flaskapp/tags

 ```
 $ docker inspect flaskapp
[
    {
        "Id": "0e99fa71ad5b52b0451bacf79ee92e6ec3f5c461a1a76012cf806de9c1f1d62f",
        "Created": "2021-12-22T20:29:00.026971525Z",
        "Path": "/entrypoint.sh",
        "Args": [
            "python",
            "main.py"
        ],
        "State": {
            "Status": "exited",
            "Running": false,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 0,
            "ExitCode": 2,
            "Error": "",
            "StartedAt": "2021-12-22T20:29:04.27178403Z",
            "FinishedAt": "2021-12-22T20:29:04.381570518Z"
        },
        "Image": "sha256:a4a6638796f65e96dc61208f1a78214f4aa490994ad7ddf1fac277e70187f466",
        "ResolvConfPath": "/var/lib/docker/containers/0e99fa71ad5b52b0451bacf79ee92e6ec3f5c461a1a76012cf806de9c1f1d62f/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/0e99fa71ad5b52b0451bacf79ee92e6ec3f5c461a1a76012cf806de9c1f1d62f/hostname",
        "HostsPath": "/var/lib/docker/containers/0e99fa71ad5b52b0451bacf79ee92e6ec3f5c461a1a76012cf806de9c1f1d62f/hosts",
        "LogPath": "/var/lib/docker/containers/0e99fa71ad5b52b0451bacf79ee92e6ec3f5c461a1a76012cf806de9c1f1d62f/0e99fa71ad5b52b0451bacf79ee92e6ec3f5c461a1a76012cf806de9c1f1d62f-json.log",
        "Name": "/flaskapp",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": [
                "/home/ako/innopolis/flask:/app"
            ],
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "Capabilities": null,
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/92a552d2ab57e961e1d5805dabca722cd4091c8e74199ba0dbde8019bcdbee07-init/diff:/var/lib/docker/overlay2/2e131bf50d17f37d10206f83f172c9dcb3751cdb2fd59173728cfaf1090ac7e6/diff:/var/lib/docker/overlay2/30885e127fe50658d84628020551adbc028d9b82b57d8c0c1d2d43ebb30fe71f/diff:/var/lib/docker/overlay2/71c2f0547d2871229bbc28e89e4a519fe74e6836d85ffb16bb2d8a9bb14f7213/diff:/var/lib/docker/overlay2/a7bad3aab987b765264775ec02437b6d6e5430e8ca187cd61f930d7f9a2dfc60/diff:/var/lib/docker/overlay2/e5a9c66120f87f52c9e181b9f09d73324a2dbba9f12ce2151e20242afa599eb3/diff:/var/lib/docker/overlay2/e99518a6da741aeb9fd54421d7e2f1d0dac0350c57a2e12794231159d9895ebd/diff:/var/lib/docker/overlay2/289f2e38c7e62403454eb8c73762039d202ef7b90bfabe3b290372f6e0f0d9d7/diff:/var/lib/docker/overlay2/a155c6d3d2336b721e40f3f5766a8e93fa6b5be6917f1b57cfcc69d7fbea138b/diff:/var/lib/docker/overlay2/88915063486d6e319c1c19cd0e681c8f062297e58994aded81d6584976ce3980/diff:/var/lib/docker/overlay2/add3f0bc9ca38b1efa0a7d2d6cb2ef9a6a9394e46fcac64b9cba3c4767250944/diff:/var/lib/docker/overlay2/dd0d0bf63353b911f5b3ad201fe10921d6ba020316b7a49f9bb5478b33d8f603/diff:/var/lib/docker/overlay2/7876ba683d6b10a9ba10b134491a897c45690c13afa684ecde6d2b65a2bd69a7/diff:/var/lib/docker/overlay2/d1f8ebe57b9639edd2eaa3bc26febcfef1692f8c526d1c5edae6bafdee5db4f4/diff:/var/lib/docker/overlay2/c5755fd541b3023528caa13dcb408478f60197ef0fb1890ca8c13994f58a1ebb/diff:/var/lib/docker/overlay2/17507a1735e821b25f73e07a87e253725a682eb59b4901d6232288cfd6be84be/diff:/var/lib/docker/overlay2/bdade87cddb8b17744e5571c73af519154cb18f5d0982600e7dc2297938832f9/diff:/var/lib/docker/overlay2/257e14007423a924cd16962b5c4ca7eff2e380430177018e8c266efbccee46b8/diff:/var/lib/docker/overlay2/2d9cc95c5494fa45dea8af990e61546d6d15aa8bf05279d959587233a394b961/diff:/var/lib/docker/overlay2/5c3b639ed0f8b4d8a03fde529586e321fe96fd6aa3250c37319c98687380ef9e/diff:/var/lib/docker/overlay2/6e8684d8e3ba2994f99e912ff0c40828590fc35ba2e01e8713d4738a81a3e5ef/diff:/var/lib/docker/overlay2/72ac6982504b63d487da9c8dcc86b73b5fae3ff552beae9b707aade122b25744/diff:/var/lib/docker/overlay2/214113e0b48fdc3be6d1d87b2eae7e9a8153cfdc3009399f746ea4f752b07713/diff:/var/lib/docker/overlay2/d3773d90d2d3e0003b72dae1aef868b758aff0c5a06f63c12e75618997e48b6f/diff:/var/lib/docker/overlay2/74bb57af514d9a39b70d5ebbe301baeb4824cbcdac85250ebc64b56ae6891a04/diff:/var/lib/docker/overlay2/db8bba1c9fc265e6bcf6d114f5775362ca5c6959f62c191a5e6c4536687393b7/diff:/var/lib/docker/overlay2/463af2a6791fe0b81d2eb1fa7366ab339a221308fd62b00e6b65638c0ac8aef0/diff",
                "MergedDir": "/var/lib/docker/overlay2/92a552d2ab57e961e1d5805dabca722cd4091c8e74199ba0dbde8019bcdbee07/merged",
                "UpperDir": "/var/lib/docker/overlay2/92a552d2ab57e961e1d5805dabca722cd4091c8e74199ba0dbde8019bcdbee07/diff",
                "WorkDir": "/var/lib/docker/overlay2/92a552d2ab57e961e1d5805dabca722cd4091c8e74199ba0dbde8019bcdbee07/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [
            {
                "Type": "bind",
                "Source": "/home/ako/innopolis/flask",
                "Destination": "/app",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],
        "Config": {
            "Hostname": "0e99fa71ad5b",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "443/tcp": {},
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D",
                "PYTHON_VERSION=3.6.8",
                "PYTHON_PIP_VERSION=19.0.1",
                "UWSGI_PLUGIN=python3",
                "UWSGI_INI=/app/uwsgi.ini",
                "UWSGI_CHEAPER=2",
                "UWSGI_PROCESSES=16",
                "NGINX_MAX_UPLOAD=0",
                "NGINX_WORKER_PROCESSES=1",
                "LISTEN_PORT=80",
                "ALPINEPYTHON=python3.6",
                "STATIC_URL=/static",
                "STATIC_PATH=/var/www/app/static",
                "STATIC_INDEX=0",
                "PYTHONPATH=/app"
            ],
            "Cmd": [
                "python",
                "main.py"
            ],
            "Image": "flaskapp",
            "Volumes": null,
            "WorkingDir": "/app",
            "Entrypoint": [
                "/entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "Sebastian Ramirez <tiangolo@gmail.com>"
            }
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "9c18b4ae3943e990c5fc8513b7357df42a505f34a75c3972460a1c00851bde5c",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/9c18b4ae3943",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "",
            "Gateway": "",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "",
            "IPPrefixLen": 0,
            "IPv6Gateway": "",
            "MacAddress": "",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "26ae0c566e0a58426caad3f75d9f9c7dd4934c897ba2670b0d52d94ff54e1bb4",
                    "EndpointID": "",
                    "Gateway": "",
                    "IPAddress": "",
                    "IPPrefixLen": 0,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "",
                    "DriverOpts": null
                }
            }
        }
    }
]
```
