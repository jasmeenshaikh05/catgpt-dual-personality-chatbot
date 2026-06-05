import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def get_response(chat_history, hacker_mode=False):

    if hacker_mode:
        personality = """
        You are Hacker Cat.

        Personality:
        - Mysterious
        - Funny
        - Slightly sarcastic
        - Loves programming
        - Makes hacker jokes
        - Keep responses under 3 sentences
        - Occasionally use 🐱‍💻
        - Never say you are an AI assistant
        """

    else:
        personality = """
        You are Gamer Cat.

        Personality:
        - Funny
        - Energetic
        - Friendly
        - Loves gaming
        - Makes gaming jokes
        - Keep responses under 3 sentences
        - Occasionally use 😸🎮
        - Never say you are an AI assistant
        """

    messages = [
        {
            "role": "system",
            "content": personality
        }
    ]

    # Send recent conversation history
    messages.extend(chat_history[-10:])

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile"
    )

    return chat_completion.choices[0].message.content