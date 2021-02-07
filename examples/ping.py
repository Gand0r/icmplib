'''
    icmplib
    ~~~~~~~

    A powerful library for forging ICMP packets and performing ping
    and traceroute.

        https://github.com/ValentinBELYN/icmplib

    :copyright: Copyright 2017-2021 Valentin BELYN.
    :license: GNU LGPLv3, see the LICENSE for details.

    ~~~~~~~

    Example: ping
'''

from icmplib import ping


host = ping('1.1.1.1', count=10, interval=0.5, timeout=1)

# The IP address of the gateway or host that responded to the request
print(host.address)
# '1.1.1.1'

# The minimum round-trip time in milliseconds
print(host.min_rtt)
# 12.2

# The average round-trip time in milliseconds
print(host.avg_rtt)
# 13.2

# The maximum round-trip time in milliseconds
print(host.max_rtt)
# 17.6

# The number of packets transmitted to the destination host
print(host.packets_sent)
# 10

# The number of packets sent by the remote host and received by the
# current host
print(host.packets_received)
# 9

# Packet loss occurs when packets fail to reach their destination
# Returns a float between 0 and 1 (all packets are lost)
print(host.packet_loss)
# 0.1

# Indicates whether the host is reachable
print(host.is_alive)
# True
