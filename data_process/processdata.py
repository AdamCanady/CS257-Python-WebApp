# Average Draw Number Finder
# CS 257, Fall 2013, Jeff Ondich
# Erin Wilson, Jiatao Cheng, Adam Canady

# This program averages all of the past room draw numbers used to draw rooms

import csv
import math

#### Build list of available rooms ####

room_list_doc = open('roomlist.txt','r')

available_rooms = []
for line in room_list_doc:
    line = line.split('\t')
    building = line[0]
    room = line[1].strip()

    available_rooms += ((building, room),)

#### Build number map to computer average properly ####

number_map_doc = open('number_map.txt','r')

number_map = {}
for line in number_map_doc:
    line = line.split('\t')
    db_num = line[0]
    roomdraw_num = line[1].strip()

    number_map[roomdraw_num] = db_num


#### Add draw numbers to rooms ####

avg_dict = {} # avg_dict[(building,room)] = [1001,1002,1001]

document_list = ['2012.csv','2011.csv','2010.csv','2009.csv','2008.csv']

for building, room in available_rooms:
    room = room[:3] # Removes letters from room numbers ex. 303A -> 303
    avg_dict[(building,room)] = []

    for document_name in document_list:
        doc_open = open(document_name, 'rU')
        document = csv.reader(doc_open)

        for row in document:
            document_building = row[1]
            document_room = row[2][:3] # Removes letters from room numbers ex. 303A -> 303

            if document_building == building and document_room == room:
                db_num = number_map[row[0]]
                avg_dict[(building,room)].append(db_num)

        doc_open.close()


#### Computer Average ####

for combo in avg_dict.keys():
    avg = float(0)
    length = len(avg_dict[combo])
    if length == 0: continue 
    for number in avg_dict[combo]:
        number = int(number)
        avg += number
    avg_dict[combo] = int(math.ceil(avg/length))

#### Print the list for our consumption ####

for combo in avg_dict.keys():
    print combo[0]+"\t"+combo[1]+"\t"+str(avg_dict[combo]) 