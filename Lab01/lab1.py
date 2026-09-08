def caesar_encrypt(text: str, shift: int) -> str:
    result = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_pos = (ord(char) - base + shift) % 26
            result.append(chr(new_pos + base))
        else:
            result.append(char)

    return "".join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    result = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_pos = (ord(char) - base - shift) % 26
            result.append(chr(new_pos + base))
        else:
            result.append(char)

    return "".join(result)




def vigenere_encrypt(text: str, key: str) -> str:
    result = []
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_char = key[key_index % len(key)]
            shift = ord(key_char.upper()) - ord('A')
            new_pos = (ord(char) - base + shift) % 26
            result.append(chr(new_pos + base))
            key_index += 1

        else:
            result.append(char)

    return "".join(result)

def vigenere_decrypt(text: str, key: str) -> str:
    result = []
    key_index = 0

    for char in text:
        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')
            key_char = key[key_index % len(key)]
            shift = ord(key_char.upper()) - ord('A')
            new_pos = (ord(char) - base - shift) % 26
            result.append(chr(new_pos + base))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)


# Caesar test
message1 = "Hello Network Security"
caesar_ct = caesar_encrypt(message1, 3)

print("\n--- Caesar Cipher ---")
print("Original:", message1)
print("Encrypted:", caesar_ct)
print("Decrypted:", caesar_decrypt(caesar_ct, 3))


# Vigenere test
message2 = "Network Security"
key = "key"

vigenere_ct = vigenere_encrypt(message2, key)

print("\n--- Vigenere Cipher ---")
print("Original:", message2)
print("Encrypted:", vigenere_ct)
print("Decrypted:", vigenere_decrypt(vigenere_ct, key))