from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import time
import threading
import asyncio

import sys
sys.path.append('../')
from app import mythread as mythread
from app import myasyncio as myasyncio

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )

@app.get("/thread_test/")
async def thread_test(request: Request):
    threads = []

    t1 = mythread.CustomThread(target=mythread.watch_tv, args=(10,))
    threads.append(t1)
    t1.start()

    t2 = mythread.CustomThread(target=mythread.eat_food, args=(2,))
    threads.append(t2)
    t2.start()

    context = {
        "t1": t1.join(),
        "t2": t2.join(),
    }

    return context

@app.get("/asyncio_test/")
async def asyncio_test(request: Request):

    # 多任务并行执行
    L = await asyncio.gather(
        myasyncio.watch_tv(10,),
        myasyncio.eat_food(2,),
    )
    print(L)

    # 多任务依次执行
    watch_res = await myasyncio.watch_tv(10,)
    eat_res = await myasyncio.eat_food(2,)

    context = {
        "t1": watch_res,
        "t2": eat_res,
        "t3": L[0],
        "t4": L[1],
    }

    return context

@app.get("/")
def index():
    return {"user": ""}

if __name__ == "__main__":
    uvicorn.run(app, port=8080)