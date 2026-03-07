import requests

response = requests.get("https://www.google.com")
print(response.status_code)  # 200이 나오면 성공!
