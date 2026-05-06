import requests
from app.config import settings

OPENROUTER_API_KEY = settings.OPENROUTER_API_KEY

def generate_notes(topic: str):
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

        response = requests.post(url, headers=headers, json=data)

        result = response.json()

        print("AI RESPONSE:", result)  # 👈 VERY IMPORTANT

        # ✅ SAFE RETURN
        return result.get("choices", [{}])[0].get("message", {}).get("content", "AI failed")

    except Exception as e:
        print("AI ERROR:", str(e))
        return f"Error generating notes for {topic}"