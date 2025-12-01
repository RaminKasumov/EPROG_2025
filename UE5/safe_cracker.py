from hashlib import sha256

def tresor(code):
    secret_code = ("b2b2f104d32c638903e151a9b20d6e27"
                   + "b41d8c0c84cf8458738f83ca2f1dd744")
    m = sha256()
    m.update(code.encode())
    if m.hexdigest() == secret_code:
        print("Safe opened! Code is:", code)
        return True
    return False

def crack_safe():
    for i in range(10000):
        code = f"{i:04d}"
        if tresor(code):
            break

crack_safe()