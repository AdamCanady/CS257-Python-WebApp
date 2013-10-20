# SQL file creator
# CS257, Fall 2013, Jeff Ondich
# Erin Wilson, Jiatao Cheng, Adam Canady

import csv

document_names = ['rooms.csv', 'buildings.csv', 'number_map.csv']

#### Create rooms.sql ####
rooms_sql = open('rooms.sql','w')
rooms_sql.write("DROP TABLE IF EXISTS rooms;\n")
rooms_sql.write("""CREATE TABLE rooms (
  building_id int,
  avg_draw_number int,
  room int,
  occupancy int,
  sub_free boolean,
  quiet boolean
);\n\n""")

headers = True
for line in csv.reader(open('rooms.csv','rU')):
    if headers == True: headers = False; continue # Skip headers

    line = [int(i) for i in line]

    building_id = line[0]
    avg_draw_number = line[1]
    room = line[2]
    occupancy = line[3]
    sub_free = line[4]
    if sub_free == 1:
        sub_free = "yes"
    else:
        sub_free = "no"
    quiet = line[5]
    if quiet == 1:
        quiet = "yes"
    else:
        quiet = "no"

    insert_statement = "INSERT INTO rooms (building_id, avg_draw_number, room, occupancy, sub_free, quiet) " + \
                        "VALUES (%d, %d, %d, %d, '%s', '%s');\n" \
                        % (building_id, avg_draw_number, room, occupancy, sub_free, quiet)

    rooms_sql.write(insert_statement)

rooms_sql.close()

#### Create buildings.sql ####
buildings_sql = open('buildings.sql','w')
buildings_sql.write("DROP TABLE IF EXISTS buildings;\n")
buildings_sql.write("""CREATE TABLE buildings (
  id int,
  building text,
  geo_lat numeric,
  geo_long numeric
);\n\n""")

headers = True
for line in csv.reader(open('buildings.csv','rU')):
    if headers == True: headers = False; continue # Skip headers

    id = int(line[0])
    building = line[1]
    geo_lat = float(line[2])
    geo_long = float(line[3])

    insert_statement = "INSERT INTO buildings (id, building, geo_lat, geo_long) " + \
                        "VALUES (%d, '%s', %f, %f);\n" \
                        % (id, building, geo_lat, geo_long)

    buildings_sql.write(insert_statement)

buildings_sql.close()

#### Create number_map.sql ####
number_map_sql = open('number_map.sql','w')
number_map_sql.write("DROP TABLE IF EXISTS number_map;\n")
number_map_sql.write("""CREATE TABLE number_map (
  db_num int,
  roomdraw_num int
);\n\n""")

headers = True
for line in csv.reader(open('number_map.csv','rU')):
    if headers == True: headers = False; continue # Skip headers

    db_num = int(line[0])
    roomdraw_num = int(line[1])

    insert_statement = "INSERT INTO number_map (db_num, roomdraw_num) "+ \
                        "VALUES (%d, %d);\n" \
                        % (db_num, roomdraw_num)

    number_map_sql.write(insert_statement)

number_map_sql.close()
