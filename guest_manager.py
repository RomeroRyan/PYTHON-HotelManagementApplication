import json
import os.path
from guest import Guest
# 11
# pass an index to update and an array of the field values


def update_guest(id, fields):
    f = open(os.path.dirname(__file__) + '/data/guest.json', 'r+')
    guests = json.load(f)
    f.seek(0)
    f.truncate()
    for index, guest in enumerate(guests):
        if guest["id"] == id:
            guests[index]["fname"] = fields[0]
            guests[index]["lname"] = fields[1]
            guests[index]["phone"] = fields[2]
            guests[index]["address"] = fields[3]
            guests[index]["email"] = fields[4]
            guests[index]["id"] = fields[5]
            guests[index]["vehicle"] = fields[6]
            guests[index]["img_path"] = fields[7]
            json.dump(guests, f, indent=4)
            f.close()


def get_raw_guests():
    f = open(os.path.dirname(__file__) + '/data/guest.json', 'r+')
    guests = json.load(f)
    f.close()
    return guests


def get_guests():
    guest_list = []
    guests = get_raw_guests()

    for guest in guests:
        guest_list.append(
            Guest(guest["fname"],
                  guest["lname"],
                  guest["phone"],
                  guest["address"],
                  guest["email"],
                  guest["id"],
                  guest["vehicle"],
                  guest["img_path"]))
    return guest_list


def find_guest(guest_id):
    guests = get_guests()
    for guest in guests:
        if guest.get_id() == guest_id:
            return guest
