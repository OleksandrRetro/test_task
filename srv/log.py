import logging
from pathlib import Path


class SrvLogger:
    """
    Logging config class.
    """
    LOG_FILE_PATH = Path(__file__).parent.parent.joinpath("logs/")

    def __add_stream_handler(self, logger: logging) -> logging:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))
        stream_handler.setLevel(logging.DEBUG)
        logger.addHandler(stream_handler)
        return logger

    def __add_file_handler(self, logger: logging, file_name: str) -> logging:
        file_handler = logging.FileHandler(self.LOG_FILE_PATH.joinpath(file_name), mode='w')
        file_handler.setFormatter(logging.Formatter(
            fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M'))
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        return logger

    def create_logger(self, caller_name: str, file_name: str) -> logging:
        logger = logging.getLogger(caller_name)
        logger.setLevel(logging.DEBUG)
        self.__add_file_handler(logger=logger, file_name=file_name)
        self.__add_stream_handler(logger=logger)
        return logger
