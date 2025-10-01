import requests

url = "https://www.sofascore.com/api/v1/unique-tournament/7/season/76953/team-events/total"
headers = {
    "user-agent": "Mozilla/5.0",
    "accept": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("✅ Données récupérées :")
    print(data)
else:
    print(f"❌ Erreur: {response.status_code} {response.text}")
