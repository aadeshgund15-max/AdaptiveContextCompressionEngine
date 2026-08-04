"""
Adaptive Context Intelligence Engine (ACIE)
Central Logger
"""

from __future__ import annotations

import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler


class Logger:

    _logger = None

    @classmethod
    def get_logger(

        cls,

        name="ACIE"

    ):

        if cls._logger is not None:

            return cls._logger

        log_directory = Path("logs")

        log_directory.mkdir(

            exist_ok=True

        )

        log_file = log_directory / "acie.log"

        logger = logging.getLogger(

            name

        )

        logger.setLevel(

            logging.DEBUG

        )

        formatter = logging.Formatter(

            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

        )

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(

            formatter

        )

        file_handler = RotatingFileHandler(

            log_file,

            maxBytes=5 * 1024 * 1024,

            backupCount=5,

            encoding="utf-8"

        )

        file_handler.setFormatter(

            formatter

        )

        if not logger.handlers:

            logger.addHandler(

                console_handler

            )

            logger.addHandler(

                file_handler

            )

        logger.propagate = False

        cls._logger = logger

        return logger


logger = Logger.get_logger()


if __name__ == "__main__":

    logger.debug("Debug")

    logger.info("Information")

    logger.warning("Warning")

    logger.error("Error")

    logger.critical("Critical")