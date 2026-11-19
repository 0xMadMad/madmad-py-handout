import re

password = input("enter your password: ")

score = 0
issues = []


if len(password) >= 8:
    score += 20
else:
    issues.append("password is too short, at least 8 characters needed")

if len(password) >= 12:
    score += 10


if re.search(r"[A-Z]", password):
    score += 15
else:
    issues.append("at least one uppercase letter..")

if re.search(r"[a-z]", password):
    score += 15
else:
    issues.append("at least one lowercase letter..")

if re.search(r"[0-9]", password):
    score += 15
else:
    issues.append("at least one number..")

if re.search(r"[^a-zA-Z0-9]", password):
    score += 15
else:
    issues.append("at least one special character..")


if len(set(password)) < len(password):
    score -= 10
    issues.append("password has repeated characters..")


common_passwords = [
    "password", "12345678", "qwerty123",
    "admin123", "123456789", "password123"
]
if password.lower() in common_passwords:
    score = 0
    issues.append("do you like being hacked?..")

if "1234" in password or "abcd" in password.lower() or "qwerty" in password.lower():
    score -= 15
    issues.append("avoid predictable sequences..")


score = max(0, min(score, 100))
print("\n--- PASSWORD REPORT ---")
print("score:", score, "/ 100")

if score >= 80:
    print("strength: STRONG")
elif score >= 50:
    print("strength: MEDium")
else:
    print("strength: weak")

if issues:
    print("\nsuggestions:")
    for issue in issues:
        print("-", issue)
else:
    print("your password looks good!")

#MadMad_75