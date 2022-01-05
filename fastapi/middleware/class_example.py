import time

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.applications import Starlette


class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        print(type(response))
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response


app = FastAPI()

app.add_middleware(CustomMiddleware)


@app.get("/")
async def get_root():
    return "hello"
