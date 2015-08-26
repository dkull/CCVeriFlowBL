#  ??
#  2|1430255191|268|1430255191|268|6|0|0|0|1412602831|52128|0|0|0|3650244206|6667|3249|49604|785|745|16|0|1|40
#  2|1430255238|209|1430255238|209|6|0|0|0|1440153565|6697|0|0|0|1489274366|50624|6724|3249|631|688|24|16|1|710
#  Date flow start          Duration Proto      Src IP Addr:Port          Dst IP Addr:Port   Flags Tos  Packets    Bytes      pps      bps    Bpp Flows
#  2015-04-29 00:06:31.268     0.000 TCP      84.50.155.207:52128 ->   217.146.78.110:6667  .A....   0        1       40        0        0     40     1
#  2015-04-29 00:07:18.209     0.000 TCP     85.214.255.221:6697  ->   88.196.133.254:50624 .AP...  16        1      710        0        0    710     1

import datetime

def parseLine(line):
    s = line.split("|")

    if len(s) != 24:
        return

    timestamp_s = s[1]
    timestamp_f = s[3]
    proto = s[5]
    srcip = s[9]
    srcport = s[10]
    dstpip = s[14]
    dstport = s[15]
    bytes = s[23]

    return {
        "timestamp_s": timestamp_s,
        "timestamp_f":timestamp_f,
        "proto": proto,
        "srcip": srcip,
        "srcport": srcport,
        "dstpip": dstpip,
        "dstport": dstport,
        "bytesy": bytes
    }
