import secrets
import string

symbols = "!@#$%^&*_-"
chars = string.ascii_letters + string.digits + symbols

length = int(input("enter password length (at least 8 characters): "))

if length<8:
    print("password must be at least 8 characters")
else:
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(symbols)
    ]

    password += [secrets.choice(chars) for _ in range(length - 4)]

    secrets.SystemRandom().shuffle(password)

    password = ''.join(password)

    print("generated password:", password)
#MadMad_26