import random
import string
import pyperclip

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Python Password Generator!")
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("Password should be at least 4 characters long.")
            return

        password = generate_password(length)
        print(f"\nYour generated password is: {password}")

        # Copy password to clipboard
        pyperclip.copy(password)
        print("📋 Password copied to clipboard!")

    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()
