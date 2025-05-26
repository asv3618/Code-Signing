## Code Signing Project - README


## Project Description
This project demonstrates code signing using ECDSA in Python to ensure software integrity and authenticity.


## Files Included:
a. Python Scripts(All files commented for clarity)
    generate_keys.py -> Generates ECDSA key pair
    sign_product.py -> Signs the product
    validate_signature.py -> Validates the product before execution
    product.py -> The signed software
    signature.sig -> The digital signature file

b. README File -> Step-by-step guide on setting up the environment


## Environment Setup
OS: Windows/Linux/MacOS
Python version: 3.x
Required libraries: ECDSA, hashlib [pip install ecdsa hashlib]
IDE: Pycharm (optional)


## Step-by-Step Instructions:
Step 1. Generate Key Pair: python generate_keys.py
This script:
    a. Generates an ECDSA key pair
    b. Stores the private key(private_key.pem) for signing
    c. Makes the public key(public_key.pem) available for validation

Step 2. Sign the Product: python sign_product.py
This script:
    a. Creates the software (product.py) – a simple Python script that prints the Student ID.
    b. Signs the file using the private key.
    c. Saves the signature (signature.sig).

Step 3. Validate the Signature and Run: python validate_signature.py
This script:
    a. Loads the public key.
    b. Verifies the product’s signature.
    c. Executes the product only if the signature is valid.


## Expected Outputs:
1. Valid signature: ✅ "Code certificate valid: execution allowed"
   I am a software made by [Student ID]

2. Tampered code: ❌ "Code certificate invalid: execution denied"


# Notes: Ensure you keep private_key.pem secret
