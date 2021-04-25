class HotelRoom:
    """ Hotel Room Class """

    def __init__(self, room_num="000", room_type="King", room_status="unavailable"):
        self.room_num = room_num
        self.room_type = room_type
        self.room_status = room_status

    def get_room_num(self):
        return self.room_num

    def set_room_num(self, room_num):
        self.room_num = room_num

    def get_room_type(self):
        return self.room_type

    def set_room_type(self, room_type):
        self.room_type = room_type

    def get_room_status(self):
        return self.room_status

    def set_room_status(self, room_status):
        self.room_status = room_status

    def get_room_combo_name(self):
        room_initials = ""
        for word in self.room_type.split(" "):
            room_initials += word[0]
        return "{0} ({1})".format(self.room_num, room_initials)