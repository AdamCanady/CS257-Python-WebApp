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

    def get_rooms_by_number(self, number):
        query = 'SELECT draw_number, building, room_number, occupancy FROM roomdraw WHERE draw_number > %s' % number
        self.cursor.execute(query)

        return self.cursor.fetchall()

    def get_rooms_by_occupancy(self, occupancy):
        '''Takes an integer and returns a list of rooms matching that occupancy'''

        rooms = []

        # Implementation soon...

        return rooms

    def get_list_of_available_rooms(self):
        '''Returns a list of all of the rooms ResLife offers'''

        rooms = []

        # Implementation soon...

        return rooms

    def get_rooms_by_environment(self, type):
        '''Takes an environment ('quiet','single_gender','subfree','interest_house') and
            returns a list of matching rooms'''

        rooms = []

        # Implementation soon...

        return rooms

    def get_rooms_near_location(self, location):
        '''Takes a location string and finds rooms close to that location'''

        rooms = []

        # Implementation soon...

        return rooms

    def get_rooms_by_location(self, location):
        '''Takes a location string and finds rooms in that hall/house'''

        rooms = []

        # Implementation soon...

        return rooms

if __name__ == "__main__":
    db = DataSource()
    print db.get_rooms_by_number('1001')