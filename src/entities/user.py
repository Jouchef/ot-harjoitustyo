class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return (
            self.username == other.username
        )

    def __str__(self):
        return f"User(username='{self._username}')"
