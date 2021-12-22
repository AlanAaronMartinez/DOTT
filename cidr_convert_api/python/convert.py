# These functions need to be implemented
import socket
import struct
from netaddr import IPAddress
import re

class CidrMaskConvert:

    def cidr_to_mask(self, val):
        print('LINEA: ',self, val)
        host_bits = 32 - int(val)
        val = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
        return val
        

    def mask_to_cidr(self, val):
        val = IPAddress(val).netmask_bits()
        return val

class IpValidate:

    def ipv4_validation(self, val):
        if re.match(r'^((\d{​​1,2}​​|1\d{​​2}​​|2[0-4]\d|25[0-5])\.){​​3}​​(\d{​​1,2}​​|1\d{​​2}​​|2[0-4]\d|25[0-5])$', val):  
            return True  
        return False
