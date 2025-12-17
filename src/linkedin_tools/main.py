
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]

def fetch_domain(domain_name):
    url = "https://api.linkedin.com/rest/memberSnapshotData"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "X-Restli-Protocol-Version": "2.0.0",
        "LinkedIn-Version": "202312", # This version header is required for the DMA API
        "Content-Type": "application/json"
    }

    params = {
        "q": "criteria",
        "domain": domain_name
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(response.text)
        return None

if __name__ == "__main__":
    # Example: Fetching Work History (Positions)
    print("Fetching Positions...")
    data = fetch_domain("POSITIONS")

    if data:
        # Save to file
        filename = "linkedin_positions.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Success! Data saved to {filename}")

def main():
    print("Hello from linkedin-tools!")


if __name__ == "__main__":
    main()
