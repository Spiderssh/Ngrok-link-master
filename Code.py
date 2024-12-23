import requests
import json
import argparse

def get_ngrok_url():
    """Fetches the public URL from the Ngrok API."""
    try:
        response = requests.get("http://127.0.0.1:4040/api/tunnels")
        tunnels = response.json().get('tunnels', [])
        if tunnels:
            return tunnels[0].get('public_url')
        else:
            print("No active tunnels found. Ensure Ngrok is running.")
    except Exception as e:
        print(f"Error fetching Ngrok URL: {e}")
        return None

def mask_url(public_url, service="tinyurl"):
    """Masks the Ngrok URL using a chosen shortening service."""
    try:
        if service == "tinyurl":
            response = requests.get(f"http://tinyurl.com/api-create.php?url={public_url}")
            if response.status_code == 200:
                return response.text
        # Add other URL masking services here.
    except Exception as e:
        print(f"Error masking URL: {e}")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mask an Ngrok link to a public URL.")
    parser.add_argument("--service", type=str, default="tinyurl", help="URL masking service (default: tinyurl).")
    args = parser.parse_args()

    ngrok_url = get_ngrok_url()
    if ngrok_url:
        masked_url = mask_url(ngrok_url, service=args.service)
        if masked_url:
            print(f"Ngrok URL: {ngrok_url}")
            print(f"Masked URL: {masked_url}")
        else:
            print("Failed to mask URL.")
    else:
        print("Ngrok is not running.")
