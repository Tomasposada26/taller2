class JsonPlaceholderUserRepository:
    def get_user_email(self, user_id):
        raise ConnectionError("User service unavailable")

class FakeUserRepository:
    def get_user_email(self, user_id):
        # TODO: retornar un email ficticio
        return f"user{user_id}@fake.local"