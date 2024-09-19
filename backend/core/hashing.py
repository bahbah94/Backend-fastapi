from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)


hashed_password = Hasher.get_password_hash("mysecretpassword")
print(hashed_password)
print(
    Hasher.verify_password(
        "mysecretpassword",
        "$2b$12$mNJeQ0PrNmgbuUqRR0DHGugcjmeHNmsT2R4XNBN8Ibx13UVzXUr2.",
    )
)
