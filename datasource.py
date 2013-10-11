'''datasource.py

CS 257 Python Web App, Fall 2013, Jeff Ondich
Jiatao Cheng, Erin Wilson, and Adam Canady

Some of the following code is from Jeff Ondich's psycopg2-demo.py
'''

class DataSource:
    def __init__(self):

        # Start with the database login info
        self.database = 'canadya'
        self.user = 'canadya'
        self.password = 'star925propane'

        # Login to the database
        try:
            self.connection = psycopg2.connect(database=database, user=user, password=password)
            self.cursor = connection.cursor()
        except Exception, e:
            raise e

    def get_rooms_by_number(self, number):
        query = 'SELECT draw_number, building, room_number, occupancy FROM roomdraw WHERE draw_number > %s' % user_draw_number
        cursor.execute(query)

        return cursor.fetchall()

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
    DataSource()