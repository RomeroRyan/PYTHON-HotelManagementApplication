import datetime

class HotelRoom:
    """ Hotel Room Class """

    def __init__(self, room_num="000", room_type="King", room_week=None):
        self.room_num = room_num
        self.room_type = room_type
        self.room_week = room_week or {0: "Unavailable", 1: "Unavailable", 2: "Unavailable", 3: "Unavailable", 4: "Unavailable", 5: "Unavailable", 6: "Unavailable"}

    def get_room_num(self):
        return self.room_num

    def set_room_num(self, room_num):
        self.room_num = room_num

    def get_room_type(self):
        return self.room_type

    def set_room_type(self, room_type):
        self.room_type = room_type

    def get_room_status(self):
        return self.room_week[str(datetime.datetime.today().weekday())]

    def set_room_status(self, status):
        self.room_week[str(datetime.datetime.today().weekday())] = status

    def set_current_room_status(self, day, status):
        self.room_week[day] = status

    def get_current_room_status(self):
        return self.room_week.get(str(datetime.datetime.today().weekday()))


    def get_room_combo_name(self):
        room_initials = ""
        for word in self.room_type.split(" "):
            room_initials += word[0]
        return "{0} ({1})".format(self.room_num, room_initials)

    def get_room_color(self, day):
        if day:
            day = str(day)
            if self.room_week[day] == "Occupied":
                return "#FF8F51"
            elif self.room_week[day] == "Dirty":
                return "#F8FC3F"
            elif self.room_week[day] == "Maintenance":
                return "#FD5E5E"
            elif self.room_week[day] == "Available":
                return "#D9D9D9"
