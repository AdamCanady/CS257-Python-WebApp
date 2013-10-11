'''templates.py

CS 257 Python Web App, Fall 2013, Jeff Ondich
Jiatao Cheng, Erin Wilson, and Adam Canady

This file defines the HTML used in this project.
'''

class Templates():
    def __init__(self):
        pass

    def get_results_page(self, content):
        results_page = '''
        <html>
            <head>
                <title>Room Finder Extraordinaire - Probable Rooms</title>
            </head>

            <body>
                %s
            </body>
        </html>
        ''' % str(content)
        return results_page

    def get_start_page(self):
        start_page = '''<!DOCTYPE HTML>
            <html>
            <head>
                <title>Room Finder Extraordinaire -- Start Page</title>
            </head>

            <body>
                <h1>Room Finder Extraordinaire</h1>
                <h2>Which Room can I get?</h2>
                <form action="index.py" method="get">
                    <p>Room Draw Number? <input type="text" name="draw_number" /></p>
                    <p><input type="submit" value="FIND ME A ROOM!!" /></p>
                </form>

                <h2>Can I get my dream room??</h2>
                <form action="index.py" method="get">
                    <p>Room Draw Number? <input type="text" name="draw_number"/></p>
                    <p>Hall or House Name?
                        <select name="dorms_houses">
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
                        </select>
                    </p>
                    <p>Number of Desired Room? <input type="text" name="room_number" /></p>
                    <p>Desired Occupancy? <input type="radio" name="capacity" value"single"> Single
                        <input type="radio" name="capacity" value"double"> Double
                        <input type="radio" name="capacity" value"triple"> Triple
                        <input type="radio" name="capacity" value"quad_plus"> Quad+</p>
                    <p>Desired Environment? <input type="radio" name="environment" value"subfree"> Sub-Free
                       <input type="radio" name="environment" value"quiet"> Quiet
                       <input type="radio" name="environment" value"single_gender"> Single Gender
                       <input type="radio" name="environment" value"interest_house"> Interest House
                    <p><input type="submit" value="FIND ME A ROOM!!" /></p>

                <h2>What's the best room I can find near my favorite location on campus?</h2>
                <form action="index.py" method="get">
                    <p>Room Draw Number? <input type="text" name="draw_number" /></p>
                    <p>Favorite Location?
                        <select name="fav_locations">
                            <option value="">Select A Location</option>
                            <option value="sayles">Sayles</option>
                            <option value="willis">Willis</option>
                            <option value="hulings">Hulings</option>
                            <option value="olin">Olin</option>
                            <option value="mudd">Mudd</option>
                            <option value="cmc">CMC</option>
                            <option value="boliou">Boliou</option>
                            <option value="laird">Laird</option>
                            <option value="gould">Gould</option>
                            <option value="leighton">Leighton</option>
                            <option value="west_athletic_complex">West Athletic Complex</option>
                            <option value="recreation_center">Recreation Center</option>
                            <option value="downtown_northfield">Downtown Northfield</option>
                            <option value="st_olaf">St Olaf</option>
                            <option value="bald_spot">Bald Spot</option>
                            <option value="weitz">Weitz</option>
                            <option value="mini_bald_spot">Mini Bald Spot</option>
                            <option value="upper_arb">Upper Arb</option>
                            <option value="lower_arb">Lower Arb</option>
                            <option value="cowling">Cowling</option>
                            <option value="bell_field">Bell Field</option>
                            <option value="ldc">LDC</option>
                            <option value="goodsell">Goodsell</option>
                            <option value="concert_hall">Concert Hall</option>
                            <option value="music_hall">Music Hall</option>
                            <option value="scoville">Scoville</option>
                            <option value="facilities">Facilities</option>
                            <option value="tunnels">Tunnels</option>
                        </select>
                    </p>
                    <p><input type="submit" value="FIND ME A ROOM!!" /></p>
                </form>

                <h2>How can I avoid my mortal enemy?</h2>
                <form action="index.py" method="get">
                    <p>YOUR Room Draw Number? <input type="text" name="my_draw_number" /></p>
                    <p>ENEMY'S Room Draw Number? <input type="text" name="enemy_draw_number" /></p>
                    <p><input type="submit" value="FIND ME A ROOM!!" /></p>
                </form>

            </body>
            </html>
            '''
        return start_page


if __name__ == "__main__":
    templates = Templates()
    templates.get_start_page()
    templates.get_results_page(1)