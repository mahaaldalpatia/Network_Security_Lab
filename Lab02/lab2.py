import hashlib

def calculate_hash(filename):
    with open(filename, "rb") as file:
        file_data = file.read()
        return hashlib.sha256(file_data).hexdigest()


with open("sample.txt", "w") as file:
    file.write("This is the original content of the file.")

print("File created successfully.")

hash1 = calculate_hash("sample.txt")
print("Original Hash:", hash1)

with open("sample.txt", "a") as file:
    file.write("\nThis text was added later.")

print("File modified successfully.")
hash2 = calculate_hash("sample.txt")
print("Modified Hash:", hash2)

if hash1 == hash2:
    print("Hashes match. File has not been modified.")
else:
    print("Hashes do not match. File integrity has been compromised.")

