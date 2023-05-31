import base64
import io
import os
import requests
from PIL import Image

# REST API https://platform.stability.ai/rest-api

#Stable Diffusion key
api_key = ""
engine_id = "stable-diffusion-v1-5"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')

if api_key is None:
    raise Exception("Missing Stability API key.")

response = requests.post(
    f"{api_host}/v1/generation/{engine_id}/text-to-image",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    },
    json={
        "text_prompts": [
            {
                "text": "NPC character image from the Harry Potter universe. Include their physical features, clothing, any magical attributes, and other relevant details."
            }
        ],
        "cfg_scale": 7,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 512,
        "width": 512,
        "samples": 1,
        "steps": 30,
    },
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

for i, image in enumerate(data["artifacts"]):

    image_data = base64.b64decode(image["base64"])
    image = Image.open(io.BytesIO(image_data))
    output_path = f"../../img/output{i}.png"
    image.save(output_path, "PNG")




