import bcrypt


class Hash():
    """
    The password hashing function to hash and verify passwords
    """

    @staticmethod
    def hash_password(password):
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(pwd_bytes, salt)
        return hashed_password

    @staticmethod
    def verify_password(plain_password, hashed_password):
        password_byte_enc = plain_password.encode('utf-8')
        # Decode the hashed password
        hashed_password_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password_byte_enc, hashed_password_bytes)
