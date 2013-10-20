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

    # Function to generate queries based on preferences indicated by the user in web form
    def get_rooms_by_preference(self, user_input_building = "",
                                      user_input_occupancy = 0,
                                      user_input_environment = ""):

        self.query = """SELECT MIN(roomdraw_num), building, room
                   FROM rooms
                   LEFT JOIN buildings ON rooms.building_id = buildings.id
                   LEFT JOIN number_map ON avg_draw_number = number_map.db_num\n"""

        # The if/else clauses are used to determine if we need to create
        # a new WHERE block or add to an existing one
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

        self.query += "GROUP BY building, room;"

        self.cursor.execute(self.query)

        return self.cursor.fetchall()

    # Function that takes user preferences as input and returns lists of rooms
    # with certain categorical probability given the user's draw number
        # Stretch: not likely to get this room
            # (rooms with average draws < 30 of you)
        # Target: number is right in range of getting this room
            # (rooms with average draws within +/- 30 of you)
        # Safety: very likely to get this room
            # (rooms with average draws > 30 of you)
    def get_rooms_like_this(self, converted_draw_number,
                                  user_input_environment,
                                  user_input_occupancy,
                                  user_input_building):
        ''' Returns a list of rooms in the format:
                        [building, room] '''

        rooms = self.get_rooms_by_preference(user_input_building, user_input_occupancy, user_input_environment)

        # calculate span of user's target rooms
        upper_target_bound = converted_draw_number + 30
        lower_target_bound = converted_draw_number - 30

        stretch = []
        target = []
        safety = []

        # Sort rooms into categories of likeliness
        if not rooms:
            raise Exception("No rooms found that match your preferences... :(")

        for room in rooms:
            if room[0] < lower_target_bound:
                stretch.append(room)

            elif room[0] >= lower_target_bound and room[0] < upper_target_bound:
                target.append(room)

            elif room[0] >= upper_target_bound:
                safety.append(room)

        return stretch, target, safety

    # Function to help a user avoid an enemy because we are on such a small campus!
    def get_rooms_far_away(self, converted_enemy_number,
                                 converted_draw_number):
        ''' Returns a list of rooms in the format:
                [building, room, occupancy, sub_free, quiet]
            that are at least 250 meters away from each other.'''

        # Find enemy's target room where "target room" is defined as the
        # room whose average draw number is closest to the enemy's draw number
        self.query = """SELECT building, room, occupancy, sub_free, quiet, geo_lat, geo_long, abs(avg_draw_number - %d) as draw_distance
                   FROM rooms
                   LEFT JOIN buildings ON rooms.building_id = buildings.id
                   ORDER BY draw_distance ASC;""" % (converted_enemy_number)
        self.cursor.execute(self.query)

        enemy_list = self.cursor.fetchall()

        if enemy_list:
            enemy_target_room = enemy_list[0]
            enemy_lat = enemy_target_room[5]
            enemy_long = enemy_target_room[6]
        else:
            raise Exception('Something went wrong while determining your enemy\'s best room!')

        # Find rooms outside a 250m radius from enemy's target room
        self.query = """SELECT MIN(roomdraw_num), building, room, occupancy, sub_free, quiet, avg_draw_number
                   FROM rooms
                   LEFT JOIN buildings ON rooms.building_id = buildings.id
                   LEFT JOIN number_map ON avg_draw_number = number_map.db_num
                   WHERE sqrt(power((geo_lat - %s),2) + power((geo_long - %s),2))*79208 > 250
                   GROUP BY building, room, occupancy, sub_free, quiet, avg_draw_number;""" % (enemy_lat, enemy_long)
        self.cursor.execute(self.query)

        results = self.cursor.fetchall()

        # calculate span of user's target rooms
        upper_target_bound = converted_draw_number + 30
        lower_target_bound = converted_draw_number - 30

        stretch = []
        target = []
        safety = []

        # Sort rooms into categories of likeliness
        if not results:
            Exception('No rooms found :(')
        for room in results:
            if room[6] < lower_target_bound:
                stretch.append(room[:6])

            elif room[6] >= lower_target_bound and room[6] < upper_target_bound:
                target.append(room[:6])

            elif room[6] >= upper_target_bound:
                safety.append(room[:6])

        return enemy_target_room, stretch, target, safety

    # Function to help a user find a room near a favorite location
    def get_rooms_near_location(self, converted_draw_number,
                                      favorite_location):

        # Get favorite_location latlon
        self.query = """SELECT building, geo_lat, geo_long
                   FROM buildings
                   WHERE building = \'%s\'""" % (favorite_location)
        self.cursor.execute(self.query)

        location_list = self.cursor.fetchall()

        if location_list:
            favorite_location = location_list[0]
            fav_location_lat = favorite_location[1]
            fav_location_long = favorite_location[2]
        else:
            raise Exception('Something went wrong while determining your favorite location!')

        # Find room within 250m radius of favorite location
        self.query = """SELECT MIN(roomdraw_num), building, room, occupancy, sub_free, quiet, avg_draw_number
                   FROM rooms
                   LEFT JOIN buildings ON rooms.building_id = buildings.id
                   LEFT JOIN number_map ON avg_draw_number = number_map.db_num
                   WHERE sqrt(power((geo_lat - %s),2) + power((geo_long - %s),2))*79208 < 250
                   GROUP BY building, room, occupancy, sub_free, quiet, avg_draw_number;""" % (fav_location_lat, fav_location_long)

        self.cursor.execute(self.query)

        results = self.cursor.fetchall()

        # calculate span of user's target rooms
        upper_target_bound = converted_draw_number + 30
        lower_target_bound = converted_draw_number - 30

        stretch = []
        target = []
        safety = []

        # Sort rooms into categories of likeliness
        for room in results:
            if room[6] < lower_target_bound:
                stretch.append(room[:6])

            elif room[6] >= lower_target_bound and room[6] < upper_target_bound:
                target.append(room[:6])

            elif room[6] >= upper_target_bound:
                safety.append(room[:6])
        else:
            Exception('No rooms found :(')

        return stretch, target, safety

    # General function to retrieve rooms within a given range of average draw numbers
    def get_rooms_in_range(self, lower, upper):
        ''' Returns a list of rooms in the format:
                [building, room, occupancy, sub_free, quiet] '''
        self.query = """SELECT MIN(roomdraw_num), building, room, occupancy, sub_free, quiet
                   FROM rooms
                   LEFT JOIN buildings ON rooms.building_id = buildings.id
                   LEFT JOIN number_map ON avg_draw_number = number_map.db_num
                   WHERE avg_draw_number > %d and avg_draw_number < %d
                   GROUP BY building, room;""" % (lower, upper)
        self.cursor.execute(self.query)

        return self.cursor.fetchall()

    # Function that reports the probability that you can get a specific room
    # (Stretch, Target, or Safety)
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

        # Find the category that the user's preferred room falls into
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

    # Function convert an assigned draw number to a number usable by the database
        # (1001 = 1, 1002 = 2, etc)
        # Note: because each class starts at _001 and ends around _510, real draw number 2001
        # was assigned 511 in the database so that all draw numbers are continuous across classes.
        # This is important for being able to accurately average draw numbers
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
