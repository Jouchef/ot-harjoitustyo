from entities.user import User


class Group:
    def __init__(self, name):
        self.name = name
        self.leaders = []
        self.participants = []
        self.calendars = 10

# asked ai how to handle errors
    def add_leader(self, user):
        if isinstance(user, User):
            self.leaders.append(user)
        else:
            raise ValueError("Only User type allowed.")

    def add_participant(self, user):
        if isinstance(user, User):
            self.participants.append(user)
        else:
            raise ValueError("Only User type allowed.")

    def add_participants(self, users):
        for user in users:
            if isinstance(user, User):
                self.participants.append(user)
            else:
                raise ValueError("only user type allowed..")

    def remove_user_from_list(self, user, user_list):
        if user in user_list:
            user_list.remove(user)

    def add_calendars(self, amount):
        self.calendars += amount

    def take_calendars(self, amount):
        self.calendars -= amount

# string representation generated partly with ai. The ".join" part was new to me.
    def __str__(self):
        leaders_names = ", ".join([leader.username for leader in self.leaders])
        participants_names = ", ".join(
            [participant.username for participant in self.participants])
        return (f"Group(name='{self.name}', "
                f"leaders=[{leaders_names}], "
                f"participants=[{participants_names}])"
                f"calendars={self.calendars}")
