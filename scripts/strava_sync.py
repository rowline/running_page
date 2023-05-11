import argparse
import json

from config import JSON_FILE, SQL_FILE
from generator import Generator


def run_strava_sync(client_id, client_secret, refresh_token):
    generator = Generator(SQL_FILE)
    generator.set_strava_config(client_id, client_secret, refresh_token)
    # if you want to refresh data change False to True
    generator.sync(False)

    # Delete activities with distance < 4 km
    activities_list = generator.load()
    activities_list = [
        activity for activity in activities_list if activity["distance"] >= 4000
    ]

    # Save filtered activities to JSON file
    with open(JSON_FILE, "w") as f:
        json.dump(activities_list, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("client_id", help="strava client id")
    parser.add_argument("client_secret", help="strava client secret")
    parser.add_argument("refresh_token", help="strava refresh token")
    options = parser.parse_args()
    run_strava_sync(options.client_id, options.client_secret, options.refresh_token)
