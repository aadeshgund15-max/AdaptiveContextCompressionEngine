"""
Adaptive Context Intelligence Engine (ACIE)
Logger Utility
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path


class ACIELogger:

    _configured = False

    @classmethod
    def _configure(cls):

        if cls._configured:
            return

        log_folder = Path("logs")
        log_folder.mkdir(exist_ok=True)

        formatter = logging.Formatter(

            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",

            "%Y-%m-%d %H:%M:%S"

        )

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(

            log_folder / "acie.log",

            encoding="utf-8"

        )

        file_handler.setFormatter(formatter)

        root = logging.getLogger("ACIE")
        root.setLevel(logging.INFO)

        root.addHandler(console_handler)
        root.addHandler(file_handler)

        cls._configured = True

    @classmethod
    def get_logger(

        cls,

        name: str

    ):

        cls._configure()

        return logging.getLogger(f"ACIE.{name}")