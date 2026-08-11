import requests

from app.core.config import MESH_API_KEY

MESH_URL = "https://api.meshapi.ai/v1/chat/completions"


def generate_recommendation(prompt: str):

    response = requests.post(
        MESH_URL,
        headers={
            "Authorization": f"Bearer {MESH_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "minimax/m2-her",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"]