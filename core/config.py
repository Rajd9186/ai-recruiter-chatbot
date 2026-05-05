import os
from ollama import Client

# Initialize client once
client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + os.getenv("OLLAMA_API_KEY")}
)

MODEL_NAME = "gpt-oss:120b-cloud"  # change if needed


def llm(prompt: str, model: str = MODEL_NAME) -> str:
    """
    Non-streaming LLM response (for API use)
    """
    try:
        response = client.chat(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]

    except Exception as e:
        return f"LLM Error: {str(e)}"


def llm_stream(prompt: str, model: str = MODEL_NAME):
    """
    Streaming generator (for future use in frontend streaming)
    """
    try:
        stream = client.chat(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=True
        )

        for part in stream:
            content = part.get("message", {}).get("content", "")
            if content:
                yield content

    except Exception as e:
        yield f"LLM Error: {str(e)}"
