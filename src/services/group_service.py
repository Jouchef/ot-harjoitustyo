from reposetory.group_reposetory import group_reposetory

class DuplicateGroupError(Exception):
    pass

class InvalidGroupError(Exception):
    pass

class GroupService:
    def __init__(self):
        self._group_reposetory = group_reposetory

    def get_group(self, group_name):
        return self._group_reposetory.get_group(group_name)


    def create_group(self, group_name):
        if self._group_reposetory.get_group(group_name):
            raise DuplicateGroupError(f"Ryhmä {group_name} on jo olemassa!")
        else:
            return self._group_reposetory.create_group(group_name)

    def delete_group(self, group_name):
        if not self._group_reposetory.get_group(group_name):
            raise InvalidGroupError(f"Poistettavaa ryhmää {group_name} ei ole olemassa!")
        else:
            return self._group_reposetory.delete_group(group_name)
    
    def list_all_groups(self):
        return self._group_reposetory.list_all_groups()

group_service = GroupService()
