# These functions need to be implemented
import socket
import struct
from netaddr import IPAddress
import re
import ipaddress

class CidrMaskConvert:

    def cidr_to_mask(self, val):
        print('LINEA:',  val)
        print('LINEA:',  int(val)
        if int(val) >= 1 and int(val) <= 32:
            host_bits = 32 - int(val)
            val = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
            return str(val)
        else:
            return 'Invalid'
        
    def mask_to_cidr(self, val):
        if val == '0.0.0.0':
            try:
                val = IPAddress(val).netmask_bits()
                return str(val)
            except:
                return 'Invalid'
        else: 
            return 'Invalid'

class IpValidate:

    def ipv4_validation(self, val):
        try: 
            ip = ipaddress.ip_address(val) 
            return True
        except ValueError: 
            return False
