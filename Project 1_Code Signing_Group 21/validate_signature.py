from ecdsa import VerifyingKey
import hashlib
import subprocess

PRODUCT_FILE = "product.py"
SIGNATURE_FILE = "signature.sig"

# Load the public key
with open("public_key.pem", "rb") as f:
    public_key = VerifyingKey.from_pem(f.read())

# Read the product content
with open(PRODUCT_FILE, "r") as f:
    product_content = f.read()

# Load the stored signature
with open(SIGNATURE_FILE, "rb") as f:
    signature = f.read()

# Compute the hash of the product content
message_hash = hashlib.sha256(product_content.encode()).digest()

# Verify the signature
try:
    public_key.verify(signature, message_hash)
    print("✅ Code certificate valid: execution allowed")

    # Execute the product safely
    subprocess.run(["python", PRODUCT_FILE], check=True)
except:
    print("❌ Code certificate invalid: execution denied")