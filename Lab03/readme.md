# Simulate User Authentication and Replay Attack Handling

## Aim

To develop a basic challenge-response authentication system using Python and simulate replay attack detection using a nonce.

## Objective

* Understand challenge-response authentication.
* Generate a random nonce for authentication.
* Verify user identity using a shared secret key.
* Detect replay attacks by preventing nonce reuse.

## Theory

Challenge-response authentication is a protocol in which a server sends a random challenge to a client. The client generates a response using the challenge and a shared secret key. The server verifies the response to authenticate the user.

A nonce is a random value used only once. It helps prevent replay attacks, where an attacker captures and reuses a previously valid authentication response.

## Requirements

* Python 3.x
* `hashlib` and `secrets` libraries (built-in)

## Working

1. The server generates a random nonce.
2. The client creates a SHA-256 response using the nonce and shared secret key.
3. The server verifies the response.
4. The server stores the used nonce.
5. If the same nonce is submitted again, a replay attack is detected.

## Execution

Run the Python program using:

```bash
python challenge_response.py
```

## Expected Output

```text
Authentication Successful

Replay Attack Simulation
Replay Attack Detected
```

## Result

A basic challenge-response authentication system was implemented successfully, and replay attack detection was simulated using nonce tracking.

## Conclusion

The experiment demonstrates how a nonce and shared secret can be used to authenticate a user and prevent reuse of a previously accepted authentication response.
