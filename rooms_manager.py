import json
import os.path
import datetime

from hotel_room import HotelRoom

def update_room(index, status, check_in=None, check_out=None):
    f = open(os.path.dirname(__file__) + '/data/rooms.json', 'r+')
    rooms = json.load(f)
    f.seek(0)
    f.truncate()
    if check_in is not None and check_out is not None:
        if check_in == check_out:
            print("Please only reserve rooms for 6 days or less and cannot check-in and check_out on the same day!")
            return 
        for day in range(check_in, (check_in + check_out) % 7):
            rooms[index]["days"][str(day%7)] = status
    else:
        day = datetime.datetime.today().weekday()
        rooms[index]["days"][str(day%7)] = status

        
    json.dump(rooms, f, indent=4)
    f.close()

def update_room_by_number(room_number, status, check_in, check_out):
    f = open(os.path.dirname(__file__) + '/data/rooms.json', 'r+')
    rooms = json.load(f)
    f.seek(0)
    f.truncate()

    for room in rooms:
        if room["room_num"] == room_number:
            for day in range(check_in, check_out):
                room["days"][str(day%7)] = status
    json.dump(rooms, f, indent=4)
    f.close()

def get_raw_rooms():
    f = open(os.path.dirname(__file__) + '/data/rooms.json', 'r+')
    rooms = json.load(f)
    f.close()
    return rooms

def get_hotel_rooms():
    room_list = []
    rooms = get_raw_rooms()

    for room in rooms:
        room_list.append(
            HotelRoom(room["room_num"], room["room_type"], room_week=room["days"]))
    return room_list

def get_hotel_room_by_num(num):
    rooms = get_raw_rooms()

    for room in rooms:
        if room["room_num"] == num:
            return HotelRoom(room["room_num"], room["room_type"], room_week=room["days"])
    return None