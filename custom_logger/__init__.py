# -*- coding: utf-8 -*-

import logging
import datetime

from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        dt_now = datetime.datetime.now()
        super().add_fields(log_record, record, message_dict)
        log_record['level'] = record.levelname
        log_record['cursor'] = f'{record.pathname}#L{record.lineno}'
        log_record['timestamp'] = dt_now.strftime('%Y/%m/%d %H:%M:%S')


def init_logger():
    handler = logging.StreamHandler()
    formatter = CustomJsonFormatter()
    handler.setFormatter(formatter)
    root = logging.getLogger()
    # aion のハンドラを除去
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(logging.DEBUG)
