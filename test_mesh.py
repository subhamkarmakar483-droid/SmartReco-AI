import requests

from app.core.config import MESH_API_KEY

response = requests.get(
    "https://api.meshapi.ai/v1/models",
    headers={
        "Authorization": f"Bearer {MESH_API_KEY}"
    },
    params={
        "free": "true"
    }
)

print("STATUS:", response.status_code)

if response.status_code == 200:
    models = response.json()

    print("\nFREE MODELS:\n")

    for model in models:
        print(model.get("id"))

else:
    print("ERROR:")
    print(response.text)