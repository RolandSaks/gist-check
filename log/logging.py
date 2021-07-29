import logging

from cmreslogging.handlers import CMRESHandler

from config.configuration import Configuration


def es_handler(index: str, host: str, port: int) -> logging.Handler:
    return CMRESHandler(
        auth_type=CMRESHandler.AuthType.NO_AUTH,
        es_index_name=index,
        hosts=[
            {
                'host': host,
                'port': port
            }
        ])


class LoggingConfig:

    def __init__(self, configuration: Configuration, level: int = logging.INFO):
        logging.basicConfig(
            level=level,
            datefmt='%Y-%m-%d %H:%M:%S',
            format='[%(threadName)s] %(asctime)s.%(msecs)03d %(message)s'
        )

        (logging
            .getLogger()
            .addHandler(es_handler(
                configuration.property("elasticsearch.index"),
                configuration.property("elasticsearch.host"),
                configuration.property("elasticsearch.port"))))
