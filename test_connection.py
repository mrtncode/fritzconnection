import os
from dotenv import load_dotenv
from fritzconnection import FritzConnection

load_dotenv()

address = os.getenv("FRITZ_ADDRESS")
user = os.getenv("FRITZ_USER")
password = os.getenv("FRITZ_PASSWORD")

print(f"Address: {address}")
print(f"User: {user}")
print(f"Password: {'*' * len(password) if password else 'None'}")

try:
    fc = FritzConnection(
        address=address,
        user=user,
        password=password
    )
    print("\n✓ Connection successful!")
    print(f"Device: {fc.device_name}")
except Exception as e:
    print(f"\n✗ Connection failed: {e}")
