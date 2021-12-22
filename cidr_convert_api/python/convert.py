# These functions need to be implemented
import socket
import struct
from netaddr import IPAddress
from IPy import IP

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
        try:
            IP(val)
            return True
        except:
            return False
