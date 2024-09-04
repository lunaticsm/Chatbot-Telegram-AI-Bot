
# Chatbot Telegram AI Bot

A simple yet powerful AI-based Telegram bot built using Pyrogram and DuckChat. This bot responds to user queries via the `/ai` command and streams the response in real-time using the GPT-4o mini model.

## Features

- **/start command**: Welcomes users and explains how to use the bot.
- **/ai command**: Allows users to ask questions, and the bot will reply using AI-powered responses.
- **Real-time response streaming**: Users see the answer to their queries updated as the response is processed.

## Prerequisites

- Python 3.12
- A Telegram bot API token from [BotFather](https://t.me/BotFather)
- DuckChat library from [github.com/lunaticsm/duck_chat](https://github.com/lunaticsm/duck_chat)

## Installation

### Ubuntu

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lunaticsm/Chatbot-Telegram-AI-Bot.git
   cd chatbot
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your credentials:
   ```bash
   API_ID=your_api_id
   API_HASH=your_api_hash
   BOT_TOKEN=your_bot_token
   ```

5. **Run the bot**:
   ```bash
   python3 -m chatbot
   ```

### Windows

1. **Clone the repository**:
   Open a terminal (CMD, PowerShell, or Git Bash) and run:
   ```bash
   git clone https://github.com/lunaticsm/Chatbot-Telegram-AI-Bot.git
   cd chatbot
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your credentials:
   ```bash
   API_ID=your_api_id
   API_HASH=your_api_hash
   BOT_TOKEN=your_bot_token
   ```

5. **Run the bot**:
   ```bash
   python -m chatbot
   ```

### Heroku

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lunaticsm/Chatbot-Telegram-AI-Bot.git
   cd chatbot
   ```

2. **Create a `requirements.txt` and `Procfile`**:
   Ensure your repository contains a `requirements.txt` and a `Procfile`.

   **Procfile**:
   ```
   worker: python -m chatbot
   ```

3. **Deploy to Heroku**:
   ```bash
   heroku create
   git push heroku main
   ```

4. **Set up environment variables** on Heroku:
   ```bash
   heroku config:set API_ID=your_api_id
   heroku config:set API_HASH=your_api_hash
   heroku config:set BOT_TOKEN=your_bot_token
   ```

5. **Run the bot**:
   Heroku will automatically run the bot after deployment.

---

## Requirements

Create a `requirements.txt` file with the following content:

```bash
pyrogram
python-dotenv
git+https://github.com/lunaticsm/duck_chat
```

This includes Pyrogram, dotenv for environment variable management, and DuckChat library from GitHub.

---

## Support

If you need assistance or have any questions, feel free to reach out on Telegram: [@alterbase2](https://t.me/alterbase2).

---

## License

This project is licensed under the MIT License.
