import hashlib
import os
from datetime import datetime


def calculate_hash(filename):
    with open(filename, "rb") as file:
        file_data = file.read()
        return hashlib.sha256(file_data).hexdigest()


def file_information(filename):
    file_size = os.path.getsize(filename)
    modified_time = os.path.getmtime(filename)

    print("File Size:", file_size, "bytes")
    print("Last Modified:",
          datetime.fromtimestamp(modified_time).strftime("%Y-%m-%d %H:%M:%S"))


# Step 1: Create the file
with open("sample.txt", "w") as file:
    file.write("This is the original content of the file.")

print("File created successfully.")

print("\nOriginal File Information:")
file_information("sample.txt")

# Step 2: Calculate original hash
hash1 = calculate_hash("sample.txt")
print("Original Hash:", hash1)


# Step 3: Modify the file
with open("sample.txt", "a") as file:
    file.write("\nThis text was added later.")

print("\nFile modified successfully.")

print("\nModified File Information:")
file_information("sample.txt")

# Step 4: Calculate modified hash
hash2 = calculate_hash("sample.txt")
print("Modified Hash:", hash2)


# Step 5: Compare hashes
print("\nIntegrity Verification:")

if hash1 == hash2:
    print("Hashes match.")
    print("File integrity is maintained.")
else:
    print("Hashes do not match.")
    print("Warning: File has been modified!")
