import logging
from duck_chat import DuckChat, ModelType

async def process_ai_query(query: str, sent_message):
    response_text = ""
    chunks_accumulated = 0

    try:
        async with DuckChat(model=ModelType.GPT4o) as duck_client:
            async for chunk in duck_client.ask_question_stream(query):
                response_text += chunk
                chunks_accumulated += 1

                if chunks_accumulated >= 10:
                    try:
                        await sent_message.edit_text(response_text)
                        chunks_accumulated = 0
                    except Exception as e:
                        logging.error(f"Error updating message: {e}")
                        break

        return response_text

    except Exception as e:
        logging.error(f"Error processing AI query: {e}")
        return "There was an error processing your request."