class CalendarService:
    def __init__(self):
        pass

    def ensure_positive_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

    def ensure_sufficient_calendars(self, source, amount):
        if amount > source.calendars:
            raise ValueError("The source does not have enough calendars.")

    def transfer_calendars(self, fromWhere, toTarget, amount):

        self.ensure_positive_amount(amount)
        self.ensure_sufficient_calendars(fromWhere, amount)
        
        fromWhere.take_calendars(amount)
        toTarget.add_calendars(amount)

    def add_calendars_to_group(self, group, amount):
        self.ensure_positive_amount(amount)
        group.add_calendars(amount)

    def remove_calendars_from_group(self, group, amount):
        self.ensure_positive_amount(amount)
        self.ensure_sufficient_calendars(group, amount)
        
        group.take_calendars(amount)
