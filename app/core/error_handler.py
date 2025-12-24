from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            return await call_next(request)
        except Exception:
            return JSONResponse(
                status_code = 500,
                content = {
                    'success' : False,
                    'message' : 'Internal server error'
                }
            )
            