import json
import os.path

from hotel_room import HotelRoom

def update_room(index, status):
    f = open(os.path.dirname(__file__) + '/data/rooms.json', 'r+')
    rooms = json.load(f)
    f.seek(0)
    f.truncate()
    rooms[index]["room_status"] = status
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
        room_list.append(HotelRoom(room["room_num"], room["room_type"], room["room_status"]))
    return room_list