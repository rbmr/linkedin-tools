import time
from typing import List, Dict, Any

import requests


class LinkedInFetcher:
    BASE_URL = "https://api.linkedin.com/rest/memberSnapshotData"

    def __init__(self, access_token: str):
        self.access_token = access_token
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "X-Restli-Protocol-Version": "2.0.0",
            "LinkedIn-Version": "202312",  # Required header
            "Content-Type": "application/json"
        }

    def fetch_domain(self, domain: str) -> List[Dict[str, Any]]:
        """
        Fetches all data for a specific domain, handling pagination automatically.
        """
        all_elements = []
        start = 0
        count = 10  # Recommended batch size

        print(f"--- Fetching Domain: {domain} ---")

        while True:
            params = {
                "q": "criteria",
                "domain": domain,
                "start": start,
                "count": count
            }

            try:
                response = requests.get(self.BASE_URL, headers=self.headers, params=params)
                response.raise_for_status()
                data = response.json()

                # Check if we have elements
                if "elements" in data and data["elements"]:
                    # The API returns a list of elements, but usually just 1 per domain request
                    # We extract the 'snapshotData' from inside that element
                    for element in data["elements"]:
                        if "snapshotData" in element:
                            all_elements.extend(element["snapshotData"])

                # Handle Pagination
                # We check if there is a 'next' link in the paging object
                paging = data.get("paging", {})
                links = paging.get("links", [])
                has_next = any(link.get("rel") == "next" for link in links)

                if has_next:
                    print(f"   Fetching next page (current total: {len(all_elements)})...")
                    start += count
                    time.sleep(0.2)  # Be polite to the API
                else:
                    break

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 404:
                    print(f"   Note: No data exists for {domain} (404).")
                    return []
                print(f"HTTP Error on {domain}: {e}")
                break

        return all_elements