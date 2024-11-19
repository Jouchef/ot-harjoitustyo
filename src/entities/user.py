class User:
    def __init__(self, username, role, group):
        self._username= username
        self._role =role
        self._group= group
        self._calendars = 0

    @property
    def username(self):
        return self._username

    @property
    def role(self):
        return self._role

    @property
    def group(self):
        return self._group
    
    @property
    def calendars(self):
        return self._calendars

    def set_username(self, new_username):
        self._username = new_username

    def set_role(self, new_role):
        self._role = new_role

    def set_group(self, new_group):
        self._group = new_group

    def add_calendars(self, amount):
        self._calendars += amount

    def take_calendars(self, amount):
        self._calendars -= amount

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return (
            self.username == other.username
            and self.role == other.role
            and self.group == other.group
            and self.calendars == other.calendars
        )

    def __str__(self):
        return f"User(username='{self._username}', rolee='{self._role}', group='{self._group}')"