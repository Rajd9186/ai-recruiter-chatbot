from ollamafreeapi import OllamaFreeAPI

# Initialize client ONCE (singleton style)
client = OllamaFreeAPI()


def llm(prompt: str, model: str = "llama2"):
    """
    Generic LLM function to generate responses
    """

    try:
        response = client.chat(
            model_name=model,
            prompt=prompt,
            temperature=0.7,
            num_predict=256
        )
        return response

    except Exception as e:
        return f"LLM Error: {str(e)}"