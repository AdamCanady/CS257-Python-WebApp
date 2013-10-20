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
    try:
        # Define the database and connect
        db = datasource.DataSource()

        if form['form_type'].value == "available_rooms":
            title = "Available Rooms"

            # Get inputs
            building = form['building'].value
            environment = form['environment'].value
            occupancy = int(form['occupancy'].value)

            # Query DB for info
            result = db.get_rooms_by_preference(building, occupancy, environment)

            # Build output
            content = gen.make_table(result)

            gen_page = gen.results_page(title, content)

            # Send output
            print gen_page

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
            headers = ["Building", "Room", "Occupancy", "Sub Free?", "Quiet?"]

            stretch_table = gen.make_table(stretch, headers)
            target_table = gen.make_table(target, headers)
            safety_table = gen.make_table(safety, headers)

            content = ""

            if stretch:
                content =+ "<h3>Stretch Rooms</h3>\n"
                content += stretch_table
            if target:
                content += "<h3>Target Rooms</h3>\n"
                content += target_table
            if safety:
                content += "<h3>Safety Rooms</h3>\n"
                content += safety_table

            gen_page = gen.results_page(title, content)

            # Send output
            print gen_page

        if form['form_type'].value == "dream_room":
            title = "Dream Room Results"

            # Get inputs
            room_number = int(form['room_number'].value)
            draw_number = int(form['draw_number'].value)
            building = form['building'].value

            # Query DB for info
            result = db.

            if result == "Stretch":
                content = "This room would be a stretch room given your draw number."

            elif result == "Target":
                content = "This room would be a target room given your draw number."

            elif result == "Safety":
                content = "This room would be a safety room given your draw number."

            elif result == "Draw Not Available":
                content = "Either this room is not availabe for drawing, or we don't have data on it"

            gen_page = gen.results_page(title, content)

            # Send output
            print gen_page

        if form['form_type'].value == "room_like_this":
            # Get inputs
            draw_number = int(form['draw_number'].value)
            environment = form['environment'].value
            occupancy = int(form['occupancy'].value)
            building = form['building'].value

            # Query DB for info
            result = db.

            # Build output
            content = gen.make_table(result)

            gen_page = gen.results_page(title, content)

            # Send output
            print gen_page

        if form['form_type'].value == "best_room_near_location":
            # Get inputs
            draw_number = int(form['draw_number'].value)
            favorite_location = form['favorite_location'].value

            # Query DB for info
            result = db.

            # Build output
            content = gen.make_table(result)

            gen_page = gen.results_page(title, content)

            # Send output
            print gen_page

        if form['form_type'].value == "mortal_enemy":
            enemy_number =
            draw_number =

            # Query DB for info
            result = db.get_rooms_far_away(enemy_number, draw_number)

            # Build output
            content = gen.make_table(result)

            gen_page = gen.results_page(title, content)

            # Send output
            print gen_page

    except:
        print gen.error_page()

else:
    print gen.get_start_page()
