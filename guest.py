class Guest:
    """ Guest Class """

    def __init__(
            self, fname="John", lname="Smith",
            phone="555-555-5555",
            address="5555 Street Ave",
            email="myEmail@gmail.com",
            id="A100000",
            vehicle="L102AO2",
            img_path="./res/placeholder.png",
            rm_number="101",
            chk_in="02/28/2021",
            chk_out="03/01/2021"
    ):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.address = address
        self.email = email
        self.id = id
        self.vehicle = vehicle
        self.img_path = img_path
        self.rm_number = rm_number
        self.chk_in = chk_in
        self.chk_out = chk_out

    def get_fname(self):
        return self.fname

    def set_fname(self, fname):
        self.fname = fname

    def get_lname(self):
        return self.lname

    def set_lname(self, lname):
        self.lname = lname

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

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_vehicle(self):
        return self.vehicle

    def set_vehicle(self, vehicle):
        self.vehicle = vehicle

    def get_img_path(self):
        return self.img_path

    def set_img_path(self, img_path):
        self.img_path = img_path

    def get_rm_number(self):
        return self.rm_number

    def set_rm_number(self, rm_number):
        self.rm_number = rm_number

    def get_chk_in(self):
        return self.chk_in

    def set_chk_in(self, chk_in):
        self.chk_in = chk_in

    def get_chk_out(self):
        return self.chk_out

    def set_chk_out(self, chk_out):
        self.chk_out = chk_out
