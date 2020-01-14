#!/usr/bin/env python
from lib.logger import json_logger_config, logger


def lambda_handler(event, context):
    json_logger_config(event, context)
    return True

