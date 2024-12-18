
class Group:
    def __init__(self, name):
        self.name = name

# string representation generated partly with ai. The ".join" part was new to me.
    def __str__(self):
        return f"Group(name='{self.name}')"
