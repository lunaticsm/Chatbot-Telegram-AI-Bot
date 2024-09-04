from pyrogram import Client, filters
from pyrogram.types import Message
from chatbot.helpers.helper import process_ai_query

def register_handlers(app: Client):
    @app.on_message(filters.command("start"))
    async def start_handler(client: Client, message: Message):
        await message.reply_text("Welcome! Type /ai followed by your question to get an AI-generated response.")

    # Handle the /ai command
    @app.on_message(filters.command("ai"))
    async def ai_handler(client: Client, message: Message):
        query = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else None

        if not query:
            return await message.reply_text("Please provide a question after the /ai command.")

        sent_message = await message.reply_text("⏳ Processing your request...")

        response_text = await process_ai_query(query, sent_message)
        await sent_message.edit_text(response_text)