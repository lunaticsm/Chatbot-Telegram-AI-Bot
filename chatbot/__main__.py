import logging
import os
from pyrogram import Client
from dotenv import load_dotenv
from chatbot.plugins.command import register_handlers

load_dotenv()

logging.basicConfig(level=logging.INFO)

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client("chatbot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


def main():
    logging.info("Starting chatbot...")
    register_handlers(app)
    app.run()


if __name__ == "__main__":
    main()
