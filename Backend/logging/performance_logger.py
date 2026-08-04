"""
Adaptive Context Intelligence Engine (ACIE)
Performance Logger
"""

from __future__ import annotations

import time

from Backend.logging.logger import logger


class PerformanceLogger:

    def __init__(

        self

    ):

        self.start_time = None

        self.operation = None

    # ---------------------------------------------

    def start(

        self,

        operation

    ):

        self.operation = operation

        self.start_time = time.perf_counter()

        logger.info(

            f"Started : {operation}"

        )

    # ---------------------------------------------

    def stop(

        self

    ):

        if self.start_time is None:

            return None

        elapsed = (

            time.perf_counter()

            - self.start_time

        )

        logger.info(

            f"Completed : {self.operation} | {elapsed:.4f} sec"

        )

        self.start_time = None

        return elapsed

    # ---------------------------------------------

    def measure(

        self,

        operation,

        function,

        *args,

        **kwargs

    ):

        self.start(

            operation

        )

        result = function(

            *args,

            **kwargs

        )

        self.stop()

        return result


if __name__ == "__main__":

    performance = PerformanceLogger()

    performance.start(

        "Demo"

    )

    time.sleep(1)

    performance.stop()