import json
import logging
import logging.handlers
import os
import time


class Logger(object):
  def __init__(self, enable_output_to_file):
    sl_formatter = logging.Formatter('%(asctime)s%(message)s')
    sl_handler = logging.StreamHandler()
    sl_handler.setFormatter(sl_formatter)

    sl_logger = logging.getLogger('stream_logger')
    sl_logger.setLevel(logging.INFO)
    sl_logger.addHandler(sl_handler)

    if enable_output_to_file:
      fl_formatter = logging.Formatter('%(message)s')
      if not os.path.isdir('./logs'):
        os.mkdir('./logs')
      fl_handler = logging.handlers.RotatingFileHandler('logs/log.json', maxBytes=20)
      fl_handler.setFormatter(fl_formatter)

      fl_logger = logging.getLogger('file_logger')
      fl_logger.setLevel(logging.INFO)
      fl_logger.addHandler(fl_handler)

      self.fl_logger = fl_logger

    self.sl_logger = sl_logger

  def log(self, ip, port, result, elapsed):
    msg = f'ip={ip}'
    if port != 0:
      msg = f' {msg} port={port}'
    msg = f' {msg} result={result}'
    if elapsed >= 0:
      msg = f' {msg} elapsed={elapsed}'
    self.sl_logger.info(msg)

    if self.fl_logger is not None:
      d = {'time': time.time(), 'ip': ip}
      if port != 0:
        d['port'] = port
      if elapsed >= 0:
        d['elapsed'] = elapsed

      self.fl_logger.info(json.dumps(d))