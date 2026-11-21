import requests

response = requests.get("https://api.github.com/users/batcodegen")
data = response.json()
print(data["name"])
print(data["public_repos"])