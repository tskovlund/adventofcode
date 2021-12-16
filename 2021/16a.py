#!/usr/bin/env python3

import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

DEBUG = True

i = 0
version_sum = 0


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def parse_packet(packet):
    global i, version_sum
    version = int(packet[i : i + 3], 2)
    dprint("Version", version)
    version_sum += version
    i += 3
    type_ID = int(packet[i : i + 3], 2)
    dprint("Type ID", type_ID)
    i += 3
    # Literal
    if type_ID == 4:
        dprint("Literal")
        number = []
        bits = packet[i : i + 5]
        i += 5
        while bits[0] == "1":
            number.append(bits[1:])
            bits = packet[i : i + 5]
            i += 5
        number.append(bits[1:])
        number = int("".join(number), 2)
        dprint(number)
    # Operator
    else:
        dprint("Operator")
        length_type_ID = packet[i]
        dprint("Length Type ID", length_type_ID)
        i += 1
        if length_type_ID == "0":
            length = int(packet[i : i + 15], 2)
            dprint("Length", length)
            i += 15
            j = i
            while i - j < length:
                parse_packet(packet)
        elif length_type_ID == "1":
            number_of_subpackets = int(packet[i : i + 11], 2)
            dprint("Number of Subpackets", number_of_subpackets)
            i += 11
            for _ in range(number_of_subpackets):
                parse_packet(packet)


with open(filename) as f:
    hex_packet = f.readline().strip("\n")
    packet = []
    for h in hex_packet:
        packet.append(bin(int(h, 16))[2:].zfill(4))
    packet = "".join(packet)
    dprint(packet)
    parse_packet(packet)
    print(version_sum)
