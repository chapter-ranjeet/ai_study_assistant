from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from app.database import get_db
from app.models.note import Note
from app.models.user import User
from app.schemas.ai_schema import NotesRequest, NotesResponse
from app.utils.security import verify_token
from app.services.ai_service import generate_notes

router = APIRouter()

# 🔐 OAuth2 setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


# ✅ AUTH FUNCTION
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    return payload


# ✅ GENERATE NOTES
@router.post("/generate", response_model=NotesResponse)
def generate_notes_api(
    request: NotesRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    # 🔹 Get topic from request
    topic = request.topic

    # 🔹 Extract email from JWT token
    email = user.get("sub")

    # 🔹 Get actual user from DB
    db_user = db.query(User).filter(User.email == email).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # 🔹 Generate AI content
    content = generate_notes(topic)

    # 🔹 Save to database
    new_note = Note(
        topic=topic,
        content=content,
        user_id=db_user.id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    # 🔹 Return response
    return {"content": content}


# ✅ GET NOTES HISTORY
@router.get("/history")
def get_notes(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    # 🔹 Extract email from token
    email = user.get("sub")

    # 🔹 Get DB user
    db_user = db.query(User).filter(User.email == email).first()

    if not db_user:
        return []

    # 🔹 Fetch notes
    notes = db.query(Note).filter(Note.user_id == db_user.id).all()

    return notes

from fastapi.responses import StreamingResponse

@router.post("/generate-stream")
def generate_notes_stream(request: NotesRequest, user=Depends(get_current_user)):
    
    def stream():
        topic = request.topic

        # 👉 Fake streaming (replace with real AI later)
        text = f"Generating notes for {topic}...\n\nThis is a sample AI response."

        for word in text.split():
            yield word + " "
            import time
            time.sleep(0.05)  # typing effect

    return StreamingResponse(stream(), media_type="text/plain")