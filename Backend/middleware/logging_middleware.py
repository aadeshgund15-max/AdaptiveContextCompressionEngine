"""
Adaptive Context Intelligence Engine (ACIE)
Logging Middleware
"""

from __future__ import annotations

import time

from starlette.middleware.base import BaseHTTPMiddleware

from Backend.logging.logger import logger


class LoggingMiddleware(

    BaseHTTPMiddleware

):

    async def dispatch(

        self,

        request,

        call_next

    ):

        start = time.perf_counter()

        logger.info(

            f"Incoming Request : {request.method} {request.url.path}"

        )

        response = await call_next(

            request

        )

        elapsed = time.perf_counter() - start

        logger.info(

            f"Completed : {request.method} {request.url.path} | "

            f"Status : {response.status_code} | "

            f"{elapsed:.4f} sec"

        )

        return response