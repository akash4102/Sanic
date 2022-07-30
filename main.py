# from sanic import Sanic
# from sanic.response import text

# app = Sanic("MyHelloWorldApp")

# @app.get("/")
# async def hello_world(request):
#     return text("Hello, world.")

# import time

# from sanic import Request, Sanic, text


# class NanoSecondRequest(Request):
#     @classmethod
#     def generate_id(*_):
#         return time.time_ns()


# app = Sanic(..., request_class=NanoSecondRequest)


# @app.get("/")
# async def handler(request):
#     return text(str(request.id))

# from sanic import Sanic
# from sanic.response import text
# app = Sanic("MyHelloWorldApp")
# @app.get("/")
# async def hello_world(request):
#     return text("Hello, world.")
# @app.get("/foo")
# async def foo_handler(request):
#     return text("I said foo!")

import time
from sanic import Request, Sanic, text

app = Sanic("MyHelloWorldApp")

@app.get("/sync")
def sync_handler(request):
    time.sleep(1)
    return text("Done.")



