# Author: Nathaniel Price
# To use this, replace payload URL with any desirable server address/URL

import requests

URL = "http://127.0.0.1:6003"


def test_availability():
    print("=== Test 1: Online Service Availablity ===")
    # payload = {"url": "http://127.0.0.1:6002"}
    payload = {"server_ip": "http://127.0.0.1",
               "server_port": "6002"}

    response = requests.get(URL, json=payload)
    response_text = response.text
    response_code = int(response_text)

    print(f"Match: {response_code}")
    return


if __name__ == "__main__":
    print("\nStarting Online Service Availability Microservice Tests")
    print("---------------------------------------")

    test_availability()

    print("\nAll tests complete.")
