import json
import os.path
import datetime

from hotel_room import HotelRoom


def update_room(index, status):
    f = open(os.path.dirname(__file__) + '/data/rooms.json', 'r+')
    rooms = json.load(f)
    day_index = datetime.datetime.today().weekday()
    f.seek(0)
    f.truncate()
    rooms[index]["days"][str(day_index)] = status
    json.dump(rooms, f, indent=4)
    f.close()

def update_room_by_number(room_number, status):
    f = open(os.path.dirname(__file__) + '/data/rooms.json', 'r+')
    rooms = json.load(f)
    f.seek(0)
    f.truncate()

    for room in rooms:
        if room["room_num"] == room_number:
            room["room_status"] = status

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
