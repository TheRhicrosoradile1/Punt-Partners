from fastapi import Depends, FastAPI

from routes import router

app = FastAPI()


app.include_router(
    router,    
    prefix="/api/coupon-codes/v1",
    tags=["main"],
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)