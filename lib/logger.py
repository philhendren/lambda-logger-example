import logging
import aws_lambda_logging


logger = logging.getLogger('lib')
logger.setLevel(logging.DEBUG)


def json_logger_config(event, context):
    aws_lambda_logging.setup(level='INFO',
                             aws_request_id=context.aws_request_id,
                             function=context.function_name)
