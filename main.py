import time
from fastapi import FastAPI, HTTPException, APIRouter,Request
from starlette.middleware.cors import CORSMiddleware  # CORSを回避するために必要
# from routers import test,auth,item
from routers import test, auth

app = FastAPI()


# CORSを回避するために設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(test.router)
app.include_router(auth.router)
# app.include_router(item.router)

