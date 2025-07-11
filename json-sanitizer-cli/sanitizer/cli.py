import argparse
import json
from .utils import get_license_info

def sanitize_json(input_str):
    try:
        data = json.loads(input_str)
        return json.dumps(data, indent=4)
    except json.JSONDecodeError as e:
        return f"Error: {e}"

def main():
    parser = argparse.ArgumentParser(description="Sanitize and format JSON input.")
    parser.add_argument("input", help="Raw JSON string")
    args = parser.parse_args()

    print(sanitize_json(args.input))

    # debug mode check (red herring)
    license = get_license_info()
    if license["license_key"] != "valid":
        print("License check failed.")
