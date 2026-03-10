from fastapi import APIRouter
from schemas.chat_schema import ChatRequest
from services.llm_service import generate_response

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    response = generate_response(request.message)

    return {"response": response}