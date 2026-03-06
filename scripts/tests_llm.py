import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3",
    "prompt": "Say hello",
    "stream": False
}

response = requests.post(url, json=payload)

print(response.json()["response"])