"""
Adaptive Context Intelligence Engine (ACIE)
Environment Configuration
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


class Environment:

    def __init__(self):

        self.root_directory = Path.cwd()

        self.env_file = self.root_directory / ".env"

        if self.env_file.exists():

            load_dotenv(self.env_file)

    # -------------------------------------------------
    # Get Environment Variable
    # -------------------------------------------------

    def get(

        self,

        key,

        default=None

    ):

        return os.getenv(

            key,

            default

        )

    # -------------------------------------------------
    # Exists
    # -------------------------------------------------

    def exists(

        self,

        key

    ):

        return key in os.environ

    # -------------------------------------------------
    # Required Variable
    # -------------------------------------------------

    def required(

        self,

        key

    ):

        value = os.getenv(

            key

        )

        if value is None:

            raise RuntimeError(

                f"Missing environment variable : {key}"

            )

        return value


environment = Environment()