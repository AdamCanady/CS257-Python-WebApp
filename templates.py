'''templates.py

CS 257 Python Web App, Fall 2013, Jeff Ondich
Jiatao Cheng, Erin Wilson, and Adam Canady

This file defines the HTML used in this project.
'''

class Templates():

    def __init__(self):
        self.start_page = open('templates/front_page.html')

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
        return self.start_page.read()

''' Tests '''
if __name__ == "__main__":
    templates = Templates()
    print templates.get_start_page()
    print templates.get_results_page(1)