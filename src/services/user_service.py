from entities.user import User
from services.group_service import GroupService

class UserService:
    def __init__(self, group_service: GroupService):
        self._users = []
        self._group_service = group_service

    def add_user(self, username, role, group_name):
        user = User(username, role, group_name)
        self._users.append(user)

        if group_name:
            group = next((g for g in self._group_service.list_groups() if g.name == group_name), None)
            if group:
                group.add_participant(user)

        return user

    def remove_user(self, username):
        for user in self._users:
            if user.username == username:
                self._users.remove(user)
                return True
        return False

    def list_users(self):
        return self._users
    
    def list_users_by_group(self, group_name):
        return [user for user in self._users if user.group == group_name]