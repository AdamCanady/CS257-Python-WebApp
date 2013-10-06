#!/usr/bin/python

try:
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
            <p>Hall or House Name? <select name="dorms_houses">\
                                    <option value="">Select A Hall/House</option>
                                    <option value="burton">Burton</option>
                                    <option value="cassat">Cassat</option>
                                    <option value="davis">Davis</option>
                                    <option value="evans">Evans</option>
                                    <option value="goodhue">Goodhue</option>
                                    <option value="james">James</option>
                                    <option value="myers">Myers</option>
                                    <option value="nourse">Nourse</option>
                                    <option value="severance">Severance</option>
                                    <option value="watson">Watson</option>
                                    <option value="allen">Allen</option>
                                    <option value="benton">Benton</option>
                                    <option value="berg">Berg</option>
                                    <option value="brooks">Brooks</option>
                                    <option value="chaney">Chaney</option>
                                    <option value="clader">Clader</option>
                                    <option value="collier">Collier</option>
                                    <option value="colwell">Colwell</option>
                                    <option value="dacie_moses">Dacie Moses</option>
                                    <option value="dixon">Dixon</option>
                                    <option value="douglas">Douglas</option>
                                    <option value="dow">Dow</option>
                                    <option value="eugster">Eugster</option>
                                    <option value="faculty_club">Faculty Club</option>
                                    <option value="farm">Farm</option>
                                    <option value="geffert">Geffert</option>
                                    <option value="hall">Hall</option>
                                    <option value="henrickson">Henrickson</option>
                                    <option value="hill">Hill</option>
                                    <option value="hunt_cottage">Hunt Cottage </option>
                                    <option value="hunt">Hunt</option>
                                    <option value="huntington">Huntington</option>
                                    <option value="jewett">Jewett</option>
                                    <option value="nason">Nason</option>
                                    <option value="owens">Owens</option>
                                    <option value="page">Page</option>
                                    <option value="parish">parish</option>
                                    <option value="parr">Parr</option>
                                    <option value="prentice">Prentice</option>
                                    <option value="rice">Rice</option>
                                    <option value="scott">Scott</option>
                                    <option value="stimson">Stimson</option>
                                    <option value="williams">Williams</option>
                                    <option value="wilson">Wilson</option>
                                    </p>
            <p>Number of Desired Room? <input type="text" name="room_number" /></p>
            <p>Desired Occupancy? <input type="radio" name="environment" value"single">Single 
                <input type="radio" name="environment" value"double">Double
                <input type="radio" name="environment" value"triple">Triple
                <input type="radio" name="environment" value"quad_plus">Quad+</p>
            <p>Desired Environment? <input type="radio" name="environment" value"subfree">Sub-Free 
               <input type="radio" name="environment" value"quiet">Quiet</p>
               <input type="radio" name="environment" value"single_gender">Single Gender</p>
               <input type="radio" name="environment" value"interest_house">Interest House</p>
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
except Exception, err:
    print err
    print traceback.format_exc()
