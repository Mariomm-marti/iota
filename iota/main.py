from fastapi import FastAPI, HTTPException


VERSION = "v1"


app = FastAPI()
number_of_requests = 0


@app.get("/")
async def root() -> dict:
    global number_of_requests
    number_of_requests += 1
    return {
        "status": "OK",
        "app": "iota",
        "repository": "https://github.com/Mariomm-marti/iota",
        "version": VERSION,
        "request_count": number_of_requests,
    }


@app.get("/health")
async def health() -> dict:
    global number_of_requests
    if number_of_requests % 2:
        raise HTTPException(status_code=500)
    return {
        "status": "OK",
    }
