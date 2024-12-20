from reposetory.user_reposetory import user_reposetory


class InvalidCredentialsError(Exception):
    pass

class DuplicateUserError(Exception):
    pass

class UserService:
    def __init__(self,):
        self._user = None
        self._user_reposetory = user_reposetory

    def register(self, username, password):
        if self._user_reposetory.get_user(username):
            raise DuplicateUserError(f"Käyttäjätunnus {username} on jo käytössä!")
        else:
            self._user_reposetory.add_user(username, password)
            return True


    def login(self, username, password):
        user_logging_in = self._user_reposetory.get_user(username)
        if user_logging_in and user_logging_in.password == password:
            self._user = user_logging_in
            return self._user
        else:
            raise InvalidCredentialsError("Väärä käyttäjätunnus tai salasana!")

        



user_service = UserService()
