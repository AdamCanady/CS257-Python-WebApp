'''datasource.py

CS 257 Python Web App, Fall 2013, Jeff Ondich
Jiatao Cheng, Erin Wilson, and Adam Canady

This module defines how to connect to our datasource and various associated
functionalities like getting metrics from various dimensions.

Some of the following code is from Jeff Ondich's psycopg2-demo.py
'''

import psycopg2

class DataSource:
    def __init__(self):

        # Start with the database login info
        self.database = 'canadya'
        self.user = 'canadya'
        self.password = 'star925propane'

        self.connect()

    def connect(self):
        # Login to the database
        try:
            self.connection = psycopg2.connect(database=self.database, user=self.user, password=self.password)
            self.cursor = self.connection.cursor()
        except Exception, e:
            raise e

    def close(self):
        self.connection.close()

    def get_rooms_by_preference(self, user_input_building = "", user_input_occupancy = 0, user_input_environment = ""):
        query = """SELECT *
                   FROM rooms
                   LEFT JOIN building ON rooms.building_id = buildings.id \n"""

        if user_input_occupancy > 0:
            if "WHERE" in query:
                query += " AND "
            else:
                query += " WHERE "
            query += "occupancy = %d" % user_input_occupancy

        if user_input_environment == "sub_free":
            if "WHERE" in query:
                query += " AND "
            else:
                query += " WHERE "
            query += "sub_free = 't'"

        if user_input_environment == "quiet":
            if "WHERE" in query:
                query += " AND "
            else:
                query += " WHERE "
            query += "quiet = 't'"

        if user_input_building:
            if "WHERE" in query:
                query += " AND "
            else:
                query += " WHERE "
            query += "building = %s" % user_input_building

        self.cursor.execute(query)

        return self.cursor.fetchall()

    def get_rooms_in_range(self, upper, lower):
        ''' Returns a list of rooms in the format:
                [building, room, occupancy, sub_free, quiet] '''
        query = """SELECT building, room, occupancy, sub_free, quiet
                   FROM rooms
                   LEFT JOIN building ON rooms.building_id = buildings.id
                   WHERE avg_draw_number > %d and avg_draw_number < %d;""" % (lower, upper)
        self.cursor.execute(query)

        return self.cursor.fetchall()

    def specific_room_possibility(self, converted_draw_number, room, building):
        ''' Returns one of ["Stretch", "Target", "Safety", "Draw Not Available"] '''
        query = """SELECT avg_draw_number
                   FROM rooms
                   LEFT JOIN building ON rooms.building_id = buildings.id
                   WHERE building = %s and room = %s;""" % (building, room)
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        upper_target_bound = converted_draw_number + 30
        lower_target_bound = converted_draw_number - 30

        if len(result) > 0:
            avg_draw_number = result[0][0]
            if avg_draw_number < lower_target_bound:
                return "Stretch"
            elif avg_draw_number >= lower_target_bound and avg_draw_number <= upper_target_bound:
                return "Target"
            elif avg_draw_number > upper_target_bound:
                return "Safety"
            else:
                raise Exception('Number Not Available')
        else:
            return "Draw Not Available"

    def convert_number(self, user_input):
        query = """SELECT db_num
                   FROM number_map
                   WHERE roomdraw_num = %d;""" % (user_input)
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        if len(result) > 0:
            return result[0][0]
        else:
            raise Exception('Invalid Room Draw Number') # Raised if number not between 1000 and 4000

    
    # def get_rooms_by_number(self, number):
    #     query = 'SELECT draw_number, building, room_number, occupancy FROM roomdraw WHERE draw_number > %s' % number
    #     self.cursor.execute(query)

    #     return self.cursor.fetchall()


if __name__ == "__main__":
    db = DataSource()
    print db.get_rooms_by_number('1001')