# type: ignore
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.src.main import router as v1_router
from api.v1.src.models.user import UserLogged
from api.v1.src.utils.oauth import get_current_user

app = FastAPI()

origins = ["http://localhost:3000", "http://172.26.0.4:3000", "http://frontend:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(v1_router, prefix="/v1")


@app.get("/")
async def root(current_user: UserLogged = Depends(get_current_user)):
    return {"message": "Hello Bigger Applications!"}
