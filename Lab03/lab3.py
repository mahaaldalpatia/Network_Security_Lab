import hmac
import hashlib
import secrets
import time

# Shared secret key
secret_key = b"mysecret"

# Store used nonces
used_nonces = set()

# Response validity time
MAX_AGE_SECONDS = 5


def generate_challenge():
    return secrets.token_hex(16)


def generate_response(challenge, timestamp):
    message = f"{challenge}:{timestamp}".encode()

    return hmac.new(
        secret_key,
        message,
        hashlib.sha256
    ).hexdigest()


def verify_response(challenge, timestamp, response):
    current_time = time.time()

    # Check timestamp
    if current_time - timestamp > MAX_AGE_SECONDS:
        print("Authentication Failed: Response expired")
        return False

    # Check whether nonce was already used
    if challenge in used_nonces:
        print("Authentication Failed: Replay attack detected")
        return False

    # Generate expected response
    expected_response = generate_response(challenge, timestamp)

    # Secure comparison
    if hmac.compare_digest(response, expected_response):
        used_nonces.add(challenge)
        print("Authentication Successful")
        return True

    print("Authentication Failed: Invalid response")
    return False


# Server generates a challenge
challenge = generate_challenge()
timestamp = time.time()

print("Server Challenge:", challenge)

# Client generates response
response = generate_response(challenge, timestamp)

print("Client Response:", response)

# First verification
print("\nFirst Authentication:")
verify_response(challenge, timestamp, response)

# Replay attack simulation
print("\nReplay Attack Simulation:")
verify_response(challenge, timestamp, response)

# Delayed response simulation
print("\nDelayed Response Simulation:")
old_timestamp = time.time() - 10
old_response = generate_response(challenge + "new", old_timestamp)

verify_response(challenge + "new", old_timestamp, old_response)