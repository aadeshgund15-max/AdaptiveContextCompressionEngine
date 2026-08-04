"""
Adaptive Context Intelligence Engine (ACIE)
Request Logger
"""

from __future__ import annotations

from datetime import datetime

from Backend.logging.logger import logger


class RequestLogger:

    def log_request(

        self,

        endpoint,

        method,

        payload=None

    ):

        logger.info(

            f"REQUEST | {method} | {endpoint}"

        )

        if payload is not None:

            logger.debug(

                payload

            )

    # ---------------------------------------------

    def log_response(

        self,

        endpoint,

        status,

        response=None

    ):

        logger.info(

            f"RESPONSE | {endpoint} | {status}"

        )

        if response is not None:

            logger.debug(

                response

            )

    # ---------------------------------------------

    def log_error(

        self,

        endpoint,

        error

    ):

        logger.error(

            f"ERROR | {endpoint}"

        )

        logger.exception(

            error

        )

    # ---------------------------------------------

    def log_execution_time(

        self,

        endpoint,

        seconds

    ):

        logger.info(

            f"{endpoint} executed in {seconds:.4f} sec"

        )


if __name__ == "__main__":

    request_logger = RequestLogger()

    request_logger.log_request(

        "/chat",

        "POST",

        {

            "query":

            "Explain ACIE"

        }

    )

    request_logger.log_response(

        "/chat",

        200,

        {

            "response":

            "Success"

        }

    )