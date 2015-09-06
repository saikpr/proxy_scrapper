from __future__ import print_function
#import logging
import sys
from collections import Counter

from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP

from pcapng import FileScanner
from pcapng.blocks import EnhancedPacket

if __name__ == '__main__':
    f = open(str(sys.argv[1]), "rb")
    rdr = FileScanner(f)


    for block in rdr:
        # print(repr(block))

        if isinstance(block, EnhancedPacket):
            assert block.interface.link_type == 1  # must be ethernet!

            decoded = Ether(block.packet_data)
            # print(repr(Ether(block.packet_data))[:400] + '...')

            _pl1 = decoded.payload
            
            if isinstance(_pl1, IP):


                _pl2= _pl1.payload
                if isinstance(_pl2, TCP):
                    _src = '{0}:{1}'.format(_pl1.dst, _pl2.dport)
                    _dst = '{0}:{1}'.format(_pl1.src, _pl2.sport)
                    print (str("Proxy-AIP:")+ str(_src))
                    print (_pl2)

