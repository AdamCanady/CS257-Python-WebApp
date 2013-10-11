
create_table = '''DROP TABLE IF EXISTS roomdraw;
CREATE TABLE roomdraw (
  year int,
  draw_number int,
  building text,
  room_number text,
  occupancy text,
);
'''
print create_table
print

import csv
doc = csv.reader(open('roomdraw.csv','rU'))
for row in doc:
	insert_statement = "INSERT INTO roomdraw (year, draw_number, building, room_number, occupancy) VALUES "
	values = "("+str(row[0])+", "+str(row[1])+", '"+str(row[2])+"', '"+str(row[3])+"', '"+str(row[4])+"')"

	print insert_statement + values