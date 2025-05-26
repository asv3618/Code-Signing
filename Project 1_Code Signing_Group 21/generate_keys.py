from ecdsa import SigningKey, NIST256p

# Generate an ECDSA key pair
private_key = SigningKey.generate(curve=NIST256p)
public_key = private_key.get_verifying_key()

# Save the private key securely
with open("private_key.pem", "wb") as f:
    f.write(private_key.to_pem())

# Save the public key for verification
with open("public_key.pem", "wb") as f:
    f.write(public_key.to_pem())

print("✅ Keys generated successfully: 'private_key.pem' and 'public_key.pem'")