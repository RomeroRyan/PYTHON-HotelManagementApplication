import json
import string
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
            guests[index]["fname"] = fields[0].upper()
            guests[index]["lname"] = fields[1].upper()
            guests[index]["phone"] = fields[2].upper()
            guests[index]["address"] = fields[3].upper()
            guests[index]["email"] = fields[4].upper()
            guests[index]["id"] = fields[5].upper()
            guests[index]["vehicle"] = fields[6].upper()
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


# WORKS: Guest First Name, Guest Last Name,  Phone Number, Street Address, Check In Date, Checkout Date.
# DOESNT WORK: Room Number bc it thinks rm_number = chk_in


def search_guests(flg, key):
    results = []
    guests = get_guests_search()
    key = key.upper()
    print("key: %s" % key)
    if flg == "Exact":
        for guest in guests:
            if guest.get_fname() == key or guest.get_lname() == key or guest.get_rm_number() == key or guest.get_phone() == key or guest.get_address() == key or guest.get_chk_in() == key or guest.get_chk_out() == key:
                results.append(guest)
    elif flg == "Contains":
        for guest in guests:
            if key in guest.get_fname() or key in guest.get_lname() or key in guest.get_rm_number() or key in guest.get_phone() or key in guest.get_address() or key in guest.get_chk_in() or key in guest.get_chk_out():
                results.append(guest)
    return results
