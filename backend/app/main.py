from fastapi import FastAPI
from app.database import Base, engine
from dotenv import load_dotenv
import app.routes.auth as auth
import app.routes.notes as notes

load_dotenv()
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(notes.router, prefix="/notes", tags=["Notes"])


@app.get("/")
def home():
    return {"message": "AI Study Assistant Running 🚀"}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)