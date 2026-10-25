
import secrets
import string


def generate_password(length):
    if length < 4:
        return None

    characters = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + string.punctuation
    )

    password_chars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    password_chars.extend(
        secrets.choice(characters) for _ in range(length - 4)
    )

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter password length (minimum 4): "))

        if length < 4:
            print("Please enter a length of at least 4.")
            return

        password = generate_password(length)
        print("\nGenerated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
