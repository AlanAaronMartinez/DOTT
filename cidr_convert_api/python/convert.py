# These functions need to be implemented
import socket
import struct
from netaddr import IPAddress
import re
import ipaddress

class CidrMaskConvert:

    def cidr_to_mask(self, val):
        if int(val) >= 1 and  int(val) <= 32 
            host_bits = 32 - int(val)
            val = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
            print('LINEA: ',self, val)
            return str(val)
        else:
            return 'Invalid'
        
    def mask_to_cidr(self, val):
        try:
            val = IPAddress(val).netmask_bits()
            return val
        except:
            return 'Invalid'

class IpValidate:

    def ipv4_validation(self, val):
        try: 
            ip = ipaddress.ip_address(val) 
            return True
        except ValueError: 
            return False
