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
            self.connection = psycopg2.connect(database=self.database,
                                               user=self.user,
                                               password=self.password)
            self.cursor = self.connection.cursor()
        except Exception, e:
            raise e

    def close(self):
        self.connection.close()

    def get_rooms_by_preference(self, user_input_building = "",
                                      user_input_occupancy = 0,
                                      user_input_environment = ""):
        self.query = """SELECT avg_draw_number, building, room
                   FROM rooms
                   LEFT JOIN buildings ON rooms.building_id = buildings.id \n"""

        if user_input_occupancy > 0:
            if "WHERE" in self.query:
                self.query += " AND "
            else:
                self.query += " WHERE "
            self.query += "occupancy = %d" % user_input_occupancy

        if user_input_environment == "sub_free":
            if "WHERE" in self.query:
                self.query += " AND "
            else:
                self.query += " WHERE "
            self.query += "sub_free = 't'"

        if user_input_environment == "quiet":
            if "WHERE" in self.query:
                self.query += " AND "
            else:
                self.query += " WHERE "
            self.query += "quiet = 't'"

        if user_input_building:
            if "WHERE" in self.query:
                self.query += " AND "
            else:
                self.query += " WHERE "
            self.query += "building = \'%s\'" % user_input_building

        self.query += ";"

        self.cursor.execute(self.query)

        return self.cursor.fetchall()

    def get_rooms_like_this(self, converted_draw_number,
                                  user_input_environment,
                                  user_input_occupancy,
                                  user_input_building):
        ''' Returns a list of rooms in the format:
                        [building, room] '''

        rooms = self.get_rooms_by_preference(user_input_building, user_input_occupancy, user_input_environment)

        for room in rooms:

        else:
            return

        return

    def get_rooms_far_away(self, converted_enemy_number,
                                 converted_draw_number):
        ''' Returns a list of rooms in the format:
                [building, room, occupancy, sub_free, quiet]
            that are at least 250 meters away from each other.'''

        # Find enemy's target room
        self.query = """SELECT building, room, occupancy, sub_free, quiet, geo_lat, geo_long, abs(avg_draw_number - %d) as draw_distance
                   FROM rooms
                   LEFT JOIN buildings ON rooms.building_id = buildings.id
                   ORDER BY draw_distance ASC;""" % (converted_enemy_number)
        self.cursor.execute(self.query)

        enemy_list = self.cursor.fetchall()

        if enemy_list:
            enemy_target_room = enemy_list[0]
            enemy_lat = enemy_target_room[5]
            enemy_lon = enemy_target_room[6]
        else:
            raise Exception('Something went wrong while determining your enemy\'s best room!')

        # Find room at least 250m away
        self.query = """SELECT building, room, occupancy, sub_free, quiet
                   FROM rooms
                   LEFT JOIN buildings ON rooms.building_id = buildings.id
                   WHERE acos(sin(geo_lat) + sin(%f) + cos(geo_lat)*cos(%f)*(cos(%f-geo_lon)))*6371000 > 250;""" % (enemy_lat, enemy_lat enemy_lon)
        self.cursor.execute(self.query)

        return self.cursor.fetchall()

    def get_rooms_near_location(self, converted_draw_number,
                                      favorite_location):

        # Get favorite_location latlon
        self.query = """SELECT building, geo_lat, geo_long,
                   FROM buildings
                   WHERE building = %s""" % (favorite_location)
        self.cursor.execute(self.query)

        location_list = self.cursor.fetchall()

        if location_list:
            favorite_location = location_list[0]
            fav_location_lat = favorite_location[0]
            fav_location_lon = favorite_location[1]
        else:
            raise Exception('Something went wrong while determining your favorite location!')

        # Find room further than 250m away
        self.query = """SELECT building, room, occupancy, sub_free, quiet
                   FROM rooms
                   LEFT JOIN buildings ON rooms.building_id = buildings.id
                   WHERE acos(sin(geo_lat) + sin(%f) + cos(geo_lat)*cos(%f)*(cos(%f-geo_lon)))*6371000 < 250""" % (fav_location_lat, fav_location_lat, fav_location_lon)
        self.cursor.execute(self.query)

        return self.cursor.fetchall()

    def get_rooms_in_range(self, lower, upper):
        ''' Returns a list of rooms in the format:
                [building, room, occupancy, sub_free, quiet] '''
        self.query = """SELECT building, room, occupancy, sub_free, quiet
                   FROM rooms
                   LEFT JOIN buildings ON rooms.building_id = buildings.id
                   WHERE avg_draw_number > %d and avg_draw_number < %d;""" % (lower, upper)
        self.cursor.execute(self.query)

        return self.cursor.fetchall()

    def specific_room_possibility(self, converted_draw_number,
                                        room,
                                        building):
        ''' Returns one of ["Stretch", "Target", "Safety", "Draw Not Available"] '''
        self.query = """SELECT avg_draw_number
                   FROM rooms
                   LEFT JOIN buildings ON rooms.building_id = buildings.id
                   WHERE building = \'%s\' and room = %s;""" % (building, room)
        self.cursor.execute(self.query)
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
        self.query = """SELECT db_num
                   FROM number_map
                   WHERE roomdraw_num = %d;""" % (user_input)
        self.cursor.execute(self.query)
        result = self.cursor.fetchall()

        if len(result) > 0:
            return result[0][0]
        else:
            raise Exception('Invalid Room Draw Number') # Raised if number not between 1000 and 4000


    # def get_rooms_by_number(self, number):
    #     self.query = 'SELECT draw_number, building, room_number, occupancy FROM roomdraw WHERE draw_number > %s' % number
    #     self.cursor.execute(self.query)

    #     return self.cursor.fetchall()

''' Tests '''
if __name__ == "__main__":
    db = DataSource()
    print "Specific Room Possibility:"
    print db.specific_room_possibility(182, 213, "Cassat Hall")
    print db.query
    print
    print "Get Rooms By Preference:"
    print db.get_rooms_by_preference(user_input_building = "Cassat Hall", user_input_occupancy = 1, user_input_environment = "sub_free")
    print db.query
    print
    print "Get Rooms In Range:"
    print db.get_rooms_in_range(462, 402)
    print db.query
