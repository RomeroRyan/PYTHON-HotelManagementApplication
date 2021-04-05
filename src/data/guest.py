class Guest:
    """ Guest Class """
    def __init__(
                self, first_name="John", last_name="Smith", phone="555-555-5555",
                address="5555 Street Ave, Ca, 55555", email="myEmail@gmail.com"
                ):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.email = email

    def get_first_name(self):
        return self.first_name
    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name
    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone

    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address

    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email