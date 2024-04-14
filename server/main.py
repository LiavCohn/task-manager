from fastapi import FastAPI
import uvicorn
from .routers import tasks

app = FastAPI()

app.include_router(tasks.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the homepage! ww"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
