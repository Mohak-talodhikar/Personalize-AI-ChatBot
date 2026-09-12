# Zia — Voice + Text Personal Assistant

**Zia is a personal assistant for your computer. Talk to it or type, and it responds with voice + text.**
Like Alexa/Siri, but runs on your PC with a web screen.

No need to open the code to understand this project. This file gives you the full picture.

---

## What can you do with Zia?

- Ask anything: `what is photosynthesis?` → Zia answers using Google Gemini AI, with voice + on-screen chat
- Wake word: Say `Zia` to wake it (if hotword detection is running)

You interact through a simple web page with a mic button, text box, and chat history.

## Key Features

1. **Voice control** — Speak via microphone, Zia listens and speaks back
2. **Text chat** — Type if you can't speak, same answer
3. **AI answers** — Uses Gemini AI for general questions
4. **Web UI** — Clean screen with animation, chat panel, and mic button

## How to Run (4 steps)

**You need:** Windows PC, Python 3.10+, microphone, Gemini API key (free from Google AI Studio).

```bash
1. Clone the project
git clone https://github.com/Mohak182003/ChatBot_Assistant.git
cd ChatBot_Assistant

2. Install dependencies
pip install eel pyttsx3 SpeechRecognition pyaudio playsound pvporcupine google-generativeai python-dotenv pyautogui

3. Add your API key
# Create a file named .env in project root and add:
GEMINI_API_KEY=your_key_here

4. Start Zia
python run.py
```

Then open `http://localhost:8000` if it doesn't open automatically. Click mic or type in the box.

## Tech Used (in plain words)

- **Python** — main brain of Zia
- **Eel** — connects Python to the web page
- **HTML/CSS/JS + Bootstrap** — the screen you see and click
- **SpeechRecognition + Pyttsx3** — to listen and to speak (Windows voice)
- **Gemini AI** — to answer general questions

## Project Structure

```
Zia/
├── run.py          # Starts the app (UI + wake-word listener)
├── engine/         # Brain: voice, AI answers
├── web/            # Screen: index.html, style, JS
└── .env            # Your API key (you create this, never share it)
```

## Good to Know

- Works best on **Windows** (uses Windows voice).
- Microphone + internet required.
- Gemini API key is required for answers.
- Zia does **not** do phone calls, messages, YouTube, or app opening — only voice + text AI chat.

## License

MIT License — free to use, modify, and share with credit. See `LICENSE`.

## About the developer

**Mohak Talodhikar**

- [LinkedIn](https://www.linkedin.com/in/mohak-talodhikar/)
- [GitHub](https://github.com/mohaktalodhikar)
- [Instagram](https://www.instagram.com/mohak_talodhikar/)