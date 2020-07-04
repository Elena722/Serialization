import csv

# with open('people.csv') as fr:
#     reader = csv.reader(fr)
#     number_of_records = 0
#     no_email = 0
#     middle_name = 0
#     without_email = []
#     for i in reader:
#         number_of_records += 1
#         if i[5] == '':
#             no_email += 1
#             without_email.append(i)
#         if i[2] != '':
#             middle_name += 1
# print(number_of_records)
# print(no_email)
# print(middle_name)
#
# with open('new_file.csv', 'w') as fw:
#     writer = csv.writer(fw, lineterminator='\n')
#     writer.writerows(without_email)

# or

with open('people.csv') as fr:
    reader = csv.DictReader(fr)
    number_of_records = 0  # without header
    no_email = 0
    middle_name = 0
    without_email = []
    for i in reader:
        number_of_records += 1
        if i['email'] == '':
            no_email += 1
            without_email.append(i)
        if i['middle_name'] != '':
            middle_name += 1

print(number_of_records)
print(no_email)
print(middle_name)
# print(without_email)
# for i in without_email:
    # print(i, type(i))

with open('new_file2.csv', 'w') as fw:
    writer = csv.DictWriter(fw, fieldnames=without_email[0])
    writer.writeheader()
    writer.writerows(without_email)