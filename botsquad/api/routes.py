from fastapi import APIRouter
from botsquad.models import ChatRequest, ChatResult
from botsquad.bot_engine import get_bot_responses

router = APIRouter()


@router.post("/chat", response_model=ChatResult)
async def chat(input: ChatRequest):
    return await get_bot_responses(input.message)
