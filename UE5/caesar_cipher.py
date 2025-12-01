letters = {chr(65 + i): i + 1 for i in range(26)}
rev_letters = {v: k for k, v in letters.items()}

def encrypt(message):
    message = message.upper()
    result = ""
    for ch in message:
        if ch in letters:
            new_val = (letters[ch] % 26) + 1
            result += rev_letters[new_val]
        else:
            result += ch
    return result

def decrypt(message):
    message = message.upper()
    result = ""
    for ch in message:
        if ch in letters:
            new_val = (letters[ch] - 2) % 26 + 1
            result += rev_letters[new_val]
        else:
            result += ch
    return result

print(encrypt("HELLO"))
print(decrypt("IFMMP"))