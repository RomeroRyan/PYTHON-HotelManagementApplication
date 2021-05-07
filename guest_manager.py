import json
import string
import os.path
from guest import Guest

def update_guest(id, fields):
    f = open(os.path.dirname(__file__) + '/data/guest.json', 'r+')
    guests = json.load(f)
    f.seek(0)
    f.truncate()
    for index, guest in enumerate(guests):
        if guest["id"] == id:
            guests[index]["fname"] = fields[0].upper()
            guests[index]["lname"] = fields[1].upper()
            guests[index]["phone"] = fields[2].upper()
            guests[index]["address"] = fields[3].upper()
            guests[index]["email"] = fields[4].upper()
            guests[index]["id"] = fields[5].upper()
            guests[index]["vehicle"] = fields[6].upper()
            guests[index]["img_path"] = fields[7]
            break
    json.dump(guests, f, indent=4)
    f.close()

def update_guest_by_room(room):
    f = open(os.path.dirname(__file__) + '/data/guest.json', 'r+')
    guests = json.load(f)
    f.seek(0)
    f.truncate()
    for index, guest in enumerate(guests):
        if guest["rm_number"] == room:
            guests.pop(index)
            break
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
            Guest(fname=guest["fname"],
                  lname=guest["lname"],
                  phone=guest["phone"],
                  rm_number=guest["rm_number"],
                  address=guest["address"],
                  email=guest["email"],
                  id=guest["id"],
                  vehicle=guest["vehicle"],
                  img_path=guest["img_path"]))
    return guest_list

def add_guest(guest, room, check_in, check_out):
    f = open(os.path.dirname(__file__) + '/data/guest.json', 'r+')
    guests = json.load(f)
    f.seek(0)
    f.truncate()

    guests.append({
        "fname": guest["fname"].get(),
        "lname": guest["lname"].get(),
        "phone": guest["phone"].get(),
        "rm_number": room.room_num,
        "address": guest["address"].get(),
        "email": guest["email"].get(),
        "chk_in": check_in,
        "chk_out": check_out,
        "id": guest["id"].get(),
        "vehicle": guest["vehicle"].get(),
        "img_path": guest["img_path"] or ".res/placeholder.png"
    })
    json.dump(guests, f, indent=4)
    f.close()

def get_guests_search():
    guests = []
    raw_guests = get_raw_guests()
    for guest in raw_guests:
        guests.append(
            Guest(guest["fname"],
                  guest["lname"],
                  guest["phone"],
                  guest["address"],
                  guest["email"],
                  guest["id"],
                  guest["vehicle"],
                  guest["img_path"],
                  guest["rm_number"],
                  guest["chk_in"],
                  guest["chk_out"]))
    return guests


def find_guest(guest_id):
    guests = get_guests()
    for guest in guests:
        if guest.get_id() == guest_id:
            return guest


def search_guests(flg, key):
    results = []
    guests = get_guests_search()
    key = key.upper()
    if key == "":
        return results
    elif flg == "Exact":
        for guest in guests:
            if guest.get_fname() == key or guest.get_lname() == key or guest.get_rm_number() == key or guest.get_phone() == key or guest.get_address() == key or guest.get_chk_in() == key or guest.get_chk_out() == key:
                results.append(guest)
    elif flg == "Contains":
        for guest in guests:
            if key in guest.get_fname() or key in guest.get_lname() or key in guest.get_rm_number() or key in guest.get_phone() or key in guest.get_address() or key in guest.get_chk_in() or key in guest.get_chk_out():
                results.append(guest)
    return results
