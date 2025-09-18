from fastapi import FastAPI
from routers import food_router, deserts_router, order_router
import uvicorn

app = FastAPI()
app.include_router(food_router)
app.include_router(deserts_router)
app.include_router(order_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

