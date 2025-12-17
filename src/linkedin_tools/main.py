import os
from dotenv import load_dotenv
from fetch import LinkedInFetcher
from storage import DataManager
from models import (
    SnapshotElement,
    Profile,
    Position,
    Education,
    Skill,
    Publication,
    Project,
    Certification,
    Language,
    Course,
    Honor,
    VolunteeringExperience,
    Patent
)
from pydantic import ValidationError

# Load env variables
load_dotenv(verbose=True)

# List of domains to fetch [cite: 5378]
TARGET_MODELS = [
    Profile,
    Position,
    Education,
    Skill,
    Publication,
    Project,
    Certification,
    Language,
    Course,
    Honor,
    VolunteeringExperience,
    Patent
]

def main():
    token = os.environ.get("ACCESS_TOKEN")
    if not token:
        print("Error: ACCESS_TOKEN not found in environment variables.")
        return

    fetcher = LinkedInFetcher(token)
    storage = DataManager()

    for ModelClass in TARGET_MODELS:
        # Fetch
        domain = ModelClass.DOMAIN
        raw_data = fetcher.fetch_domain(domain)

        if not raw_data:
            print(f"No data found for {domain}")
            continue

        # Store (Raw Backup)
        storage.save_domain(domain, raw_data)

        # Validate (Optional but recommended for processing)
        print(f"Validating {domain}...")
        try:
            # Polymorphic instantiation
            objects = [ModelClass(**item) for item in raw_data]
            print(f"✅ Validated {len(objects)} {ModelClass.__name__} objects.")
        except ValidationError as e:
            print(f"❌ Validation failed for {ModelClass.DOMAIN}: {e}")

if __name__ == "__main__":
    main()