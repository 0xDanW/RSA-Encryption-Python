import rsa


# First time key generation
# public_key, private_key = rsa.newkeys(1024)

# with open("public.pem", "wb") as f:
#     f.write(public_key.save_pkcs1("PEM"))

# with open("private.pem", "wb") as f:
#     f.write(private_key.save_pkcs1("PEM"))

with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())


# RSA encryption PoC
message = "My password is Daniel_123"
encrypted_message = rsa.encrypt(message.encode(), public_key)


# RSA decryption PoC
encrypted_message = open("encrypted.message", "rb").read()
clear_message = rsa.decrypt(encrypted_message, private_key)


# Signature generation
signature = rsa.sign(message.encode, private_key, "SHA-256")
with open("signature", "rb") as f:
    f.write(signature)


# Signature verification
print(rsa.verify(message.encode, signature, public_key))