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
    # Try to enrich notes by fetching a short summary from Wikipedia.
    # If Wikipedia is unreachable or doesn't have a summary, fall back to a simple template.
    topic_title = topic.strip() or "Untitled Topic"

    try:
        import requests

        url = (
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            + requests.utils.requote_uri(topic_title.replace(" ", "_"))
        )
        headers = {"User-Agent": "ai-study-assistant/1.0 (contact@example.com)"}
        r = requests.get(url, timeout=6, headers=headers)
        if r.status_code == 200:
            data = r.json()
            extract = data.get("extract", "").strip()

            if extract:
                # Build structured notes from the extract
                # Split into sentences naively
                sentences = [s.strip() for s in extract.split(". ") if s]

                definition = sentences[0].rstrip(".") if sentences else f"{topic_title} overview."

                key_concepts = []
                # use next up to 3 sentences as key concepts
                for s in sentences[1:4]:
                    key_concepts.append(s.rstrip("."))

                # If no additional sentences, try extracting common technical keywords from the extract
                if not key_concepts:
                    keywords = [
                        "hardware",
                        "software",
                        "systems",
                        "embedded",
                        "networks",
                        "algorithms",
                        "circuits",
                        "VLSI",
                        "microprocessors",
                        "computer architecture",
                    ]
                    lowered = extract.lower()
                    for kw in keywords:
                        if kw.lower() in lowered:
                            key_concepts.append(kw.capitalize())

                # Helpful generic steps
                steps = [
                    "Understand the fundamental principles and theory.",
                    "Build practical projects and hands-on experience.",
                    "Study advanced topics and recent research or applications.",
                ]

                example = ""  # Leave empty if not derivable
                if len(sentences) > 3:
                    example = sentences[3].rstrip(".")

                parts = [
                    f"Definition: {definition}",
                    "Key Concepts:",
                ]

                if key_concepts:
                    for kc in key_concepts:
                        parts.append(f"- {kc}")
                else:
                    parts.append("- (no specific concepts found)")

                parts.extend(["", "Important Steps/Process:", *[f"{i+1}. {s}" for i, s in enumerate(steps)]])

                if example:
                    parts.extend(["", "Example:", example])

                parts.extend(["", "Summary:", f"{definition}."])

                return "\n\n".join(parts)

    except Exception:
        # ignore errors and fall back to template
        pass

    # Fallback plain template
    bullets = [
        f"Definition: A brief description of {topic_title}.",
        "Key Concepts:",
        "- Core idea 1\n- Core idea 2\n- Core idea 3",
        "Important Steps/Process:",
        "1. Step one\n2. Step two\n3. Step three",
        "Example:",
        f"A short example illustrating {topic_title}.",
        "Summary:",
        f"Concise summary of {topic_title}.",
    ]

    return "\n\n".join(bullets)