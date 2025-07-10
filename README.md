# 🧠 BotSquad

**BotSquad** is a lightweight chat application where you can talk to a group of AI bots, each with a unique personality. The goal is to explore multi-agent interaction using modern LLM APIs and build toward contextual memory, personalization, and simple UI integration.

- 👥 Multi-bot personalities (Max, Luna, Tom)
- 💬 Single API endpoint (`/chat`) to talk with all bots
- 🔐 API key-based access to OpenAI models
- 📦 Modular code using FastAPI, Pydantic models, and clean architecture

---

## 🛠 Tech Stack

| Layer        | Tech Used              | Purpose |
|--------------|------------------------|---------|
| Backend      | **FastAPI**            | Web framework for building APIs |
| Models       | **Pydantic**           | Request and response validation |
| LLM API      | **OpenAI GPT-4o**      | Chatbot intelligence |
| Env Config   | **Python `os` / dotenv** | Load OpenAI key and configs |
| Project Mgmt | **Poetry**             | Dependency management and virtualenv |
| Dev Tools    | **PyCharm + Black**    | Code formatting and development |

---

## ▶️ Getting Started

```bash
# Install dependencies
poetry install

# Set your OpenAI key
echo "OPENAI_API_KEY=your-key-here" > .env

# Run FastAPI backend
poetry run uvicorn botsquad.main:app --reload

# (Optional) Start Gradio UI if added later
# poetry run python ui.py
```

---

## ✅ TODO

- [x] FastAPI `/chat` endpoint
- [x] ChatRequest and ChatResult models
- [x] Basic bot personalities using GPT
- [ ] Memory integration with Redis
- [ ] Token usage logging per session
- [ ] Gradio UI frontend
- [ ] Unit and integration tests
- [ ] Deploy to Render or Fly.io
- [ ] Persistent chat history using PostgreSQL
- [ ] WebSocket support for streaming responses

---

## 📁 Project Structure

```
botsquad/
├── api/               # FastAPI routes
│   └── routes.py
├── bot_engine.py      # LLM and personality logic
├── config.py          # Load secrets
├── main.py            # FastAPI app entry point
├── models.py          # Pydantic models
├── __init__.py
```

---

## ✨ License

MIT — use it freely, contribute if you like!
