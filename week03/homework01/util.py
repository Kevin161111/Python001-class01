import socket
import struct
import re
import time

from ping3 import ping


def is_port_open(ip: str, port: int) -> bool:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(5)
  loc = (ip, port)
  result = s.connect_ex(loc)
  s.close()
  return result == 0


def ping_host(ip):
  result = ping(ip, timeout=1)
  return type(result) == float and result > 0.0


def ip2int(addr):
  return struct.unpack("!I", socket.inet_aton(addr))[0]


def int2ip(addr):
  return socket.inet_ntoa(struct.pack("!I", addr))


def parse_ip_range(ip_range):
    matches = re.match(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\-"
                       r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$", ip_range)
    if matches is None:
      raise ValueError('bad format of ip range')

    ips = matches.groups()
    ip_int32_from = ip2int(ips[0])
    ip_int32_to = ip2int(ips[1])
    if ip_int32_from > ip_int32_to:
      raise ValueError('bad ip range')

    return ip_int32_from, ip_int32_to


def measure_time(func, *args):
  start_time = time.time()
  ret = func(*args)
  elapsed = time.time() - start_time
  return ret, elapsed