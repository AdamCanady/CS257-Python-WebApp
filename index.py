#!/usr/bin/python
'''index.py

CS 257 Python Web App, Fall 2013, Jeff Ondich
Jiatao Cheng, Erin Wilson, and Adam Canady

This is a revision of our project outline that perform basic room draw
search functionality.

Some of the code from this file was derived from Jeff Ondich's tinywebapp.py
'''

import cgi
import cgitb
cgitb.enable()

import datasource
import templates

Templates = templates.Templates()

print "Content-type: text/html\r\n\r\n"

# Get the user input
form = cgi.FieldStorage()

# ***** SANITIZE USER INPUT HERE ****

# If a form was submitted, do something about it!
if 'draw_number' in form:
    # Get the user's draw number
    user_draw_number = form['draw_number'].value
    db = datasource.DataSource()

    # Now that we have their draw number, we can find probable rooms
    content = ''

    # We have a cursor now. Use it to print a table of results.
    content += "<p>These are the rooms that were drawn after your number in the past years:</p>"
    content += '<table border="1">\n'
    content += '<table border="1">\n<tr style="font-weight:bold;"><td>Draw Number</td> <td>Building</td> <td>Room Number</td> <td>Occupancy</td></tr>'
    for row in db.get_rooms_by_number(user_draw_number):
        content += '<tr><td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td></tr>' % (row[0], row[1], row[2], row[3])
    content += '</table>\n'

    # Close connection to DB
    db.close()

    print Templates.get_results_page(content)

else:
    print Templates.get_start_page()
