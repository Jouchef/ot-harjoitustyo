from entities.group import Group

class GroupService:
    def __init__(self):
        self._groups = []

    def create_group(self, name):
        new_group = Group(name)
        self._groups.append(new_group)
        return new_group

    def delete_group(self, group_name):
        for group in self._groups:
            if group.name == group_name:
                self._groups.remove(group)
                return True
        return False

    def list_groups(self):
        return self._groups
