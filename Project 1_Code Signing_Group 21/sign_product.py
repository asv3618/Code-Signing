from ecdsa import SigningKey
import hashlib

STUDENT_ID = "11691714"
PRODUCT_FILE = "product.py"
SIGNATURE_FILE = "signature.sig"

# Load private key
with open("private_key.pem", "rb") as f:
    private_key = SigningKey.from_pem(f.read())

# Create the product (software)
product_content = f'print("I am a software made by {STUDENT_ID}")\n'
with open(PRODUCT_FILE, "w") as f:
    f.write(product_content)

# Sign the product file
message_hash = hashlib.sha256(product_content.encode()).digest()
signature = private_key.sign(message_hash)

# Save the signature
with open(SIGNATURE_FILE, "wb") as f:
    f.write(signature)

print("✅ Product signed successfully. Signature saved in 'signature.sig'")