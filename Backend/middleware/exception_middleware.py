"""
Adaptive Context Intelligence Engine (ACIE)
Exception Middleware
"""

from __future__ import annotations

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

from Backend.logging.logger import logger


class ExceptionMiddleware(

    BaseHTTPMiddleware

):

    async def dispatch(

        self,

        request,

        call_next

    ):

        try:

            return await call_next(

                request

            )

        except Exception as error:

            logger.exception(

                error

            )

            return JSONResponse(

                status_code=500,

                content={

                    "success": False,

                    "error": type(error).__name__,

                    "message": str(error)

                }

            )