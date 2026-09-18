# Generate and Verify X.509 Self-Signed Digital Certificate

## Aim

To generate a self-signed X.509 digital certificate using OpenSSL, inspect its structure, and verify the certificate.

## Requirements

- Windows 10/11
- OpenSSL
- Command Prompt

## Theory

An **X.509 certificate** is a digital certificate that contains identity information and a public key.

A **self-signed certificate** is signed using its own private key instead of a Certificate Authority (CA). It is commonly used for testing, development, and laboratory experiments.

## Procedure

### 1. Check OpenSSL Installation

```cmd
openssl version
```

### 2. Generate a 2048-bit RSA Private Key

```cmd
openssl genrsa -out private.key 2048
```

This creates `private.key`. The private key must be kept secret.

### 3. Generate a Self-Signed X.509 Certificate

```cmd
openssl req -x509 -new -key private.key -sha256 -days 365 -out certificate.crt
```

Enter the requested certificate information. For example:

```text
Country Name: IN
State: Delhi
Locality: Delhi
Organization Name: Cybersecurity Lab
Organizational Unit: Security
Common Name: localhost
Email Address: student@example.com
```

This creates `certificate.crt`.

### 4. Inspect the Certificate

```cmd
openssl x509 -in certificate.crt -text -noout
```

This displays the certificate version, serial number, issuer, subject, validity period, public key, and signature algorithm.

### 5. Display Subject, Issuer and Validity

```cmd
openssl x509 -in certificate.crt -noout -subject -issuer -dates
```

### 6. Verify the Certificate

```cmd
openssl verify -CAfile certificate.crt certificate.crt
```

Expected output:

```text
certificate.crt: OK
```

### 7. Generate SHA-256 Fingerprint

```cmd
openssl x509 -in certificate.crt -noout -fingerprint -sha256
```

## Files Generated

```text
private.key
certificate.crt
```

- **private.key** — Private RSA key
- **certificate.crt** — Self-signed X.509 certificate

## Result

A self-signed X.509 digital certificate was successfully generated, its structure was inspected, and the certificate was verified using OpenSSL.

## Security Note

The `private.key` file contains the private key and should **not be shared**. Self-signed certificates are suitable for testing and lab environments but are not automatically trusted by normal browsers.

## Viva Questions

### 1. What is X.509?

X.509 is a standard format for digital certificates.

### 2. What is a self-signed certificate?

A certificate signed using its own private key.

### 3. What is the purpose of a private key?

It is used for cryptographic operations such as signing.

### 4. What is contained in an X.509 certificate?

Identity information, public key, validity period, issuer, and digital signature.

### 5. Why did we use SHA-256?

SHA-256 is used as a secure hashing algorithm for the certificate signature.

### 6. What is the purpose of certificate verification?

To check whether the certificate can be validated against the specified trust source.

### 7. Where are certificates used?

They are commonly used in HTTPS/TLS and other secure communications.
