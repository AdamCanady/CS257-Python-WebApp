#!/usr/bin/python

import cgi

# Get the user input
form = cgi.FieldStorage()

# ***** SANITIZE USER INPUT HERE ****

start_page = '''<!DOCTYPE HTML>
<html>
<head>
    <title>Room Finder Extraordinaire -- Start Page</title>
</head>

<body>
	<h1>Room Finder Extraordinaire</h1>
    <h2> Which Room can I get? </h2>
    <form action="webapp.py" method="get">
        <p>Room Draw Number? <input type="text" name="draw_number" /></p>
        <p><input type="submit" value="FIND ME A ROOM!!" /></p>
    </form>

    <h2> Can I get my dream room?? </h2>
    <form action="webapp.py" method="get">
    	<p>Room Draw Number? <input type="text" name="draw_number" /></p>
    	<p>Hall or House Name? <input type="text" name="building" /></p>
    	<p>Number of Desired Room? <input type="text" name="room_number" /></p>
    	<p>Desired Occupancy? <input type="text" name="occupancy" /></p>
    	<p>Desired Environment? <input type="radio" name="environment" value"subfree">Sub-Free 
           <input type="radio" name="environment" value"quiet">Quiet</p>
    	<p><input type="submit" value="FIND ME A ROOM!!" /></p>

    <h2> What's the best room I can find near my favorite location on campus? </h2>
    <form action="webapp.py" method="get">
        <p>Room Draw Number? <input type="text" name="draw_number" /></p>
        <p>Favorite Location? <input type="text" name="favorite_loc" /></p>
        <p><input type="submit" value="FIND ME A ROOM!!" /></p>
    </form>

    <h2> How can I avoid my mortal enemy? </h2>
    <form action="webapp.py" method="get">
        <p>YOUR Room Draw Number? <input type="text" name="my_draw_number" /></p>
        <p>ENEMY'S Room Draw Number? <input type="text" name="enemy_draw_number" /></p>
        <p><input type="submit" value="FIND ME A ROOM!!" /></p>
    </form>




</body>
</html>
'''


print "Content-type: text/html\r\n\r\n"

if 'animal' in form and 'badanimal' in form:
	animal = form['animal'].value
	badAnimal = form['badanimal'].value

	lol_page = '''<DOCTYPE HTML>
	<html>
	<head>
	    <title>Tiny web app results</title>
	</head>

	<body>
	    <p>I like %ss, too.</p>
	    <p>Also, %ss are gross.</p>
	</body>
	</html>''' % (animal, badAnimal)

	print lol_page
else:
	print start_page



