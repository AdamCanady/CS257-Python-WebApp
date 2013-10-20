#!/usr/bin/python
'''index.py

CS 257 Python Web App, Fall 2013, Jeff Ondich
Jiatao Cheng, Erin Wilson, and Adam Canady

This is the code that creates our finalized web app's backend.

Some of the code from this file was derived from Jeff Ondich's tinywebapp.py
'''

import cgi
import cgitb
cgitb.enable()

import datasource
import templates

gen = templates.Templates()

print "Content-type: text/html\r\n\r\n"

# Get the user input
form = cgi.FieldStorage()

# If a form was submitted, do something about it!
if 'form_type' in form:
    # try:
        # Define the database and connect
        db = datasource.DataSource()

        # Displays all available rooms
        if form['form_type'].value == "available_rooms":
            title = "Available Rooms"

            # Get inputs
            building = form['building'].value
            if building == "no_preference":
                building = ""
            environment = form['environment'].value
            if environment == "no_preference":
                environment = ""
            occupancy = int(form['occupancy'].value)

            # Query DB for info
            result = db.get_rooms_by_preference(building, occupancy, environment)

            # Build output
            content = gen.make_table(result, ['Average Draw Number', 'Building', 'Room Number'])

            gen_page = gen.make_results_page(title, content)

            # Send output
            print gen_page

        # Displays rooms and likeliness given user's draw number
        if form['form_type'].value == "which_rooms":
            title = "Here's a list of rooms you could get:"

            # Get inputs
            draw_number = int(form['draw_number'].value)

            converted_draw_number = db.convert_number(draw_number)

            stretch_number = converted_draw_number - 30
            safety_number = converted_draw_number + 30

            # Query DB for info
            stretch = db.get_rooms_in_range(0, stretch_number)
            target = db.get_rooms_in_range(stretch_number, safety_number)
            safety = db.get_rooms_in_range(safety_number, 10000)

            # Build output
            headers = ["Average Draw Number", "Building", "Room", "Occupancy", "Sub Free?", "Quiet?"]

            stretch_table = gen.make_table(stretch, headers)
            target_table = gen.make_table(target, headers)
            safety_table = gen.make_table(safety, headers)

            content = ""

            if stretch:
                content += "<h3>Stretch Rooms</h3>\n"
                content += stretch_table
            if target:
                content += "<h3>Target Rooms</h3>\n"
                content += target_table
            if safety:
                content += "<h3>Safety Rooms</h3>\n"
                content += safety_table

            gen_page = gen.make_results_page(title, content)

            # Send output
            print gen_page

        # Displays likeliness of a user drawing their dream room
        if form['form_type'].value == "dream_room":
            title = "Dream Room Results"

            # Get inputs
            room_number = int(form['room_number'].value)
            draw_number = int(form['draw_number'].value)
            converted_draw_number = db.convert_number(draw_number)
            building = form['building'].value

            # Query DB for info
            result = db.specific_room_possibility(converted_draw_number, room_number, building)

            if result == "Stretch":
                content = "This room would be a STRETCH room given your draw number."

            elif result == "Target":
                content = "This room would be a TARGET room given your draw number."

            elif result == "Safety":
                content = "This room would be a SAFETY room given your draw number."

            elif result == "Draw Not Available":
                content = "Either this room is not availabe for drawing, or we don't have data on it"

            gen_page = gen.make_results_page(title, content)

            # Send output
            print gen_page

        # Displays lists of rooms that match user indicated preferences and
        # the likelihood of getting those rooms
        if form['form_type'].value == "room_like_this":
            title = "Here are some rooms that fit your preferences:"

            # Get inputs
            draw_number = int(form['draw_number'].value)
            converted_draw_number = db.convert_number(draw_number)
            environment = form['environment'].value
            if environment == "no_preference":
                environment = ""
            occupancy = int(form['occupancy'].value)
            building = form['building'].value
            if building == "no_preference":
                building = ""

            # Query DB for info
            stretch, target, safety = db.get_rooms_like_this(converted_draw_number, environment, occupancy, building)

            # Build output
            headers = ['Average Draw Number', 'Building', 'Room']
            stretch_table = gen.make_table(stretch, headers)
            target_table = gen.make_table(target, headers)
            safety_table = gen.make_table(safety, headers)

            content = ""

            if stretch:
                content += "<h3>Stretch Rooms</h3>\n"
                content += stretch_table
            if target:
                content += "<h3>Target Rooms</h3>\n"
                content += target_table
            if safety:
                content += "<h3>Safety Rooms</h3>\n"
                content += safety_table

            gen_page = gen.make_results_page(title, content)

            # Send output
            print gen_page

        # Displays lists of rooms within 250m of user's favorite location and
        # the likelihood of getting those rooms
        if form['form_type'].value == "best_room_near_location":
            title = "Here are some rooms near " + form['favorite_location'].value

            # Get inputs
            draw_number = int(form['draw_number'].value)
            converted_draw_number = db.convert_number(draw_number)
            favorite_location = form['favorite_location'].value

            # Query DB for info
            stretch, target, safety = db.get_rooms_near_location(converted_draw_number, favorite_location)

            # Build output
            headers = ["Average Draw Number", "Building", "Room", "Occupancy", "Sub Free?", "Quiet?"]

            stretch_table = gen.make_table(stretch, headers)
            target_table = gen.make_table(target, headers)
            safety_table = gen.make_table(safety, headers)

            content = ""

            if stretch:
                content += "<h3>Stretch Rooms</h3>\n"
                content += stretch_table
            if target:
                content += "<h3>Target Rooms</h3>\n"
                content += target_table
            if safety:
                content += "<h3>Safety Rooms</h3>\n"
                content += safety_table

            gen_page = gen.make_results_page(title, content)

            # Send output
            print gen_page

        # Displays rooms outside of a 250m radius of an enemy's target room
        if form['form_type'].value == "mortal_enemy":
            title = "Mortal Enemy Avoider"

            # Get inputs
            enemy_number = int(form['enemy_number'].value)
            converted_enemy_number = db.convert_number(enemy_number)
            draw_number = int(form['draw_number'].value)
            converted_draw_number = db.convert_number(draw_number)

            # Query DB for info
            enemy_target_room, stretch, target, safety = db.get_rooms_far_away(converted_enemy_number, converted_draw_number)

            # Build output
            content = "<h2>Your mortal enemy will probably choose %s %s.</h2>\n" % (enemy_target_room[0], enemy_target_room[1])

            content += "<h3>So you should choose one of the following:</h3>\n"

            headers = ["Average Draw Number", "Building", "Room", "Occupancy", "Sub Free?", "Quiet?"]

            stretch_table = gen.make_table(stretch, headers)
            target_table = gen.make_table(target, headers)
            safety_table = gen.make_table(safety, headers)

            if stretch:
                content += "<h3>Stretch Rooms</h3>\n"
                content += stretch_table
            if target:
                content += "<h3>Target Rooms</h3>\n"
                content += target_table
            if safety:
                content += "<h3>Safety Rooms</h3>\n"
                content += safety_table

            gen_page = gen.make_results_page(title, content)

            # Send output
            print gen_page

    # except:
    #     print gen.get_error_page()

else:
    print gen.get_start_page()
