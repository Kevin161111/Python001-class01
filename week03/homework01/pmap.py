import argparse

import logger
import util

import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def create_task_generator(task_type, ip_from, ip_to):
  if task_type == 'tcp':
    for int32_ip in range(ip_from, ip_to + 1):
      str_ip = util.int2ip(int32_ip)
      for port in range(1, 65535 + 1):
        yield util.is_port_open, str_ip, port
  else:
    for int32_ip in range(ip_from, ip_to + 1):
      yield util.ping_host, util.int2ip(int32_ip)


def current_run(is_proc, num_of_workers, task_generator, enable_measurement, logger):
  klass = globals()['ThreadPoolExecutor']
  if is_proc:
    klass = globals()['ProcessPoolExecutor']

  with klass(max_workers=num_of_workers) as executor:
    futures = {}
    for t in task_generator:
      func = t[0]
      args = list(t)
      args.pop(0)
      if enable_measurement:
        future = executor.submit(util.measure_time, func, *args)
      else:
        future = executor.submit(func, *args)
      futures[future] = t

    for f in concurrent.futures.as_completed(futures):
      tt = futures[f]
      ip = tt[1]
      port = 0
      if len(tt) == 3:
        port = tt[2]
      r = f.result()
      logger.log(ip, port, r[0], r[1])


def main():
  parser = argparse.ArgumentParser(description='opening port probe')
  parser.add_argument('-n', type=int, default=4, help='number of concurrent')
  parser.add_argument('-f', choices=['ping', 'tcp'], default='tcp', help='protocol, ping or tcp')
  parser.add_argument('-ip', type=str, required=True, help='ip range, e.g. 192.168.1.1-192.168.1.128')
  parser.add_argument('-w', action='count', default=0, help='write to file')
  parser.add_argument('-m', choices=['proc', 'thread'], default='proc', help='multiprocess or threading', required=False)
  parser.add_argument('-v', action='count', default=0, help='show elapsed time')
  args = parser.parse_args()
  the_logger = logger.Logger(args.w > 0)
  ip_range = util.parse_ip_range('192.168.0.1-192.168.0.1')
  task_gen = create_task_generator(args.f, ip_range[0], ip_range[1])
  current_run(args.m, args.n, task_gen, args.v > 0, the_logger)


if __name__ == '__main__':
  main()