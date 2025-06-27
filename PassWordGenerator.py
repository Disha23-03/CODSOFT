import random
import string

print("=== Password Generator ===")

# Step 1: Ask for password length
try:
    length = int(input("Enter desired password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        # Step 2: Build character pool
        letters = string.ascii_letters  # a-z + A-Z
        digits = string.digits  # 0-9
        symbols = string.punctuation  # Special characters

        all_chars = letters + digits + symbols

        # Step 3: Generate password
        password = "".join(random.choices(all_chars, k=length))

        # Step 4: Output
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
