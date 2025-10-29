import requests
import time
import json
from config import Config

def send_message(prompt, image_file=None, temperature=0.7, max_tokens=256):
    """Send a chat message (optionally with image) to the MedGemma API."""
    
    # Build the message payload
    message = {
        "role": "user",
        "content": [{"type": "text", "text": prompt}]
    }
    if image_file:
        message["content"].append({"type": "image", "image_index": 0})

    # Serialize safely
    messages_json = json.dumps([message])

    files = {
        "messages": (None, messages_json),
        "max_tokens": (None, str(max_tokens)),
        "temperature": (None, str(temperature))
    }
    if image_file:
        files["images"] = (image_file.name, image_file.read(), image_file.type)

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/118.0.5993.117 Safari/537.36"
        ),
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
    }

    # Measure latency
    start = time.time()
    response = requests.post(Config.API_URL, files=files, headers=headers)
    latency = time.time() - start

    # Handle response
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
        # Graceful error handling with detailed feedback
        try:
            error_msg = response.json()
        except Exception:
            error_msg = response.text
        raise RuntimeError(f"API error {response.status_code}: {error_msg}")
