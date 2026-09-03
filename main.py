import requests
res = requests.get("https://api.github.com")

print(f"The Status of GitHub: {res.status_code} ")