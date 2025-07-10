from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class BotResponse(BaseModel):
    bot: str
    message: str


class Metadata(BaseModel):
    bot: str
    tokens: int


class ChatResult(BaseModel):
    responses: list[BotResponse]
    metadata: list[Metadata]
    model: str
