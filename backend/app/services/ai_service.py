import requests
from app.config import settings

OPENROUTER_API_KEY = settings.OPENROUTER_API_KEY

def generate_notes(topic: str):
    # Try calling OpenRouter; if it fails (network/timeouts/etc.)
    # fall back to a local simple notes generator so the app remains usable.
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f"Generate notes for {topic}"
                }
            ]
        }

        # short timeout to fail fast when external network is unavailable
        response = requests.post(url, headers=headers, json=data, timeout=8)

        result = response.json()

        print("AI RESPONSE:", result)

        return result.get("choices", [{}])[0].get("message", {}).get("content", "AI failed")

    except Exception as e:
        print("AI ERROR:", str(e))
        # Local fallback generator
        return _local_generate_notes(topic)


def _local_generate_notes(topic: str) -> str:
    # Simple template-based notes generator as a fallback when API is unreachable
    topic_title = topic.strip().capitalize() or "Untitled Topic"
    bullets = [
        f"Definition: A brief description of {topic_title}.",
        "Key Concepts:",
        "- Core idea 1\n- Core idea 2\n- Core idea 3",
        "Important Steps/Process:",
        "1. Step one\n2. Step two\n3. Step three",
        "Example:",
        f"A short example illustrating {topic_title}.",
        "Summary:",
        f"Concise summary of {topic_title}."
    ]

    return "\n\n".join(bullets)