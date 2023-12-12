import csv
import re

merged_data = {}

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.DictReader(f, delimiter=",")
    for i in rows:
        phone = re.sub(r".?(\d{1}).*(\d{3}).*(\d{3}).?(\d{2}).?(\d{2})((\s)\(?(\w{3}.)\s?(\d{4}).?)?", r"+\1(\2)\3-\4-\5\7\8\9", i['phone'])
        i['phone'] = phone

        p = re.findall(r"[А-Я][а-я]+", i['lastname']) + re.findall(r"[А-Я][а-я]+", i['firstname'])
        i['lastname'] = p[0]
        i['firstname'] = p[1]
        i['surname'] = p[2] if len(p) == 3  else ''
        key = (i['lastname'], i['firstname'])
        if key in merged_data:
            merged_data[key]['surname'] = i['surname'] if i['surname'] else merged_data[key]['surname']
            merged_data[key]['organization'] = i['organization'] if i['organization'] else merged_data[key]['organization']
            merged_data[key]['position'] = i['position'] if i['position'] else merged_data[key]['position']
            merged_data[key]['phone'] = i['phone'] if i['phone'] else merged_data[key]['phone']
            merged_data[key]['email'] = i['email'] if i['email'] else merged_data[key]['email']
        else:
            merged_data[key] = i

title = []

for i in merged_data.values():
    for k in i.keys():
        title.append(k)
    break

with open('new_file.csv', 'w', encoding='utf-8') as file:
    file_write = csv.DictWriter(file, delimiter=',', lineterminator='\r', fieldnames=title)
    file_write.writeheader()
    for merged in merged_data.values():
        file_write.writerow(merged) 