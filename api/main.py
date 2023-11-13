from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware


from src.models.user import UserLogged
from src.main import router as v1_router
from src.utils.oauth import get_current_user



app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(v1_router, prefix="/v1")

@app.get("/")
async def root(current_user:UserLogged = Depends(get_current_user)):
    return {"message": "Hello Bigger Applications!"}

