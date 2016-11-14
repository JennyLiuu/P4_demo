##P4 packet filtering & ban list

====

##Demo Target:

 - packet filtering : only tcp/udp packet allow to access the network
 - ban list : When h1 sends over 10 packets, he will be banned

##Topology:



## Setup:

```bash
$ ./compile_bmv2.sh
```

## How to use:

- Start mininet topology

```bash
$ sudo ./topology.py
```

- Add entries to switch

```bash
$ ./send_cmd.sh
```

- Add entries to switch (send the ban list)

```bash
$ ./send_cmd.sh
```

- Start ./sender.py from h1 (xterm) (argv[1] is the host , argv[2] is the time to sleep)

```
# ./sender.py 1 1
```

- Start ./receiver.py from h3 (xterm) ((argv[1] is the host)

```
# ./receiver.py 3
```

