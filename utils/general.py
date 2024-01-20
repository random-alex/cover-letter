from urllib.parse import urlparse

import requests

from utils.config import OPENAI_API_ENDPOINT


def get_local_gpt_api_key() -> str | None:
    try:
        from utils.gpt_api import GPT_API_KEY
        return GPT_API_KEY
    except Exception:
        print('No openAI key submitted! Please provide key')
        return None


def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def is_valid_openai_api_key(api_key: str):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(OPENAI_API_ENDPOINT, headers=headers)

    return response.status_code == 200
