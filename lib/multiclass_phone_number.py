class PhoneNumber:
    def __init__(self, phone_number=None):
        self.phone_number = phone_number

    def has_a_phone_number_check(self):
        if self.phone_number != None:
            return True