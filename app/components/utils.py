import requests
import time
import json

def send_message(prompt, image_file=None, temperature=0.7, max_tokens=512):
    # Build the message payload properly
    message = {
        "role": "user",
        "content": [{"type": "text", "text": prompt}]
    }
    if image_file:
        message["content"].append({"type": "image", "image_index": 0})

    # Serialize JSON safely
    messages_json = json.dumps([message])

    # Build form-data payload
    files = {"messages": (None, messages_json)}
    if image_file:
        files["images"] = (image_file.name, image_file.read(), image_file.type)

    start = time.time()
    response = requests.post("https://api.knoxxi.net/knoxxi-chat/api/v1/chat", files=files)
    latency = time.time() - start

    if response.status_code == 200:
        data = response.json()
        return {
            "text": data["response"],
            "model": data["version"],
            "latency": latency,
            "tokens": data.get("tokens_used"),
            "disclaimer": data.get("disclaimer"),
        }
    else:
        raise RuntimeError(f"API error {response.status_code}: {response.text}")
