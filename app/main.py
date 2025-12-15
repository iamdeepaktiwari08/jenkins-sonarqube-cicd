import os


def secure_login(input_password: str) -> bool:
    """
    Secure login check.
    Password is read from environment variable (no hardcoding).
    """

    if not input_password:
        raise ValueError("Password is required")

    stored_password = os.getenv("APP_PASSWORD")

    if not stored_password:
        raise EnvironmentError("APP_PASSWORD is not set")

    return input_password == stored_password


if __name__ == "__main__":
    # example usage
    user_password = "test123"  # simulate user input
    result = secure_login(user_password)
    print("Login success:", result)