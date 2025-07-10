from openai import OpenAI
from botsquad.config import OPENAI_API_KEY
import os
from botsquad.models import BotResponse, Metadata, ChatResult

client = OpenAI(api_key=OPENAI_API_KEY)

PERSONAS = {
    "Max": "You are Max, a chill surfer who loves philosophy and slang.",
    "Luna": "You are Luna, a quiet bookworm who speaks gently and wisely.",
    "Tom": "You are Tom, a confident hacker who teases others playfully.",
}


async def get_bot_responses(user_input: str) -> ChatResult:
    replies = []
    metadata = []

    model_name = os.getenv("OPENAI_MODEL", "gpt-4o")

    for name, personality in PERSONAS.items():
        messages = [
            {"role": "system", "content": personality},
            {"role": "user", "content": user_input},
        ]

        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
        )

        reply = response.choices[0].message.content.strip()
        replies.append(BotResponse(bot=name, message=reply))
        metadata.append(Metadata(bot=name, tokens=response.usage.total_tokens))

    return ChatResult(responses=replies, metadata=metadata, model=model_name)
