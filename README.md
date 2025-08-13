# Smile Education Chatbot

A recruitment-focused chatbot for Smile Education, built in Python with SOLID principles and a summary-buffer memory.  
Handles candidate onboarding, school staffing requests, and general queries.

**Live Demo:** [smilebot-quwb8h8asglm4byeybwkkf.streamlit.app](https://smilebot-quwb8h8asglm4byeybwkkf.streamlit.app/)

---

## Features

- **Three agents:** CandidateBot, SchoolBot, GeneralBot  
- **Summary buffer memory:** last 10 raw messages + rolling summary for older context  
- **Hybrid flow:** scripted onboarding + LLM for nuanced replies and stage transitions  
- **Email simulation:** structured upload forms logged to `/emails/*.json`  
- **Candidate summary:** auto-generated after onboarding, saved to `/data`

---

## Quick Start

```bash
git clone <repo_url>
cd smile-bot
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Create a `.env` file:

```
OPENAI_API_KEY=sk-...
```

### Run console version:

```bash
python cli.py
```

### Run Streamlit demo:

```bash
streamlit run app.py
```

---

## How It Works

- **ConversationManager** stores the last 10 turns and a rolling summary.  
- **Router** decides the active agent with lightweight rules + LLM fallback.  
- **Agents** handle their own prompts and logic.  
- **EmailService** logs “sent” forms locally instead of actually sending.

---

## License

Proprietary – demo for Smile Education.
