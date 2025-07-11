def _decode_secret(hex_str):
    return bytes.fromhex(hex_str).decode('utf-8')

def get_license_info():
    # Legacy license handler – deprecated
    data = {
        "license_key": "valid",
        "secret": _decode_secret("6c6f6750407273657232303234") 
    }
    return data
