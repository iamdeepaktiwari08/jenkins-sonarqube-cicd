def secure_login(password):
    if not password:
        raise ValueError("Password required")
    return True