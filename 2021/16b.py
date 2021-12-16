#!/usr/bin/env python3

import sys
import os
from math import prod

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

i = 0


def parse_packet(packet):
    global i
    version = int(packet[i : i + 3], 2)
    i += 3
    type_ID = int(packet[i : i + 3], 2)
    i += 3
    # Literal
    if type_ID == 4:
        number = []
        bits = packet[i : i + 5]
        i += 5
        while bits[0] == "1":
            number.append(bits[1:])
            bits = packet[i : i + 5]
            i += 5
        number.append(bits[1:])
        number = int("".join(number), 2)
        return number
    # Operator
    else:
        subpackets = []
        length_type_ID = packet[i]
        i += 1
        if length_type_ID == "0":
            length = int(packet[i : i + 15], 2)
            i += 15
            j = i
            while i - j < length:
                subpackets.append(parse_packet(packet))
        elif length_type_ID == "1":
            number_of_subpackets = int(packet[i : i + 11], 2)
            i += 11
            for _ in range(number_of_subpackets):
                subpackets.append(parse_packet(packet))
        operator = type_ID
        if operator == 0:
            return sum(subpackets)
        elif operator == 1:
            return prod(subpackets)
        elif operator == 2:
            return min(subpackets)
        elif operator == 3:
            return max(subpackets)
        elif operator == 5:
            return int(subpackets[0] > subpackets[1])
        elif operator == 6:
            return int(subpackets[0] < subpackets[1])
        elif operator == 7:
            return int(subpackets[0] == subpackets[1])


with open(filename) as f:
    hex_packet = f.readline().strip("\n")
    packet = []
    for h in hex_packet:
        packet.append(bin(int(h, 16))[2:].zfill(4))
    packet = "".join(packet)
    print(parse_packet(packet))
