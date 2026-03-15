#main.py
import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    #Before message
    print("Before Message:")
    print("HTTP Method: ", request.method)
    print("URL path: ", request.url)
    response = await call_next(request)
    #After message
    print("After Message:")
    print("URL path: ", request.url)
    print("Status Code: ", response.status_code)

    return response

#404 Exception Handler
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={"message": "The requested resource was not found"},
    )

@app.get("/hello")
def hello_message():
    return {"message": "Hello, FastAPI!"}