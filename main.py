from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from canvas.modules.auth import auth_repository
from canvas.modules.routers import auth

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)