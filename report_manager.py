import json
import string
import os.path
from guest import Guest

def add_section(guest, section):
    f = open(os.path.dirname(__file__) + '/data/report.json', 'r+')
    sections = json.load(f)[section]
    f.seek(0)
    f.truncate()

    sections.append({
        "fname": guest["fname"],
        "lname": guest["lname"],
        "phone": guest["phone"],
        "rm_number": guest["room_num"],
        "address": guest["address"],
        "email": guest["email"],
        "chk_in": guest["check_in"],
        "chk_out": guest["check_out"],
        "id": guest["id"],
        "vehicle": guest["vehicle"],
        "img_path": guest["img_path"] or ".res/placeholder.png",
        "paid_total": guest["paid_total"]
    })
    json.dump(sections, f, indent=4)
    f.close()

def get_report_section(section):
    sections_list = []
    sections = get_raw_report()

    for guest in sections[section]:
        sections_list.append(
            Guest(fname=guest["fname"],
                  lname=guest["lname"],
                  phone=guest["phone"],
                  rm_number=guest["rm_number"],
                  address=guest["address"],
                  email=guest["email"],
                  chk_in=guest["chk_in"],
                  chk_out=guest["chk_out"],
                  id=guest["id"],
                  vehicle=guest["vehicle"],
                  img_path=guest["img_path"],
                  paid_total=guest["paid_total"]))
    return sections_list

def get_raw_report():
    f = open(os.path.dirname(__file__) + '/data/report.json', 'r+')
    reports = json.load(f)
    f.close()
    return reports