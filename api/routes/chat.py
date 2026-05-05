from fastapi import APIRouter
from models.request import ChatRequest
from models.response import ChatResponse
from services.chat_service import ChatService

router = APIRouter()

@router.post("/")
def chat(req: ChatRequest):
    answer = ChatService().get_response(req.question)
    return ChatResponse(answer=answer)